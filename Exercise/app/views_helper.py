import hashlib


def hash_password(password):
    return hashlib.new('sha512', password.encode('utf-8')).hexdigest()
