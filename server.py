import json

from fastapi import FastAPI, Request
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
# from common.settings_local import TORTOISE_ORM
from common.settings import TORTOISE_ORM
from routers import (
    inlineapp_api_router,
)
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from schemas import ResponseBase
from common.err import *

app = FastAPI()


@app.exception_handler(BaseError)
async def err_handler(request, exc):
    return JSONResponse(status_code=200,
                        # content=ResponseBase(success=False, code=exc.code, msg=f'{exc.error}').model_dump())
                        content=ResponseBase(success=False, code=exc.code, msg=f'{exc.error}').dict())


# app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/img", StaticFiles(directory="ss"), name="img")
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    # generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)

app.include_router(inlineapp_api_router.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


if __name__ == '__main__':
    try:
        uvicorn.run(app, access_log=False, host='0.0.0.0', port=80)
    except BaseException as e:
        raise e
