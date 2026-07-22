from cryptography.fernet import Fernet

# FERNET_KEY = Fernet.generate_key().decode()
# print("Generated Key:", FERNET_KEY)
FERNET_KEY="EGHVxn86Z3bvA6IHLSz0r4NhOQJ-v2nyAQQEY8jPo_A="
cipher=Fernet(FERNET_KEY.encode())
encrypted=cipher.encrypt("1234 5678 9012".encode()).decode()
print("original:","1234 5678 9012")
print("Encrypted:",encrypted)
decrypt=cipher.decrypt("gAAAAABqXyGwrcpMoPmYAvaWCBYqP2SH7YoMKbslpk4d4R7xyeBoxQIqgrvNTQNU_XH7tEeUNuI5pJiFpbr0UQLynNmRCO_pbw==")
print("Decrypt:",decrypt)