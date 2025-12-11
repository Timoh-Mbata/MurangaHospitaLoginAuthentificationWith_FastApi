from pydantic import BaseModel, Field ,field_validator ,EmailStr
from fastapi import Depends , HTTPException ,status
from fastapi.security import  OAuth2PasswordBearer
from typing import Annotated
from datetime import datetime , timedelta
from jose import JWTError , jwt
from passlib.context import CryptContext
from dotenv import dotenv_values
from connect import connect
from config import load_config

env_values = dotenv_values(".env")
secret_key = env_values["SECRET_KEY"]
algorithm = env_values["ALGORITHM"]

ACCESS_TOKEN_EXPIRES_IN_MINUTES = env_values["ACCESS_TOKEN_EXPIRES_IN_MINUTES"]

connecting_db = connect(load_config())


class User(BaseModel):
    username : str
    useremail : EmailStr or None = None
    disable : bool or None = None

class LoginModel(BaseModel):
    username : str
    userpassword : str

class UserInDb (User):
    userpassword: str

class Token(BaseModel):
    accessToken : str
    TokenTpye : str

class TokenData(BaseModel):
    username : str or None = None


pwd_context = CryptContext(schemes=["argon2"],deprecated="auto")
outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password , hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_hashedPassword(password):
    return pwd_context.hash(password)

def get_user(username: str) -> UserInDb | None:
    try:
        with connecting_db.cursor() as cur:
            cur.execute("""
                SELECT username, useremail, userpassword, disable
                FROM users
                WHERE username = %s
                LIMIT 1
            """, (username,))
            row = cur.fetchone()
            if not row:
                return None
            return UserInDb(
                username=row[0],
                email=row[1],
                userpassword=row[2],  
                disabled=row[3]
            )
    except Exception as e:
        print("DB ERROR in get_user:", e)
        return None
    
    
def authenticate_user(username : str , password : str ) -> UserInDb | None :
    user = get_user(username=username)
    if not user : return False
    if not verify_password(password,user.userpassword) : return False   
    return user

def create_accessToken (data:dict ,expires_delta:timedelta or None = None):
    to_encode = data.copy()
    if expires_delta :
        expires = datetime.utcnow() + expires_delta
    else :
        expires = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp":expires})
    encoded_jwt = jwt.encode(to_encode,secret_key,algorithm=algorithm)
    return encoded_jwt

async def get_current_user(token:str = Depends(outh2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = get_user(username=token_data.username)
    if user is None:
        raise credential_exception

    return user

async def get_current_active_user(current_user: UserInDb = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")

    return current_user