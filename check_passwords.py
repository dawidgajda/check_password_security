"""Password checking using API - https://haveibeenpwned.com/"""
from hashlib import sha1
from requests import get
from password_verification import PasswordVerification


class CheckPasswords:
    """Check secure password"""

    def __init__(self, passwords_file, secure_passwords_file, response_helper_file) -> None:
        self.passwords_file = passwords_file
        self.secure_passwords_file = secure_passwords_file
        self.response_helper_file = response_helper_file
        self.standard_passwords = []
        self.secure_passwords = []
        self.check_standard_passwords_from_text_file(self.passwords_file)
        self.check_passwords_in_have_i_been_pwned(self.response_helper_file)
        self.add_secure_passwords_to_text_file(self.secure_passwords_file)
        self.clear_response_helper_file(self.response_helper_file)

    def check_standard_passwords_from_text_file(self, passwords_file):
        """Check standard passwords

        Args:
            passwords_file txt: file with passwords
        """
        with open(passwords_file, mode='r', encoding='utf-8') as file:
            for line in file:
                if PasswordVerification(line).check_password():
                    self.standard_passwords.append(line.strip())

    def check_passwords_in_have_i_been_pwned(self, response_helper_file):
        """Check passwords in API

        Args:
            response_helper_file txt: helper file to write response hashes
        """
        for password in self.standard_passwords:
            line_counter = 0
            find_line_counter = 0
            password_hash = sha1(password.encode('utf-8')).hexdigest().upper()
            response = get(
                f'https://api.pwnedpasswords.com/range/{password_hash[0:5]}').text

            with open(response_helper_file, mode='w',
                      encoding='utf-8', newline='') as write_helper_file:
                write_helper_file.write(response)

            with open(response_helper_file, mode='r', encoding='utf-8') as read_helper_file:
                for line in read_helper_file:
                    line_counter += 1
                    if line.strip()[0:35] == password_hash[5:]:
                        find_line_counter += 1
                        break
                if line_counter - find_line_counter == line_counter:
                    self.secure_passwords.append(password)

    def add_secure_passwords_to_text_file(self, secure_passwords_file):
        """Save secure passwords

        Args:
            secure_passwords_file txt: file to save secure password
        """
        with open(secure_passwords_file, mode='w', encoding='utf-8') as write_secure_password_file:
            for password in self.secure_passwords:
                write_secure_password_file.write(password + '\n')

    def clear_response_helper_file(self, response_helper_file):
        """Clear helper file

        Args:
            response_helper_file txt: helper file with response hashes
        """
        with open(response_helper_file, mode='w', encoding='utf-8') as clear_helper_file:
            clear_helper_file.write('')
