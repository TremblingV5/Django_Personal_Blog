from hashlib import md5

def get_md5(*args):
    info = "".join(args)
    return md5(info.encode('utf-8')).hexdigest()
