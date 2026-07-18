from typing import Annotated

from pydantic import AfterValidator

from domain.exceptions.text import TextException


def validate_non_blank(v: str) -> str:
    if not v or not v.strip():
        raise TextException(v)
    return v.strip()


NON_BLANK_STR = Annotated[str, AfterValidator(validate_non_blank)]
