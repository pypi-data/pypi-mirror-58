default_set = set


def set(seq=()):
    """
    Sobrescreve função set para aceitar dicionários
    :param seq: Lista de dicionários
    :return: Lista de dicionários únicos
    """
    import json
    if type(seq) is list and type(seq[0]) is dict:
        jsons = [json.dumps(d, sort_keys=True) for d in seq]
        jsons_set = list(set(jsons))
        res = [json.loads(j) for j in jsons_set]
        return res
    else:
        return default_set(seq)


def path(full_path, dic):
    """
    Get value from dic following a path
    :param full_path:
    :param dic:
    :return:
    """
    if '.' in full_path:
        data = dic
        nodes = full_path.split('.')
        data_list = []
        for node in nodes:
            if node in data:
                data = data[node]
            else:
                return None

            if isinstance(data, list):
                for d in data:
                    data_list += [path(full_path.split(node)[1][1:], d)]
                break
        if len(data_list):
            return data_list
        return data

    else:
        if full_path in dic:
            return dic[full_path]
        else:
            return None


def unpack(dic):
    """
    Unpack while obj isn't a obj
    """

    if isinstance(dic, list):
        if len(dic) == 1:
            return dic[0]
        else:
            new = []
            for i in dic:
                new += [unpack(i)]
            return new
    return dic


def flat(dic):
    ret = []

    # Se é um único item
    if isinstance(dic, dict):
        return dic

    for i in dic:
        if isinstance(i, list):
            ret += i
        else:
            ret += [i]
    return ret


def flatten(d):
    out = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten(subdict).items()
                out.update({key + '.' + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out
