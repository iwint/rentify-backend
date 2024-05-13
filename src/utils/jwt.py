import os
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta


class AuthHandler:
    secret = os.getenv('SECRET_KEY')
    expire_time_duration_min = 1440
    algorithm = os.getenv('ALGORITHM')
    security = HTTPBearer()

    def endcode_token(self, email):
        payload = {
            "exp": datetime.utcnow() + timedelta(minutes=self.expire_time_duration_min),
            "iat": datetime.utcnow(),
            "sub": email
        }
        return jwt.encode(payload, self.secret, self.algorithm)

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=self.algorithm)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')
        except Exception as e:
            return e

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)
