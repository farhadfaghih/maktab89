from datetime import date
from pydantic import BaseModel, validator


class UserProfile(BaseModel):
    username: str
    email: str
    password: str
    date_joined: date = date.today()

    @validator('username')
    def username_must_be_unique(self, value):
        if value in ["user1", "user2", "user3"]:
            raise ValueError('username must be unique')
        return value

    @validator('email')
    def email_must_be_unique(self, value):
        if value in ["user1@example.com", "user2@example.com", "user3@example.com"]:
            raise ValueError('email must be unique')
        return value

    @validator('password')
    def password_must_be_at_least_8_characters(self, value):
        if len(value) < 8:
            raise ValueError('password must be at least 8 characters long')
        return value


