from password_verification import PasswordVerification


def test_len_password():
    password = 'Admin1!'
    password_verification = PasswordVerification(password)
    assert password_verification.check_password() == False


def test_number_in_password():
    password = 'AdminAdmin!'
    password_verification = PasswordVerification(password)
    assert password_verification.check_password() == False


def test_upper_letter_in_password():
    password = 'adminadmin1!'
    password_verification = PasswordVerification(password)
    assert password_verification.check_password() == False


def test_lower_letter_in_password():
    password = 'ADMINADMIN1!'
    password_verification = PasswordVerification(password)
    assert password_verification.check_password() == False


def test_special_char_in_password():
    password = 'AdminAdmin1'
    password_verification = PasswordVerification(password)
    assert password_verification.check_password() == False


def test_password_standard():
    password = 'Admin1!Admin2@'
    password_verification = PasswordVerification(password)
    assert password_verification.check_password() == True
