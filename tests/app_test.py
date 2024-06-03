import sys
import pytest

sys.path.insert(0, '..')  
from cw_praca_z_kodem.app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get('/')
    assert response.data.decode() == '<p>Hello, World!</p>'
    assert response.status_code == 200
