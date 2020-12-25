import codecs


def clear_string(line):
    line = line.replace("", "")
    return codecs.decode(codecs.encode(
        line, 'latin-1', 'backslashreplace'), 'unicode-escape')


def resize_sides(width, height, max_size=99):
    if width > height:
        resized_width = max_size
        resized_height = int(
            round((max_size / float(width)) * height))
    else:
        resized_height = max_size
        resized_width = int(
            round((max_size / float(height)) * width))
    return resized_width, resized_height