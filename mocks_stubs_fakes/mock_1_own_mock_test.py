from mocks_stubs_fakes.db_writer import Connector
from mocks_stubs_fakes.own_mock import OwnMock
from pytest import fixture


@fixture
def connector():
    conn = Connector('Valid connection string must be passed')
    conn.db_connector = OwnMock()
    return conn


def test_database_writer(connector):
    example_query = 'SELECT * FORM USERS WHERE ID=10'
    connector.write_to_database(example_query)
    assert connector.db_connector.open.call_count == 1
    assert connector.db_connector.close.call_count == 1
    assert connector.db_connector.write.call_count == 1
    assert example_query in connector.db_connector.write.call_args_kwargs[0][0]