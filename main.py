import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from src.posts.router import main_router

app = FastAPI()

app.mount('/static', StaticFiles(directory='static/templates'), name='static')

app.include_router(main_router)


if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=5000)
