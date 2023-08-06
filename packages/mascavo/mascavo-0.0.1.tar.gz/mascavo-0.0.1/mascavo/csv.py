"""
    This file deal with csv operations
"""


def read(filename: str):
    """
    Read CSV and make a dictionary list
    :param filename: csv
    :return: dictionary list
    """
    import csv
    return list(csv.DictReader(open(filename)))


def write(dics: list, filename: str, keys=None):
    """
    Create a CSV from a dictionary list
    :param dics: dictionary list
    :param filename: output filename
    :param keys: Optional, subset of keys. Default is all keys.
    :return: None
    """
    if not keys:
        keys = sorted(set().union(*(d.keys() for d in dics)))

    import csv
    with open(filename, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dics)
