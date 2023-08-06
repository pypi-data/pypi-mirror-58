def dumps(dics):
    def default(o):
        import datetime
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()

    import json
    return json.dumps(
        dics,
        sort_keys=True,
        indent=2,
        default=default,
    )
