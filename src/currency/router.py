from fastapi import APIRouter, Form
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated
from src.bbapi.currency_data import get_currency, json_data, separate_filial, city_list

main_router = APIRouter()

templates = Jinja2Templates(directory='static/templates')


# Change name var a & r
@main_router.get('/filial_id/{bank_id}')
async def get_filial(
        request: Request,
        bank_id: str,
):
    r = separate_filial(json_data)
    a = r[bank_id]
    return templates.TemplateResponse(request=request, name='third.html', context={'BANK': a}, status_code=200)


@main_router.post('/filial_id/{bank_id}')
async def post_filial(
        request: Request,
        bank_id: str,
        currency_in: Annotated[str, Form()],
        currency_out: Annotated[str, Form()],
        cash_in: Annotated[str, Form()]
):
    r = separate_filial(json_data)
    a = r[bank_id]

    if currency_out == 'BYN_out':
        tot = float(cash_in) * float(a['in'][currency_in])
    elif currency_in == 'BYN_in':
        tot = float(cash_in) / float(a['out'][currency_out])
    else:
        tot = float(cash_in) * float(a['in'][currency_in]) / float(a['out'][currency_out])

    context = {
        'TOTAL': round(tot, 2),
        'TOTAL_CURRENCY': currency_out.split('_')[0],
        'BANK': a
               }

    print(bank_id, currency_in, currency_out, cash_in, f'total-{tot}')

    return templates.TemplateResponse(request=request, name='third.html', context=context, status_code=200)


@main_router.get('/')
async def get_index(request: Request):
    cities = city_list(json_data)

    return templates.TemplateResponse(
        request=request, name='zero.html', context={'CITY_LIST': cities}, status_code=200
    )


@main_router.post('/')
async def get_root(request: Request, city_name: Annotated[str, Form()]):
    res = list()
    for i in json_data:
        if city_name == i['name']:
            res.append(i)

    tot = separate_filial(res)

    return templates.TemplateResponse(
        request=request, name='second.html', context={'DATA': tot}, status_code=200
    )
