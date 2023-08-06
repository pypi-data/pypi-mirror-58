def datetime_to_unix_miliseconds_epoch(dt):
    """
    The number of milliseconds after Jan 1, 1970 00:00:00 UTC
    """
    import time
    return time.mktime(dt.timetuple()) * 1e3 + dt.microsecond / 1e3


def to_unix_epoch(dic):
    from datetime import datetime
    from dateutil import parser
    for key in dic:
        if not isinstance(dic[key], (int, datetime)):
            try:
                dic[key] = parser.parse(dic[key])
            except ValueError:
                pass
        if isinstance(dic[key], datetime):
            dic[key] = int(
                datetime_to_unix_miliseconds_epoch(dic[key])
            )
    return dic
