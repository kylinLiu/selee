import logging.config

from common.loguru_conf import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

for log_name in logging.root.manager.loggerDict.keys():
    if log_name not in LOGGING_CONFIG['loggers']:
        LOGGING_CONFIG['loggers'][log_name] = {"handlers": ["root", 'json_root'], "level": "WARNING", "propagate": False}




access_logger = logging.getLogger("access")
root_logger = logging.getLogger('root')
debugger = logging.getLogger("debugger")
mysql_logger = logging.getLogger('mysql_timeout')
http_logger = logging.getLogger('http')
