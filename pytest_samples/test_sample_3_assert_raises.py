import pytest
from logic_functions import get_json_data_from_file
import pytest
import json


@pytest.fixture(scope="session")
def json_file(tmpdir_factory):
    json_data = json.dumps({'hello': 'mate'})
    fn = tmpdir_factory.mktemp("data").join("data.json")
    with open(fn, 'w+') as f:
        f.write(json_data)

    return fn


def test_get_json_data_with_incorrect_path(json_file):
    not_existing_path = 'asfd'
    with pytest.raises(FileNotFoundError) as ex:
        get_json_data_from_file(json_file)
    print(ex)


def test_get_json_data_with_correct_path(json_file):
    data = get_json_data_from_file(json_file)
    print(data)
    assert data == {'hello': 'mate'}


