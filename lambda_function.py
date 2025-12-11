import os
from application.post_confirmation_service import PostConfirmationService
from infrastructure.dynamodb_repository import DynamoDBRepository
from utils.logger import get_logger
from domain.exceptions import PostConfirmationError

logger = get_logger(__name__)

TABLE_NAME = os.environ.get("USERS_TABLE")  # Variable de entorno

dynamo_repo = DynamoDBRepository(TABLE_NAME)
post_service = PostConfirmationService(dynamo_repo)

def lambda_handler(event, context):
    """
    Este Lambda se dispara automáticamente cuando el usuario confirma su email/telefono en Cognito.
    Siempre debe devolver `event` para que Cognito complete el flujo correctamente.
    """

    logger.info("PostConfirmation Lambda invoked")

    try:
        post_service.process(event)
        return event  # obligatorio

    except PostConfirmationError as e:
        logger.error(f"PostConfirmation error: {str(e)}")
        return event  # Cognito exige devolver event aunque falle

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return event
