def remove_duplicates(lista):
    """
    Remove duplicados de uma lista
    :param lista:
    :return:
    """
    return list(set(lista))


def flat(l):
    """
    Aplaina uma lista de lista
        ex: [[1,2,3],[4,5,6],[7,8,9]] = [1,2,3,4,5,6,7,8,9]
    :param l: lista de lista
    :return: lista
    """
    return [item for sublist in l for item in sublist]


def overlap(l1, l2):
    """
    Checa se algum item de uma lista ocorre em outra lista
    :param l1: Lista1
    :param l2: Lista2
    :return:
    """
    return any([i == j for j in l2 for i in l1])
