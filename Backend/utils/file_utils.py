import hashlib

def generate_hash_code(file_byte: bytes) -> str:

    return hashlib.sha256(file_byte).hexdigest()