from db.load_env import dev_key
from fastapi import HTTPException
from routes.debug import Hkey

def get_dev_key(dev_key_header:str):

    if Hkey(str(dev_key_header)) != dev_key:
        raise HTTPException(
            status_code=401, detail="Unauthorized"
        )