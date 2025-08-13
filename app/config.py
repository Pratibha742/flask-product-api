import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")
    API_KEY = os.getenv("API_KEY", "defaultkey")