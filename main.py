import asyncio

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

# from src.bbapi.currency_data import get_currency
from src.currency.router import main_router

app = FastAPI()

app.mount('/static', StaticFiles(directory='static/templates'), name='static')

app.include_router(main_router)


if __name__ == '__main__':
    # asyncio.run(get_currency())
    uvicorn.run(app=app, host='127.0.0.1', port=5000)
