import re
from typing import Annotated

from pydantic import AfterValidator

from domain.exceptions.endereco import EnderecoException

UF_VALIDAS = {
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
    "SP", "SE", "TO",
}


def validate_cep(v: str) -> str:
    digits = re.sub(r"\D", "", v)
    if len(digits) != 8:
        raise EnderecoException(f"CEP INVALIDO: {v}")
    return digits


def validate_uf(v: str) -> str:
    uf = v.strip().upper()
    if uf not in UF_VALIDAS:
        raise EnderecoException(f"UF INVALIDA: {v}")
    return uf


CEP = Annotated[str, AfterValidator(validate_cep)]
UF = Annotated[str, AfterValidator(validate_uf)]
