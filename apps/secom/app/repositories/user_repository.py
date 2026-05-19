import logging

from secom.app.schemas.user_schema import UserSchema

logger = logging.getLogger(__name__)


class UserRepository:

    def __init__(self) -> None:
        pass

    def save_user(self, user_schema: UserSchema) -> None:
        logger.info(
            "[UserRepository] save_user 레이어 진입 — %s",
            user_schema.model_dump(),
        )
        # TODO: UserModel 영속화
        logger.info(
            "[UserRepository] save_user 레이어 완료 — userId=%s",
            user_schema.userId,
        )
