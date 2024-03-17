import datetime
import time

unit_map = (
    ('y', 365 * 24 * 3600 * 1000),
    ('m', 30 * 24 * 3600 * 1000),
    ('w', 7 * 24 * 3600 * 1000),
    ('d', 24 * 3600 * 1000),
    ('h', 3600 * 1000),
    ('i', 60 * 1000),
    ('s', 1000),
)

DEFAULT_WINDOW = {
    60000: '近1分钟',
    300000: '近5分钟',
    600000: '近10分钟',
    1800000: '近30分钟',
    3600000: '近1小时',
    43200000: '近12小时',
    86400000: '近24小时',
    172800000: '近48小时',
    259200000: '近72小时',
    604800000: '近7天',
    1296000000: '近15天',
    2592000000: '近30天',
    5184000000: '近60天',
    7776000000: '近90天',
    10368000000: '近120天',
    15552000000: '近180天',
    31536000000: '近1年(365)',
    63072000000: '近两年(2*365)'
}

MILLSECOND_ONE_HOUR = 3600000


def timestamp():
    return int(time.time() * 1000)


def millisecond2str(num: int):
    for unit, millisecond in unit_map:
        d, remain = divmod(num, millisecond)
        if d != 0 and remain == 0:
            return '{}{}'.format(d, unit)
    return str(num)


def getTimeOffsetByCountryId(country_id):
    if int(country_id) in [1, 4]:
        return 7
    elif int(country_id) in [2, 3]:
        return 8
    elif int(country_id) in [6, 7, 8, 9, 10, 26]:
        return 1
    else:
        return None


def timestamp_to_utc_datetime(timestamp):
    utc_dt_time = datetime.datetime.utcfromtimestamp(timestamp / 1000.0)
    return utc_dt_time


def timestamp_to_datetime(timestamp, country_id):
    return timestamp_to_utc_datetime(timestamp + getTimeOffsetByCountryId(country_id) * MILLSECOND_ONE_HOUR)


def get_current_timestamp():
    return int(time.time() * 1000)


# 获取指定counrtry_id对应时区的datetime
def get_current_date_time(country_id):
    return timestamp_to_datetime(get_current_timestamp(), country_id)


def get_current_date_str(country_id):
    return str(get_current_date_time(country_id))[0:10]


def datetime_timestamp_to_date_timestamp(_timestamp):
    return int(_timestamp / 1000.0) * 1000


def get_current_day_str():
    return datetime.date.today().strftime("%Y-%m-%d")


def get_current_week_days():
    today = datetime.date.today()
    today_weekday = today.weekday()
    # saturday = today + datetime.timedelta(days=saturday_weekday - today_weekday)
    # sunday = today + datetime.timedelta(days=sunday_weekday - today_weekday)
    date_list = [today + datetime.timedelta(days=_ - today_weekday) for _ in range(20)]
    # 历史日期不需要展示，不可约
    # date_list = [_.strftime("%Y-%m-%d") for _ in date_list if _ >= today]
    date_list = {
        _.strftime("%#m-%#d"): _.strftime("%Y-%m-%d")
        for _ in date_list
    }
    return date_list


def get_current_weekend():
    today = datetime.date.today()
    saturday_weekday = 5
    sunday_weekday = 6
    today_weekday = today.weekday()
    saturday = today + datetime.timedelta(days=saturday_weekday - today_weekday)
    sunday = today + datetime.timedelta(days=sunday_weekday - today_weekday)
    date_list = [saturday, sunday]
    # 历史日期不需要展示，不可约
    date_list = [_.strftime("%Y-%m-%d") for _ in date_list if _ >= today]
    return date_list
    # return saturday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")


def get_current_weeks():
    today = datetime.date.today()
    # saturday_weekday = 5
    # sunday_weekday = 6
    today_weekday = today.weekday()
    # saturday = today + datetime.timedelta(days=saturday_weekday - today_weekday)
    # sunday = today + datetime.timedelta(days=sunday_weekday - today_weekday)
    date_list = [today + datetime.timedelta(days=_ - today_weekday) for _ in range(0, 30)]
    # 历史日期不需要展示，不可约
    date_list = [_.strftime("%Y-%m-%d") for _ in date_list if _ >= today]
    return date_list
    # return saturday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")


def get_time_str(ms):
    timeArray = time.localtime(int(ms / 1000))
    return time.strftime("%Y--%m--%d %H:%M:%S", timeArray)


if __name__ == '__main__':
    millisecond2str(1296000000)
