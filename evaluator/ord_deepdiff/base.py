from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class DiffReportKind(str, Enum):
    LIST_OF_COMPOUND_LISTS = "LIST_OF_COMPOUND_LISTS"

    LIST_OF_COMPOUNDS = "LIST_OF_COMPOUNDS"

    REACTION_CONDITIONS = "REACTION_CONDITIONS"

    LIST_OF_REACTION_WORKUPS = "LIST_OF_REACTION_WORKUPS"


class DiffReport(BaseModel):
    kind: DiffReportKind

    reference: dict | list[dict]

    actual: dict | list[dict]


class FieldChangeType(str, Enum):
    """ used to describe an entry from `DeepDiff` """

    # ref is None, act is not None (addition)
    ADDITION = "ADDITION"

    # ref is not None, act is None (removal)
    REMOVAL = "REMOVAL"

    # ref is not None, act is not None (change)
    ALTERATION = "ALTERATION"
