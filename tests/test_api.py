import pytest
from src.api_client import get_users
from src.validations import validate_user_count, validate_user_fields, validate_email_format
from src.logger import setup_logger
setup_logger()

@pytest.mark.parametrize("validation_func", [validate_user_count, validate_user_fields, validate_email_format])

def test_validations(validation_func):
    users = get_users()
    validation_func(users)



