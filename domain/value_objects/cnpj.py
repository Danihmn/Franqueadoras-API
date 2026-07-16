from validate_docbr import CNPJ as CNPJValidator

from domain.exceptions.cnpj import CNPJException

cnpj = CNPJValidator()


class CNPJ:
    def __init__(self, value):
        if not cnpj.validate(value):
            raise CNPJException(value=value)

        self.value = value

    def __eq__(self, other):
        return isinstance(other, CNPJ) and self.value == other.value

    def __repr__(self):
        return f"CNPJ({self.value})"
