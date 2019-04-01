def get_formated_name(first, middle, last=''):
    if last:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + middle
    return full_name


