def check_state(value):
    if value >= 100:
        return 'Gas'
    elif 100 > value >= 0:
        return 'Liquid'
    else:
        return 'Solid'
