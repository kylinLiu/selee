from pydantic import BaseModel, Field
from utils.time import timestamp

class ResponseBase(BaseModel):
    """返回成功"""
    success: bool = Field(True, description="true-成功, false-失败")
    code: int = Field(200, description="code值: 200-成功, 99-服务器错误, 403-参数错误, 600-第三方接口错误, 1000-请求参数校验失败, 1095-服务超时")
    msg: str = Field(None, description="错误信息")
    data: dict = Field(None, description="数据")
    timestamp: int = Field(default_factory=timestamp, description='时间戳')
