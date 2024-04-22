from fastapi import APIRouter, Form
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated
from src.bbapi.currency_data import get_currency, json_data, separate_filial

main_router = APIRouter()

templates = Jinja2Templates(directory='static/templates')


@main_router.get('/')
async def get_root(request: Request):
    currency_data_json = separate_filial(json_data)

    city_list = {}
    return templates.TemplateResponse(
        request=request, name='1.html', context={}, status_code=200
    )


@main_router.get('/index')
async def index(request: Request):
    # currency_data_json = get_currency()
    currency_data_json = separate_filial(json_data)

    # return templates.TemplateResponse(
    #     request=request,
    #     name='index.html',
    #     context={
    #         'cities': currency_data_json[''],
    #         'currency_in': currency_data_json['in'],
    #         'currency_out': currency_data_json['out'],
    #         'info': currency_data_json['info']
    #     },
    #     status_code=200
    # )

    return templates.TemplateResponse(
        request=request, name='index.html', context={'bb_api_data': currency_data_json}, status_code=200
    )


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
    print("total =", sum)
    context = {
        'total': sum
    }

    return templates.TemplateResponse(request=request, name='index.html', context=context, status_code=200)
