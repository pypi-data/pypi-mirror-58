def digitos(txt):
    """
    Função digitos('asdf123123') = '123123'
    :param txt: Texto inicial
    :return: Saída somente com dígitos
    """
    return ''.join([c for c in txt if c.isdigit()])


def normalize_unicode(data):
    import unicodedata
    return str(unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore').decode('ascii'))
