class DomainException(Exception):
    """Execução base de todas as regras de negócio violadas"""

    def __init__(self, message: str, code: str = "DOMAIN ERROR"):
        self.message = message
        self.code = code
        super().__init__(message)
