import pytest

@pytest.fixture
def sample_signup_input():
    return {'FirstName': 'Calista', 
            'LastName': 'Phippen', 
            'Email': 'calista.phippen1@marist.edu', 
            'PhoneNumber': '1234567891', 
            'Password': 'mypassword'
            }

@pytest.fixture
def sample_login_input():
    return {
        'Email': 'calista.phippen1@marist.edu', 
        'Password': 'mypassword'
    }


def test_signup_invalid_first_name(test_client):
    # Provide invalid first name (with numbers) in the signup data
    invalid_signup_input = {
        'FirstName': 'Calista123',  # Invalid first name with numbers
        'LastName': 'Phippen',
        'Email': 'calista.phippen1@marist.edu',
        'PhoneNumber': '1234567891',
        'Password': 'mypassword'
    }

    response = test_client.post('/signup', data=invalid_signup_input)

    assert response.status_code == 200  
    assert b"First name can only contain letters." in response.data  


#Create at least one test case that injects a critical error   
from unittest.mock import patch

def test_signup_database_error_handling(test_client, sample_signup_input):

    with patch('db.server.db.session.execute') as mock_execute:
        mock_execute.side_effect = Exception("Database connection error")

       
        response = test_client.post('/signup', data=sample_signup_input)
        
        
        assert response.status_code == 200  
        assert b"Something went wrong on our end." in response.data    