from abc import ABC, abstractmethod
from configparser import ConfigParser

import pyodbc
from multipledispatch import dispatch
from pyodbc import Connection, Row


class DataSource(ABC):
    """
    Abstract base class for the Data Source implementations.
    DataSource classes are responsible for holding information relating
    to the odbc connection.

    Vendor implementations should parse the data_sources.ini file to
    configure the connection based off the defined configurable values.

    Vendors are free to customize the parameters required as the DataSource
    implementation is passed the config section.
    """

    def _load_datasources_config(self, datasource_name):
        data_sources = ConfigParser()
        data_sources.read('data_sources.ini')
        self._set_fields(data_sources[datasource_name])

    def _set_fields(self, config):
        for field in self.__dict__.keys():
            try:
                setattr(self, field, config[field])
            except KeyError:
                pass

    def _validate_fields(self):
        for field in self.__dict__.keys():
            if getattr(self, field) is None:
                raise SQLException(f'{field} is not defined')

    @abstractmethod
    def get_connection(self) -> Connection:
        """
        Abstract method to be implemented by the Vendor specific DataSource implementation.

        It should build a DSN string from the configured parameters and setup the connection.
        """
        raise NotImplementedError()


class MySqlDataSource(DataSource):
    """
    MySQL DataSource implementation. Creates a MySQL DataSource connection from the provided config section.

    Available DataSource parameters are:

    - driver
    - server
    - port
    - database
    - user
    - password

    """

    def __init__(self, datasource_name):
        self.driver: str = None
        self.server: str = None
        self.port: str = None
        self.database: str = None
        self.user: str = None
        self.password: str = None
        self._load_datasources_config(datasource_name)

    def get_connection(self):
        self._validate_fields()
        cnxn = pyodbc.connect(
            f'DRIVER={self.driver};'
            f'SERVER={self.server};'
            f'PORT={self.port};'
            f'DATABASE={self.database};'
            f'USER={self.user};'
            f'PASSWORD={self.password};'
            f'charset=utf8mb3;'
        )
        cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        cnxn.setencoding(encoding='utf-8')
        return cnxn


class RowMapper(ABC):

    @abstractmethod
    def map_row(self, results_set: Row):
        raise NotImplementedError()


class PdbcOperations:
    def __init__(self, data_source: DataSource):
        self.data_source: DataSource = data_source

    @dispatch(str, RowMapper)
    def query(self, statement, row_mapper: RowMapper):
        connection = self.data_source.get_connection()
        cursor = connection.cursor()
        cursor.execute(statement)
        return [row_mapper.map_row(row) for row in cursor.fetchall()]

    @dispatch(str, tuple, RowMapper)
    def query(self, statement, parameters, row_mapper: RowMapper):
        connection = self.data_source.get_connection()
        cursor = connection.cursor()
        cursor.execute(statement, parameters)
        return [row_mapper.map_row(row) for row in cursor.fetchall()]


class SQLException(Exception):
    pass
