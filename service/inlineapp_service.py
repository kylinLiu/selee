import asyncio

import json

class InlineappService:


    @classmethod
    async def update_params(cls):
        print("yyyyyyyyyy")
        with open('C:/code/header', 'r') as f:
            return {"header": f.read()}

    @classmethod
    async def create_order(cls, formdata):
        print("xxxxxxxxxxxxx")
        header = formdata["header"]
        with open('C:/code/header', 'w') as f:
            f.write(header)
