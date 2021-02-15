from unittest.mock import patch, call
from mocks_stubs_fakes.db_writer import Connector


@patch('mocks_stubs_fakes.db_writer.Connector.db_connector')
def test_database_writer(db_connector):
    conn = Connector('asdf')
    example_query = 'SELECT * FORM USERS WHERE ID=10'
    conn.write_to_database(example_query)
    second_example_query = 'SELECT id FROM USERS WHERE age>20'
    conn.write_to_database(second_example_query)
    assert db_connector.open.call_count == 2
    assert db_connector.close.call_count == 2
    # db_connector.write.assert_called_once_with(example_query)
    db_connector.write.assert_called_with(second_example_query)
    expected_call = call(example_query)
    another_expected_call = call(second_example_query)
    db_connector.write.assert_has_calls([expected_call], any_order=True)
    db_connector.write.assert_has_calls([expected_call, another_expected_call])
    # db_connector.write.assert_has_calls(reversed([expected_call, another_expected_call]) )
    db_connector.write.assert_any_call(example_query)
    db_connector.write.assert_called()
    assert db_connector.write.called
