import logging

def validate_user_count(users):
    logging.info("Validing User count")
    assert len(users) > 0, "No Users returned from API"

def validate_user_fields(users):
    logging.info("Validing user fields")
    required_fields = ["id", "name", "email"]

    for user in users:
        for field in required_fields:
            assert field in user, f"Missing field: {field}"

def validate_email_format(users):
    logging.info("Validating email format")
    for user in users:
        assert "@" in user["email"], f"Invalid email: {user['email']}"