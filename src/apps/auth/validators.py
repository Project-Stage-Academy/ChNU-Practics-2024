from django.core.exceptions import ValidationError


def is_special_symbol(char):
    return char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"


class CustomPasswordValidator:
    def __init__(
        self,
        require_uppercase=True,
        require_number=True,
        require_special_symbol=True,
    ):
        self.require_uppercase = require_uppercase
        self.require_number = require_number
        self.require_special_symbol = require_special_symbol

    def validate(self, password, user=None):
        if self.require_uppercase and not any(char.isupper() for char in password):
            raise ValidationError(
                "Password must contain at least one uppercase letter.",
                code="password_no_upper",
            )

        if self.require_number and not any(char.isdigit() for char in password):
            raise ValidationError(
                "Password must contain at least one number.",
                code="password_no_digit",
            )

        if self.require_special_symbol and not any(
            is_special_symbol(char) for char in password
        ):
            raise ValidationError(
                "Password must contain at least one special symbol.",
                code="password_no_symbol",
            )

    def get_help_text(self):
        return "Your password must contain at least one uppercase letter, one number, and one special symbol."
