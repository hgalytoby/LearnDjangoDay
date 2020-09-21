import random


def get_verify_code():
    result = str()
    data = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(random.randint(4, 6)):
        result += random.choice(data)
    return result


def get_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
