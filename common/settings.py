import os

from pathlib import Path

TORTOISE_ORM = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.mysql',  # MySQL or Mariadb
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                # 'host': '64.176.81.31',
                # 'port': '3456',
                'user': 'root',
                'password': 'kylin123',
                'database': 'kzz',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                # 'echo': True
            }
        }
    },
    "apps": {
        "models": {
            "models": ["models.dp_model", "models.tj_model",
                       "models.gdzw_model", "models.hlf_model","models.gdhy_model", "models.inlineapp_model", ],
            "default_connection": "default",
        }
    },
    "use_tz": False,  # 建议不要开启，不然存储日期时会有很多坑，时区转换在项目中手动处理更稳妥。
    "timezone": "Asia/Shanghai"
}

LOGGER_DIR = os.environ.get('LOG_DIR', r'./logs')
if not LOGGER_DIR:
    raise Exception('请先设置日志目录环境变量: LOG_DIR')
elif not Path(LOGGER_DIR).exists():
    raise Exception('日志目录不存在')
else:
    LOGGER_DIR = Path(LOGGER_DIR)
