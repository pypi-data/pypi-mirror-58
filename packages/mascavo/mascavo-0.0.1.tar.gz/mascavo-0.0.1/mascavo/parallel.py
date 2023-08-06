def tmap(func, args, workers=16):
    """
    Redefinição da função map, multithread, aguarda threads no final e retorna resultado expandido em lista.
    :param func: função
    :param args: lista
    :param workers: número de threads máximo
    :return: resultado do mapeamento de fn em l expandido em lista
    """

    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
        ex.shutdown(wait=True)

    return list(res)


def pmap(func, args, workers=None):
    """
    Redefinição da função map, multiprocessos, aguarda processos no final e retorna resultado expandido em lista.
    :param func: função
    :param args: lista
    :param workers: número de processos máximo
    :return: resultado do mapeamento de fn em l expandido em lista
    """

    import multiprocessing
    if not workers:
        workers = multiprocessing.cpu_count()

    if workers == 1:
        return list(map(func, args))

    import concurrent.futures
    with concurrent.futures.ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)
        ex.shutdown(wait=True)
    return list(res)
