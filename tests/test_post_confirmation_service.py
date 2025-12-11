import pytest
from unittest.mock import MagicMock
from src.post_confirmation.application.post_confirmation_service import PostConfirmationService
from src.post_confirmation.domain.exceptions import PostConfirmationError

EVENT = {
    "request": {
        "creationDate": "2025-01-10T12:00:00Z",
        "userAttributes": {
            "sub": "123-abc",
            "email": "test@example.com",
            "name": "John Doe",
            "birthdate": "1990-01-01",
            "gender": "male",
            "phone_number": "+123456789"
        }
    }
}

def test_postconfirmation_success():
    mock_repo = MagicMock()
    service = PostConfirmationService(mock_repo)

    user = service.process(EVENT)

    assert user.email == "test@example.com"
    assert user.sub == "123-abc"
    mock_repo.save_user.assert_called_once()


def test_postconfirmation_dynamo_failure():
    mock_repo = MagicMock()
    mock_repo.save_user.side_effect = Exception("Dynamo error")

    service = PostConfirmationService(mock_repo)

    with pytest.raises(PostConfirmationError):
        service.process(EVENT)
