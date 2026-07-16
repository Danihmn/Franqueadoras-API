from typing import Annotated

from pydantic import AfterValidator
from validate_docbr import CNPJ as CNPJValidator

from domain.exceptions.cnpj import CNPJException

cnpj = CNPJValidator()


def validate_cnpj(v: str) -> str:
    if not cnpj.validate(v):
        raise CNPJException(v)
    return v


CNPJ = Annotated[str, AfterValidator(validate_cnpj)]
