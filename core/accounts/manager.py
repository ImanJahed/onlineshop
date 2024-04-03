from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **extra_fields):
        """
        Custom user model manager where email is the unique identifiers
        for authentication instead of usernames.
        """

        if not username:
            raise ValueError("Username must be set")

        if not email:
            raise ValueError('Email must be set')


        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)

        user.save()
        return user


    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('type',4)


        if not extra_fields.get('is_admin'):
            raise ValueError("Admin must have is_admin=True")

        if not extra_fields.get('is_staff'):
            raise ValueError("Admin must have is_staff=True")

        return self.create_user(username, email, password, **extra_fields)

