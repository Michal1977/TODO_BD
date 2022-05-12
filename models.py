import json
import sqlite3
from sqlite3 import Error


class Todos:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def get(self, table, conditions):
        values = conditions.values()
        return self.cursor.execute(
            f"SELECT * FROM {table} WHERE {'and'.join([f'{condition}=?' for condition in conditions])}", list(values)
        )

    def add_to_table(self, table, columns):
        self.cursor.execute(f"INSERT INTO {table}({','.join([column_name for column_name in columns])}) VALUES({','.join(['?' for _ in columns])})", list(columns.values()))
        self.conn.commit()

    def update(self, table, id, **kwargs):

        parameters = [f"{k} = ?" for k in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(v for v in kwargs.values())
        values += (id,)

        sql = f''' UPDATE {table}
                 SET {parameters}
                 WHERE id = ?'''
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("OK")
        except sqlite3.OperationalError as e:
            print(e)
