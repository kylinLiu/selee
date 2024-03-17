from common.settings import LOGGER_DIR

LOGGING_CONFIG: dict = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "()": "logging.Formatter",
            "fmt": '%(asctime)s %(name)s %(levelname)s %(filename)s:%(lineno)d pid-%(process)d-%(thread)d:  %(message)s',
        },
        "json_default": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": "%(asctime) %(created) %(levelname) %(filename) %(lineno) %(module) %(message) %(name) %(pathname) %(process) %(processName) %(thread) %(threadName)",
        },
        "access": {
            "()": "logging.Formatter",
            "fmt": '%(asctime)s %(name)s %(levelname)s %(filename)s:%(lineno)d pid-%(process)d-%(thread)d:  %(message)s',
        },
        "json_access": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": '%(asctime) %(created) %(levelname) %(name) %(process) %(thread) %(method) %(remote) %(url) %(status_code) %(request_time)',
        },
        "jump_able_fmt":{
            "()": "logging.Formatter",
            "fmt": '%(asctime)s - %(name)s - "%(pathname)s:%(lineno)d" - %(funcName)s - %(levelname)s - %(message)s',
        }
    },
    "handlers": {
        "root": {
            "formatter": "default",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGER_DIR / 'root.log',
            "maxBytes": 1024 * 1024 * 1024,
            "backupCount": 3
        },
        "json_root": {
            "formatter": "json_default",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGER_DIR / 'json_root.log',
            "maxBytes": 1024 * 1024 * 1024,
            "backupCount": 3
        },
        "access": {
            "formatter": "access",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGER_DIR / 'access.log',
            "maxBytes": 1024 * 1024 * 1024,
            "backupCount": 3
        },
        "json_access": {
            "formatter": "json_access",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGER_DIR / 'json_access.log',
            "maxBytes": 1024 * 1024 * 1024,
            "backupCount": 3
        },
        "stream_handler":{
            "formatter": "jump_able_fmt",
            "class": "logging.StreamHandler",
        },
        'mysql_timeout': {
            "formatter": "default",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGER_DIR / 'mysql_timeout.log',
            "maxBytes": 1024 * 1024 * 1024,
            "backupCount": 3
        },
        'http': {
            "formatter": "default",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGER_DIR / 'http.log',
            "maxBytes": 1024 * 1024 * 1024,
            "backupCount": 3
        },
    },
    "loggers": {
        "tortoise": {"handlers": ["root", 'json_root',"stream_handler"], "level": "ERROR", "propagate": False},
        "tortoise.db_client": {"handlers": ["root", 'json_root','stream_handler'], "level": "ERROR", "propagate": False},
        "root": {"handlers": ["root", 'json_root',"stream_handler"], "level": "DEBUG", "propagate": False},
        "uvicorn.error": {"handlers": ["root", 'json_root',"stream_handler"], "level": "INFO", "propagate": False},
        "uvicorn": {"handlers": ["root", 'json_root'], "level": "INFO", "propagate": False},
        "access": {"handlers": ["access", 'json_access'], "level": "INFO", "propagate": False},
        "debugger": {"handlers": ["stream_handler"], "level": "DEBUG", "propagate": False},  # 生产使用ERROR级别
        "mysql_timeout": {"handlers": ["mysql_timeout"], "level": "DEBUG", "propagate": False},
        "http": {"handlers": ["http", 'stream_handler'], "level": "INFO", "propagate": False},
    },
}
