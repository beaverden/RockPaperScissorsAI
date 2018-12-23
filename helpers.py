def evaluate(first, second):
    r = {
        'rs': 1,
        'rp': 2,
        'rr': 0,
        'ps': 2,
        'pr': 1,
        'pp': 0,
        'sr': 2,
        'sp': 1,
        'ss': 0
    }
    return r[first + second]


def opposite(move):
    op = {
        'r': 'p',
        'p': 's',
        's': 'r'
    }
    return op[move]