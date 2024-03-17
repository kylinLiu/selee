import datetime


def last_15_days():
    today = datetime.date.today()
    # saturday_weekday = 5
    # sunday_weekday = 6
    today_weekday = today.weekday()
    # saturday = today + datetime.timedelta(days=saturday_weekday - today_weekday)
    # sunday = today + datetime.timedelta(days=sunday_weekday - today_weekday)
    date_list = [today + datetime.timedelta(days=_) for _ in range(0, 30)]
    # 历史日期不需要展示，不可约
    gzr = []
    zm = []
    for row in date_list:
        if row.weekday() in [5, 6]:
            zm.append(row.strftime("%Y-%m-%d"))
        else:
            gzr.append(row.strftime("%Y-%m-%d"))
    return zm, gzr
    # return saturday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")


zm, gzr = last_15_days()
print(zm)
print(gzr)
