from unittest.mock import patch
from mocks_stubs_fakes.db_writer import Connector
from pytest import fixture, raises
import os

# PATCH START STOP
#
# @fixture
# def connector():
#     patcher = patch('mocks_stubs_fakes.db_writer.Connector.db_connector')
#     patcher.start()
#     conn = Connector('Valid connection string must be passed')
#     yield conn
#     patcher.stop()
#
#
# def test_database_writer_start_stop(connector):
#     example_query = 'SELECT * FORM USERS WHERE ID=10'
#     connector.write_to_database(example_query)
#     assert connector.db_connector.open.call_count == 1
#     assert connector.db_connector.close.call_count == 1
#     connector.db_connector.write.assert_called_once_with(example_query)

# PATCH AS A DECORATOR

# @patch('mocks_stubs_fakes.db_writer.Connector.db_connector')
# def test_database_writer(db_connector):
#     conn = Connector('asdf')
#     example_query = 'SELECT * FORM USERS WHERE ID=10'
#     conn.write_to_database(example_query)
#     assert db_connector.open.call_count == 1
#     assert db_connector.close.call_count == 1
#     db_connector.write.assert_called_once_with(example_query)

# Patch as a context manager


@patch('mocks_stubs_fakes.db_writer.Connector.db_connector')
class TestContextManager:

    def test_read_from_db(self, db_connector):
        conn = Connector('asdf')
        example_query = 'SELECT * FORM USERS WHERE ID=10'
        conn.read_from_database(example_query)
        assert db_connector.open.call_count == 1
        assert db_connector.close.call_count == 1
        db_connector.read.assert_called_once_with(example_query)

    def test_read_from_db_connection_closed_when_exception_raised(self, _):
        conn = Connector('asdf')
        example_query = 'SELECT * FORM USERS WHERE ID=10'
        with patch('mocks_stubs_fakes.db_writer.Connector.db_connector') as db_connector:
            db_connector.read.side_effect = [ValueError]
            with raises(ValueError):
                conn.read_from_database(example_query)
        assert db_connector.open.call_count == 1
        assert db_connector.close.call_count == 1

# Patch variations
#
# @patch.object(Connector, 'db_connector')
# def test_database_writer_with_patched_obj(db_connector):
#     conn = Connector('asdf')
#     example_query = 'SELECT * FORM USERS WHERE ID=10'
#     conn.write_to_database(example_query)
#     assert db_connector.open.call_count == 1
#     assert db_connector.close.call_count == 1
#     db_connector.write.assert_called_once_with(example_query)

#

# @patch.dict('os.environ', {'CONNECTION_STRING': 'VALUE'})
# def test_get_something_from_env():
#     conn = Connector('')
#     conn.get_config_from_env()
#     assert conn.connection_string == 'VALUE'
#
#
# def test_get_something_from_env_without_patching():
#     conn = Connector('')
#     conn.get_config_from_env()
#     assert conn.connection_string == None


class CustomStingClass(str):
    pass


def test_patch_object_wraps():
    target_string = CustomStingClass('ASDF_a2e2r3')
    with patch.object(target_string, 'upper', wraps=target_string.upper) as str_spy:
        assert target_string.upper() == 'ASDF_A2E2R3'
        str_spy.call_count == 1
