from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

password = "Timoh@2023"

hashed = pwd_context.hash(password)
print(hashed)

# from connect import connect
# from config import load_config

# connector = connect(load_config())

# print(connector)