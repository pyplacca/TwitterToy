import sqlite3 as sql

default_database = 'database/ddoi.db'


class DatabaseManager:
    def __init__(self, database: str):
        self.connection = self.cursor = self.table = None
        self.create_connection(database)

    def use_table(self, name: str, **table_structure: object) -> None:
        # check existence of selected table
        if not self._table_exists(name):
            # create table in current database if it doesn't exist
            self._create_table(name, **table_structure)
        self.table = name

    def _apply(self) -> None:
        self.connection.commit()

    def _table_exists(self, name: str) -> bool:
        try:
            self.cursor.execute("SELECT * FROM {}".format(name))
            return True
        except sql.OperationalError:
            return False

    def _create_table(self, name: str, **structure: object) -> None:
        # convert structure object to sql query string
        structure_string = self._join(map(lambda item: ' '.join(item), structure.items()))
        self.cursor.execute('CREATE TABLE {table_name} ({table_structure})'.format(
            table_name=name,
            table_structure=structure_string
        ))
        self._apply()

    @staticmethod
    def _join(args, delimiter: str = ', ') -> str:
        return delimiter.join(args)

    def disconnect(self):
        self.connection.close()

    def get(self, **query: object) -> dict:
        # convert query object to sql query string
        conditions = self._join([f'{k}={repr(v)}' for k, v in query.items()])
        self.cursor.execute("SELECT * FROM {table} WHERE {conditions}".format(
            table=self.table,
            conditions=conditions
        ))
        result = self.cursor.fetchone()
        if result:
            return dict(zip(result.keys(), list(result)))
        return {}

    def insert(self, **query: object) -> None:
        self.cursor.execute("INSERT INTO {table} ({columns}) VALUES ({values})".format(
            table=self.table,
            columns=self._join(query.keys()),
            values=self._join(map(repr, query.values())),
        ))
        self._apply()

    def delete(self, query=None):
        pass

    def revert(self) -> None:
        self.connection.rollback()

    def create_connection(self, database: str) -> None:
        self.connection = sql.Connection(database)
        self.connection.row_factory = sql.Row
        self.cursor = self.connection.cursor()
