import hashlib


def generate_md5_code(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


print(generate_md5_code("zsvifdwe23121)d&##!@"))