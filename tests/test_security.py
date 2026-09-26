from app.core.security import hash_password, verify_password


def test_verify_password_correct():
    hashed = hash_password("mypassword123")
    assert verify_password("mypassword123", hashed) is True


def test_verify_password_incorrect():
    hashed = hash_password("mypassword123")
    assert verify_password("wrongpassword", hashed) is False