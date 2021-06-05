"""to get env vars """
import os

def isEnvEquals(env_name:str, value:str):
    return value == os.environ.get(env_name)

def getEnv(env_name:str):
    return os.environ.get(env_name)
