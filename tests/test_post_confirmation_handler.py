from unittest.mock import MagicMock, patch
from lambda_function import lambda_handler

EVENT = {
    "request": {
        "creationDate": "2025-01-10T12:00:00Z",
        "userAttributes": {
            "sub": "123",
            "email": "test@example.com",
            "name": "Jane",
            "birthdate": "1980-01-01",
            "gender": "female",
            "phone_number": "+111111111"
        }
    }
}

@patch("src.post_confirmation.handler.post_service")
def test_handler_success(mock_service):
    result = lambda_handler(EVENT, None)
    assert result == EVENT
    mock_service.process.assert_called_once()


@patch("src.post_confirmation.handler.post_service")
def test_handler_failure(mock_service):
    mock_service.process.side_effect = Exception("boom")

    result = lambda_handler(EVENT, None)
    assert result == EVENT  # Cognito always expects the event back
