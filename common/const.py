CART_TYPE = {
    "": "普通车牌",
    "30": "黑色车牌",
    "22": "临时车牌",
}
TIMESTR_LIST = ["00:00-12:00", "12:00-18:00", "18:00-24:00", "00:00-24:00", ]
COMMON_ORDER_PARAMS = [
    "identity", "activityDate", "activityId", "activityName", "areaId", "areaName", "category",
    "city", "county", "frameNum", "plateNum", "plateType", "province", "road", "timeId", "mobile",
]
ACTIVITY_NAME_LIST = ["梅沙景区", "大鹏半岛", "仙湖植物园停车场"]
JQ_ORDER_PARAMS_MAP = {
    17: {
        "activityName": "梅沙景区", "areaId": 17, "areaName": "梅沙片区", "category": 1,
    },
    18: {
        "activityName": "大鹏半岛", "areaId": 18, "areaName": "大鹏片区", "category": 1,
    },
    104: {
        "activityName": "仙湖植物园停车场", "areaId": 104, "areaName": "仙湖停车楼", "category": 2,
    },
}

COMMON_ORDER_PARAMS_MAP = {
    "identity": "P", "city": "深圳市", "county": "福田区", "frameNum": "", "province": "广东", "road": "梅林街道",
}

USER_ORER_PARAMS = ["mobile", "timeId", "plateType", "plateNum", "activityDate", "activityId", ]
# DP_HOST = 'yycx.szjj.sz.gov.cn'
