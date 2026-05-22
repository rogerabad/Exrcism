def score(x, y):
    distance = (x**2 + y**2) ** 0.5
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0
    

    """ 
    if -1 <= x <= 1 and -1 <= y <= 1:
        return 10
    if -5 <= x <= 5 and -5 <= y <= 5:
        return 5
    if -10 <= x <= 10 and -10 <= y <= 10:
        return 1
    return 0 
    """


