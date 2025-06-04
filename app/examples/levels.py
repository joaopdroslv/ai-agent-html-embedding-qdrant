from app.schemas.user_level import UserLevel
from app.enums.user_level import UserLevelEnum

admin = UserLevel(
    id=UserLevelEnum.admin.value,
    name="Admins",
)

final_user = UserLevel(
    id=UserLevelEnum.final_user.value,
    name="Final Users",
)

operational = UserLevel(
    id=UserLevelEnum.operational.value,
    name="Operationals",
)
