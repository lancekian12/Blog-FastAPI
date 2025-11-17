from pwdlib import PasswordHash


class Hash():
    password_hash = PasswordHash.recommended()

    @staticmethod
    def bcrypt_password(password: str):
        return Hash.password_hash.hash(password)
