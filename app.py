from fastapi import FastAPI

from infrastructure.handlers.exception_handler import (
    register_exception_handlers,
)

app = FastAPI(title="App for franchise management")


register_exception_handlers(app)
