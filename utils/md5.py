
import hashlib
def md5_16bit(input_str):
    md5_hash = hashlib.md5(input_str.encode())
    return md5_hash.hexdigest()

