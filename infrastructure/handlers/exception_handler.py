from http import HTTPStatus

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from domain.exceptions.cnpj import CNPJException
from domain.exceptions.domain import DomainException


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(DomainException, domain_exception_handler)  # type: ignore
    app.add_exception_handler(CNPJException, cnpj_exception_handler)  # type: ignore


def domain_exception_handler(
    request: Request, exc: DomainException
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={"detail": exc.message},
    )


def cnpj_exception_handler(
    request: Request, exc: CNPJException
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={"detail": exc.message},
    )
