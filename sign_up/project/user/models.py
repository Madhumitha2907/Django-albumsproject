from django.db import models
from django.core.validators import EmailValidator, RegexValidator

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number')]
    )
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.password1 != self.password2:
            raise ValueError("Passwords must match")
        super().save(*args, **kwargs)
