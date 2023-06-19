from singleton import Singleton
from peewee import InternalError, MySQLDatabase, PostgresqlDatabase, SqliteDatabase
from checklogger import CheckLogger
from tests.config.database import DatabaseConfig


class CheckDatabase(metaclass=Singleton):
    _databases = {"MY_SQL": MySQLDatabase,
                  "POSTGRES": PostgresqlDatabase,
                  "SQL_LITE": SqliteDatabase
                  }

    def __init__(self):
        self.database = self._databases[DatabaseConfig.DATABASE_TYPE](host=DatabaseConfig.HOST,
                                                                      user=DatabaseConfig.USER,
                                                                      password=DatabaseConfig.PASSWORD,
                                                                      database=DatabaseConfig.DATABASE)
        CheckLogger.info(f"Connect to database {DatabaseConfig.DATABASE_TYPE} with credentials host={DatabaseConfig.HOST}, "
                    f"user = {DatabaseConfig.USER}, password = {DatabaseConfig.PASSWORD},"
                    f" database = {DatabaseConfig.DATABASE}")
        try:
            self._connection = self.database.connection()
        except InternalError:
            CheckLogger.warning("Access denied, wrong credentials")

        CheckLogger.info(f"Create cursor for database")
        self._cursor = self._connection.cursor()

    def get_cursor(self):
        return self._cursor

    def execute(self, data):
        self.get_cursor().execute(data)
        self._connection.commit()

    def fetchall(self):
        return self.get_cursor().fetchall()

    def __del__(self):
        CheckLogger.info(f"Stop {self._connection} session")
        self._connection.close()
