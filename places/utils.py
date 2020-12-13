import codecs


def clear_string(some_string):
    return codecs.decode(codecs.encode(
        some_string, 'latin-1', 'backslashreplace'), 'unicode-escape')
