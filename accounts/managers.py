from typing import Any, Optional
from django.contrib.auth.models import UserManager


class UserManager(UserManager):
    def create_user(self ,email: str , password: str | None ,**extra_fields: Any):
        """Create and save user with given email

        Args:
            email (str): User given email
            password (str | None): User given password

        Raises:
            ValueError: Email must be set
        """

        if not email:
            raise ValueError("Email must be set")



        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)

        user.save()
        return user


    def create_superuser(self, email: str, password: str | None, **extra_fields: Any):
        """Create superUser with given email and password

        Args:
            email (str): user given email
            password (str | None): user given password

        Returns:
            _type_: user
        """
        user = self.create_user(email=email,password=password,**extra_fields)

        user.is_admin = True
        user.save()

        return user