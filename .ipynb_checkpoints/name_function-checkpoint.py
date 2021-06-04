def get_format_name(first,last,middle = ""):
    if middle:
        format_name = first + " " + middle + " " + last
    else:
        format_name = first + " " + last
    return format_name.title()