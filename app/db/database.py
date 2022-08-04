from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    #: This is a username
    username = fields.CharField(max_length=20, unique=True)  # noqa: WPS432
    name = fields.CharField(max_length=50, null=True)  # noqa: WPS432
    category = fields.CharField(max_length=30, default="misc")  # noqa: WPS432
    password_hash = fields.CharField(max_length=128, null=True)  # noqa: WPS432
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class PydanticMeta:
        exclude = ["password_hash"]


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserInDb", exclude_readonly=True)
