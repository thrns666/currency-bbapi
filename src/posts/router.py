from fastapi import APIRouter, Form
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated

from src.bbapi.currency_data import get_currency

main_router = APIRouter()

templates = Jinja2Templates(directory='static/templates')


@main_router.get('/')
async def get_root(request: Request):
    return {'msg': 'im here'}


@main_router.get('/index')
async def index(request: Request):
    # currency_data_json = get_currency()
    return templates.TemplateResponse(request=request, name='index.html', context={}, status_code=200)


@main_router.post('/index')
async def take_data(
        request: Request,
        office: Annotated[str, Form()],
        currency_in: Annotated[str, Form()],
        currency_out: Annotated[str, Form()],
        cash_in: Annotated[str, Form()],
        cash_out: Annotated[str, Form()]
):
    print(office, currency_in, currency_out, cash_in, cash_out)

    sum = int(cash_in) + int(cash_out)
    print("total = ", sum)
    context = {
        'total': sum
    }

    return templates.TemplateResponse(request=request, name='index.html', context=context, status_code=200)
