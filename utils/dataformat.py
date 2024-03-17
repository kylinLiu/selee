def formlist_to_dict(formlist):
    _dict = {}
    for row in formlist:
        _dict.setdefault(row[0], [])
        _dict[row[0]].append(row[1])
    for k, v in _dict.items():
        if len(v) == 1:
            _dict[k] = v[0]
    return _dict
