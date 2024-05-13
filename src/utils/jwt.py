import os
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from icecream import ic


class AuthHandler:
    secret = os.getenv('SECRET_KEY')
    expire_time_duration_min = 1440
    algorithm = os.getenv('ALGORITHM')
    security = HTTPBearer()

    def encode_token(self, email):
        payload = {
            "exp": datetime.utcnow() + timedelta(minutes=self.expire_time_duration_min),
            "iat": datetime.utcnow(),
            "sub": email
        }
        return jwt.encode(payload, self.secret, self.algorithm)

    def decode_token(self, token):
        ic(token)

        try:
            payload = jwt.decode(token, self.secret, algorithms=self.algorithm)
            ic(payload)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')
        except Exception as e:
            return e

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        ic(auth)
        return self.decode_token(auth.credentials)
