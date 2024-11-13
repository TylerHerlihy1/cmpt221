import pytest

# example fixture - user input
# hint... can you do something similar for login?
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
