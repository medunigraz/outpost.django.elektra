import logging
from collections.abc import Mapping
from typing import (
    Final,
    Optional,
)

from celery import shared_task
from django.core.cache import cache
from lxml.etree import (
    Element,
    SubElement,
    _Element,
    tostring,
)

from .conf import settings

logger = logging.getLogger(__name__)


NSMAP: Final[dict[str, str]] = {
    "v1": "v1.upmproject.pure.atira.dk",
    "v3": "v3.commons.pure.atira.dk",
}

RESEARCHFIELD_CLASSIFICATION: Final[dict[int, str]] = {
    0: "none",
    1: "none",
    2: "neuroscience",
    3: "cancer",
    4: "shr",
    5: "none",
    6: "metabolism",
    7: "microbiome",
}


class ElektraTasks:
    @shared_task(bind=True, ignore_result=True, name=f"{__name__}.Elektra:generate")
    def generate(task):
        from . import models

        projects = models.ProjectImport.objects.filter(
            type="10", status="Projekt zur Umsetzung freigegeben"
        )

        nsmap = dict(NSMAP)
        root = Element(f"{{{nsmap['v1']}}}upmprojects", nsmap=nsmap)

        def to_xml(
            project, nsmap: Mapping[str, str], outer_root: Optional[_Element]
        ) -> _Element:
            """Build and return the XML element that represents this project."""
            root = SubElement(
                outer_root,
                f"{{{nsmap['v1']}}}upmproject",
                id=str(project.id),
                type="research",
            )

            activity_types = SubElement(root, f"{{{nsmap['v1']}}}activityTypes")
            activity_type = SubElement(activity_types, f"{{{nsmap['v1']}}}activityType")
            activity_type.text = "research"

            title = SubElement(root, f"{{{nsmap['v1']}}}title")
            title_text = SubElement(
                title, f"{{{nsmap['v3']}}}text", lang="en", country="GB"
            )
            title_text.text = project.title.get("de")

            if project.short:
                description_element = SubElement(root, f"{{{nsmap['v1']}}}acronym")
                description_element.text = project.short

            append_internal_participant(project, root, nsmap)
            append_organization(project, root, nsmap)

            start_date_element = SubElement(root, f"{{{nsmap['v1']}}}startDate")
            start_date_element.text = project.effective_start.strftime("%Y-%m-%d")
            end_date_element = SubElement(root, f"{{{nsmap['v1']}}}endDate")
            end_date_element.text = project.effective_end.strftime("%Y-%m-%d")

            if project.wibi_codes or project.research_field_ids:
                append_keywords(project, root, nsmap)

            visibility_element = SubElement(root, f"{{{nsmap['v1']}}}visibility")
            visibility_element.text = "Public"

            return root

        def get_logical_names(project) -> list[str]:
            """Return keyword group names that apply to this project."""
            groups: list[str] = []
            if project.wibi_codes:
                groups.append("/dk/atira/pure/keywords/wibi")
            if project.research_field_ids:
                groups.append("/dk/atira/pure/keywords/researchfields")
            return groups

        def append_text_element(
            parent: _Element, tag: str, text: str, **attributes: str
        ) -> _Element:
            """Create a new XML child element with text content and optional attributes."""
            element = SubElement(parent, tag, **attributes)
            element.text = text
            return element

        def append_internal_participant(
            project, root: _Element, nsmap: Mapping[str, str]
        ) -> None:
            """Append the internal project leader participant information to the XML root."""
            participant = SubElement(root, f"{{{nsmap['v1']}}}internalParticipants")
            internal_participant = SubElement(
                participant, f"{{{nsmap['v1']}}}internalParticipant"
            )
            append_text_element(
                internal_participant,
                f"{{{nsmap['v1']}}}personId",
                str(project.leader_id),
            )
            append_text_element(internal_participant, f"{{{nsmap['v1']}}}role", "pi")
            append_text_element(
                internal_participant,
                f"{{{nsmap['v1']}}}associationStartDate",
                project.effective_start.strftime("%Y-%m-%d"),
            )
            append_text_element(
                internal_participant,
                f"{{{nsmap['v1']}}}associationEndDate",
                project.effective_end.strftime("%Y-%m-%d"),
            )

        def append_organization(
            project, root: _Element, nsmap: Mapping[str, str]
        ) -> None:
            """Append organization and sponsor details to the XML root element."""
            organizations = SubElement(root, f"{{{nsmap['v1']}}}organisations")
            SubElement(
                organizations,
                f"{{{nsmap['v1']}}}organisation",
                id=str(project.organization_id),
            )

            external_organizations = SubElement(
                root,
                f"{{{nsmap['v1']}}}externalOrganisations",
            )

            for sponsor in project.sponsors:
                external_org_assoc = SubElement(
                    external_organizations,
                    f"{{{nsmap['v3']}}}externalOrganisationAssociation",
                )
                append_text_element(
                    external_org_assoc,
                    f"{{{nsmap['v3']}}}externalOrgName",
                    sponsor,
                )

            SubElement(
                root,
                f"{{{nsmap['v1']}}}managedByOrganisation",
                id=str(1),
            )

        def append_keywords(project, root: _Element, nsmap: Mapping[str, str]) -> None:
            """Append keyword groups to the XML representation based on project data."""
            keywords = SubElement(root, f"{{{nsmap['v1']}}}keywords")

            for logical_name in get_logical_names(project):
                logical_group = SubElement(
                    keywords,
                    f"{{{nsmap['v3']}}}logicalGroup",
                    logicalName=logical_name,
                )
                structured_keywords = SubElement(
                    logical_group,
                    f"{{{nsmap['v3']}}}structuredKeywords",
                )

                if logical_name == "/dk/atira/pure/keywords/wibi":
                    for wibi in project.wibi_codes:
                        classification_value = wibi[-3:]
                        SubElement(
                            structured_keywords,
                            f"{{{nsmap['v3']}}}structuredKeyword",
                            classification=classification_value,
                        )

                if logical_name == "/dk/atira/pure/keywords/researchfields":
                    for researchfield in project.research_field_ids:
                        SubElement(
                            structured_keywords,
                            f"{{{nsmap['v3']}}}structuredKeyword",
                            classification=RESEARCHFIELD_CLASSIFICATION.get(
                                researchfield, "none"
                            ),
                        )

        logger.info("Generating new XML body")
        for project in projects:
            root.append(to_xml(project, nsmap, root))

        body = tostring(
            root, xml_declaration=True, encoding="UTF-8", pretty_print=True
        ).decode()
        cache.set(settings.ELEKTRA_PROJECT_IMPORT_CACHE_KEY, body)
        logger.info(f"Finished generating new XML body with size {len(body)}")

        return body
