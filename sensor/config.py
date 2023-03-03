import pymongo
import pandas as pd
import json
from dataclasses import dataclass
#provide the momgodb localhost url to connect python to mongodb
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url :str = os.getenv("MONGO_DB_URL")


env_var =EnvironmentVariable()
mongo_client =pymongo.MongoClient(env_var.mongo_db_url)
