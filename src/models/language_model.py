from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict):
        # raise NotImplementedError
        self.data = data

    # Req. 2
    def to_dict(self):
        # raise NotImplementedError
        languages_object = {
            "name": self.data['name'],
            "acronym": self.data['acronym'],
        }
        return languages_object

    # Req. 3
    @classmethod
    def list_dicts(cls):
        raise NotImplementedError
