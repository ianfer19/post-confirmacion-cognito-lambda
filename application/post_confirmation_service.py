from domain.models import ConfirmedUser
from domain.exceptions import PostConfirmationError
from utils.logger import get_logger
import datetime

logger = get_logger(__name__)

class PostConfirmationService:

    def __init__(self, dynamo_repo):
        self.dynamo_repo = dynamo_repo

    def process(self, event):
        try:
            logger.info("Processing Cognito PostConfirmation event")

            attrs = event["request"]["userAttributes"]
            print(attrs)

            user = ConfirmedUser(
                sub=attrs["sub"],
                email=attrs["email"],
                name=attrs.get("name", ""),
                birthdate=attrs.get("birthdate", ""),
                gender=attrs.get("gender", ""),
                phone_number=attrs.get("phone_number", ""),
                confirmed_at=datetime.datetime.now().isoformat(),
            )

            # Guardar en DynamoDB
            self.dynamo_repo.save_user(user)

            logger.info("User successfully processed in PostConfirmation trigger")

            return user

        except Exception as e:
            logger.error(f"PostConfirmationService error: {str(e)}")
            raise PostConfirmationError(str(e))
