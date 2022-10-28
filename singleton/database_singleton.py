from typing import Any
import sqlite3

class SingletonMeta(type):
  _instance = {}

  def __call__(cls, *args: Any, **kwds: Any) -> Any:
    if cls not in cls._instance:
      instance =  super().__call__(*args, **kwds)
      cls._instance[cls] = instance
    return cls._instance[cls]


class BaseDatabase(metaclass=SingletonMeta):
  connection = None
  
  def connect(self):
    if self.connection is None:
      self.connection = sqlite3.connect("db.clicksign")
      self.cursor = self.connection.cursor()
    return self.cursor


class SQLiteDatabase(BaseDatabase):
    ...


class PostgressFakeDatabase(BaseDatabase):
    ...


db1 = SQLiteDatabase().connect()
print(id(db1))
db2 = SQLiteDatabase().connect()
print(id(db2))

print("-" * 15)

db3 = PostgressFakeDatabase().connect()
print(id(db3))
db4 = PostgressFakeDatabase().connect()
print(id(db4))