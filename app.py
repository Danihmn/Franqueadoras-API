from fastapi import FastAPI

from infrastructure.exception_handlers import register_exception_handlers

app = FastAPI()


register_exception_handlers(app)
