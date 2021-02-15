import os
import mocks_stubs_fakes.importme

class FakeDBAdapter():
    def __init__(self, conn_str):
        self.conn_str = conn_str


class Connector:
    db_connector = None

    def __init__(self, conncetion_string):
        self.connection_string = conncetion_string
        if not Connector.db_connector:
            Connector.db_connector = FakeDBAdapter(conncetion_string)

    def read_from_database(self, query):
        self.db_connector.open()
        try:
            result = self.db_connector.read(query)
        finally:
            self.db_connector.close()

    def write_to_database(self, query):
        self.db_connector.open()
        try:
            self.db_connector.write(query)
        finally:
            self.db_connector.close()

    def do_something(self, arg):
        if arg:
            self.do_first()
            return
        self.do_second()

    def get_config_from_env(self):
        self.connection_string = os.environ.get('CONNECTION_STRING')


