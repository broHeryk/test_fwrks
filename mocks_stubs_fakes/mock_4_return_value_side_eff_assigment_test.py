from unittest import mock
from mocks_stubs_fakes.db_writer import Connector
import pytest


@mock.patch('mocks_stubs_fakes.db_writer.Connector.db_connector', return_value=300)
def test_return_value_return_as_dec(db_conn_mock):
    c = Connector('Test')
    assert c.db_connector() == 300


def test_return_value_without_decorator():
    db_conn = mock.Mock(return_value=300)
    # The same effect as
    db_conn.return_value = 300
    c = Connector('Test')
    c.db_connector = db_conn
    assert c.db_connector() == 300


@mock.patch('mocks_stubs_fakes.db_writer.Connector.db_connector')
def test_side_effect_options_exc(db_conn_mock):
    db_conn_mock.side_effect = ValueError
    c = Connector('Test')
    with pytest.raises(ValueError):
        c.db_connector()

@mock.patch('mocks_stubs_fakes.db_writer.Connector.db_connector', side_effect=ValueError)
def test_side_effect_options_exc_1(db_conn_mock):
    c = Connector('Test')
    with pytest.raises(ValueError):
        c.db_connector()


@mock.patch('mocks_stubs_fakes.db_writer.Connector.db_connector', side_effect=[ValueError, ZeroDivisionError])
def test_side_effect_options_exc_sequence(_):
    c = Connector('Test')
    with pytest.raises(ValueError):
        c.db_connector()
    with pytest.raises(ZeroDivisionError):
        c.db_connector()


@mock.patch('mocks_stubs_fakes.db_writer.Connector.db_connector', side_effect=[10, 11])
def test_side_effect_options_exc_values_seq(_):
    c = Connector('Test')
    assert c.db_connector() == 10
    assert c.db_connector() == 11
    with pytest.raises(StopIteration) as exc:
        c.db_connector()
        print(exc)


@mock.patch('mocks_stubs_fakes.db_writer.Connector.db_connector', mock.PropertyMock(return_value=300))
def test_return_value_prop_mock():
    c = Connector('Test')
    assert c.db_connector == 300


@mock.patch('mocks_stubs_fakes.db_writer.Connector.db_connector', lambda x: 300)
def test_pass_lambda_as_callable():
    c = Connector('Test')
    assert c.db_connector() == 300


def obj_constructor(*args, **kwargs):
    return kwargs['value']


@mock.patch('mocks_stubs_fakes.db_writer.Connector.db_connector', obj_constructor)
def test_pass_function_as_callable():
    c = Connector('Test')
    assert c.db_connector(value=300) == 300

