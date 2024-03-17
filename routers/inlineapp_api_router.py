from fastapi import APIRouter, Request
from schemas import ResponseBase

router = APIRouter(prefix="/inlineapp/api", tags=["inlineapp 接口"])
# router.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")
from service.inlineapp_service import InlineappService


@router.post("/orderadd", response_model=ResponseBase)
async def orderadd(request: Request):
    formdata = dict(await request.form())
    print(formdata)
    datas = await InlineappService.create_order(formdata)

    return ResponseBase(data={'data': datas})


@router.get("/orders/{token}", response_model=ResponseBase)
async def orders(token):
    datas = await InlineappService.orders(token)

    return ResponseBase(data={'data': datas})
