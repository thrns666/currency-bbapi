from fastapi import APIRouter
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
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
async def take_data(request: Request, office: str, currency_in: str, currency_out: str):
    print(office, currency_in, currency_out)
    return 'ok 201'
