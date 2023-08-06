def stringify(node):
    """
    Dado um nó HTML concatena todos os textos visíveis incluindo os nós filhos e retorna um único string
    :param node: Nó pai
    :return: String
    """
    from itertools import chain
    parts = ([node.text] + list(chain(*([c.text, c.tail] for c in node.getchildren()))) + [node.tail])
    parts = list(filter(None, parts))
    parts = [str(i).strip() for i in parts]
    parts = [i for i in parts if i]
    return ''.join(filter(None, parts))
