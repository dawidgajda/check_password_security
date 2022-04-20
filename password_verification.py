"""Password verification
Min eight length
Min one number
Min one upper letter
Min one lower letter
Min one special char

    Returns:
        Boolean: True when meets standard or else False
    """
from string import punctuation

PASSWORD_LENGTH = 8
NUMBERS = '0123456789'
SPECIAL_CHAR = list(punctuation)


class PasswordVerification:
    """Password verification"""

    def __init__(self, password) -> None:
        self.password = password
        self.password_standard = True
        self.check_values = []

    def check_len(self):
        """Check length password

        Returns:
            Boolean: True when meets standard or else False
        """
        if len(self.password) < PASSWORD_LENGTH:
            return not self.password_standard
        return self.password_standard

    def check_is_number(self):
        """Check is number in password

        Returns:
            Boolean: True when meets standard or else False
        """
        for char in self.password:
            if char in NUMBERS:
                return self.password_standard
        return not self.password_standard

    def check_is_upper_letter(self):
        """Check is upper letter in password

        Returns:
            Boolean: True when meets standard or else False
        """
        for char in self.password:
            if char.isupper():
                return self.password_standard
        return not self.password_standard

    def check_is_lower_letter(self):
        """Check is lower letter in password

        Returns:
            Boolean: True when meets standard or else False
        """
        for char in self.password:
            if char.islower():
                return self.password_standard
        return not self.password_standard

    def check_is_special_char(self):
        """Check is special char in password

        Returns:
            Boolean: True when meets standard or else False
        """
        for char in self.password:
            if char in SPECIAL_CHAR:
                return self.password_standard
        return not self.password_standard

    def check_password(self):
        """Check all standard in password

        Returns:
            Boolean: True when meets standard or else False
        """
        self.check_values.append(self.check_len())
        self.check_values.append(self.check_is_number())
        self.check_values.append(self.check_is_upper_letter())
        self.check_values.append(self.check_is_lower_letter())
        self.check_values.append(self.check_is_special_char())
        print(self.check_values)

        if all(self.check_values):
            return True
        return False
