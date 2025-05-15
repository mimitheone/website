import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_landing_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Your Stay' in response.data

def test_checkin_get(client):
    response = client.get('/checkin')
    assert response.status_code == 200
    assert b'Self Check-In' in response.data

def test_checkin_post_success(client):
    response = client.post('/checkin', data={'name': 'John Doe', 'reservation_code': 'ABC123'}, follow_redirects=True)
    assert b'Check-in successful!' in response.data

def test_checkin_post_missing_fields(client):
    response = client.post('/checkin', data={'name': '', 'reservation_code': ''}, follow_redirects=True)
    assert b'Please fill in all fields.' in response.data 