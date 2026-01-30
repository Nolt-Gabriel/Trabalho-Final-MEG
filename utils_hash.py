from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended() 

#Pega a senha e faz o hash dela
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

#Verificação de senha para o login
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

