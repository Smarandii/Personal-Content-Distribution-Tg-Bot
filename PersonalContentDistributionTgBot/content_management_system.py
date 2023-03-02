from sqlite3 import connect
from init_db import db_name, table_name
from aiogram import types as aiogram_types


class DataBaseInterface:

    def __init__(self):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = connect(database=self.db_name)

    def add_row(self, row: tuple):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                f"""INSERT INTO {self.table_name} 
                VALUES ('{row[0]}', '{row[1]}');"""
            )
            self.connection.commit()
            return True
        except Exception as e:
            return False

    def get_row_where(self, trigger_word=None, file_id=None) -> tuple:
        sql = ""
        if trigger_word is not None:
            sql = f"SELECT * FROM {self.table_name} WHERE trigger_word='{trigger_word}'"
        if file_id is not None:
            sql = f"SELECT * FROM {self.table_name} WHERE file_id='{file_id}'"
        cursor = self.connection.cursor()
        cursor.execute(
            sql
        )
        return cursor.fetchone()


class ContentManagementSystem:

    def __init__(self):
        self._db = DataBaseInterface()

    def trigger_word_exists(self, trigger_word: str):
        return self._db.get_row_where(trigger_word=trigger_word.lower())

    def map_file_id_to_trigger_word(self, message: aiogram_types.Message):
        if message.caption is not None:
            result = self._db.add_row(
                (message.document.file_id, message.caption.lower())
            )
            return result
        else:
            return False

    def _get_file_id_and_description_from_trigger_word(self, trigger_word):
        return self._db.get_row_where(trigger_word=trigger_word)

    def get_file_id_mapped_to(self, trigger_word: str):
        return self._get_file_id_and_description_from_trigger_word(trigger_word.lower())
