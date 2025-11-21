from pwdlib import PasswordHash

class Hash:
    password_hash = PasswordHash.recommended()  # uses Argon2

    @staticmethod
    def hash_password(password: str):
        return Hash.password_hash.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return Hash.password_hash.verify(plain_password, hashed_password)
