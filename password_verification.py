from string import punctuation

PASSWORD_LENGTH = 8
NUMBERS = '0123456789'
SPECIAL_CHAR = list(punctuation)


class PasswordVerification:
    def __init__(self, password) -> None:
        self.password = password
        self.password_standard = True

    def change_flag_password_standard(self):
        self.password_standard = False
        return self.password_standard

    def check_password(self):
        if len(self.password) < PASSWORD_LENGTH:
            self.change_flag_password_standard()

        is_number = 0
        for char in self.password:
            if char not in NUMBERS:
                is_number += 1
            if is_number == len(self.password):
                self.change_flag_password_standard()

        is_upper = 0
        for char in self.password:
            if not char.isupper():
                is_upper += 1
            if is_upper == len(self.password):
                self.change_flag_password_standard()

        is_lower = 0
        for char in self.password:
            if not char.islower():
                is_lower += 1
            if is_lower == len(self.password):
                self.change_flag_password_standard()

        is_special_char = 0
        for char in self.password:
            if char not in SPECIAL_CHAR:
                is_special_char += 1
            if is_special_char == len(self.password):
                self.change_flag_password_standard()

        return self.password_standard
