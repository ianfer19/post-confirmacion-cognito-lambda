import boto3
from utils.logger import get_logger

logger = get_logger(__name__)

class DynamoDBRepository:

    def __init__(self, table_name: str):
        self.table = boto3.resource("dynamodb").Table(table_name)

    def save_user(self, user):
        logger.info("Saving confirmed user in DynamoDB")

        self.table.put_item(
            Item={
                "sub": user.sub,
                "email": user.email,
                "name": user.name,
                "birthdate": user.birthdate,
                "gender": user.gender,
                "phone_number": user.phone_number,
                "confirmed_at": user.confirmed_at,
            }
        )
