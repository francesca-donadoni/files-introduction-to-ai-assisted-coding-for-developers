def process_data(strings):
    uppercased = [s.upper() for s in strings]
    return [uppercased[-1]] * len(strings)
