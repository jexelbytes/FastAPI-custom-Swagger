from dotenv import load_dotenv
import os
load_dotenv()

host = os.getenv("HOST")
port = int(os.getenv("PORT"))
api_key = os.getenv("API_KEY")


is_develop = (str(os.getenv("IS_DEVELOP")).lower() in ('true', '1'))

summary = """This is a very custom OpenAPI schema"""

description = """
### Here's a longer description of the custom **OpenAPI** schema
"""

swagger_config = {
    "syntaxHighlight.theme": "nord",
    "persistAuthorization": True,
    "tryItOutEnabled":True,
    "docExpansion": "none",
    "displayRequestDuration":True,
    "filter":True,
}