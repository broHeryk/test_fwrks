import datetime
import botocore.session
from botocore.stub import Stubber
from pytest import fixture, raises


s3 = botocore.session.get_session().create_client('s3')
stubber = Stubber(s3)

response = {
    'IsTruncated': False,
    'Name': 'test-bucket',
    'MaxKeys': 1000, 'Prefix': '',
    'Contents': [{
        'Key': 'test.txt',
        'ETag': '"abc123"',
        'StorageClass': 'STANDARD',
        'LastModified': datetime.datetime(2016, 1, 20, 22, 9),
        'Owner': {'ID': 'abc123', 'DisplayName': 'myname'},
        'Size': 14814
    }],
    'EncodingType': 'url',
    'ResponseMetadata': {
        'RequestId': 'abc123',
        'HTTPStatusCode': 200,
        'HostId': 'abc123'
    },
    'Marker': ''
}

@fixture
def s3_stub():
    expected_params = {'Bucket': 'test-bucket'}
    stubber.add_response('list_objects', response, expected_params)
    stubber.activate()
    yield stubber
    stubber.deactivate()


def test_get_data_from_s3(s3_stub):
    service_response = s3.list_objects(Bucket='test-bucket')
    assert service_response == response
    with raises(Exception) as exc:
        s3.list_objects(hello='42')
    print(exc)

def test_pending_responses(s3_stub):
    s3_stub.assert_no_pending_responses()