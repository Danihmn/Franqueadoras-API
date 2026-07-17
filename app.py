from http import HTTPStatus

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from domain.exceptions.domain import DomainException

app = FastAPI(title="App for franchise management")


@app.exception_handler(DomainException)
def domain_exception_handler(
    request: Request, exc: DomainException
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={"detail": exc.message},
    )
