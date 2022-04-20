from password_verification import PasswordVerification


def test_len_password():
    password = PasswordVerification('AdminAdmin')
    password_short = PasswordVerification('Admin')
    assert password.check_len() == True
    assert password_short.check_len() == False


def test_number_in_password():
    is_number = PasswordVerification('Admin1')
    not_is_number = PasswordVerification('Admin')
    assert is_number.check_is_number() == True
    assert not_is_number.check_is_number() == False


def test_upper_letter_in_password():
    is_upper = PasswordVerification('adminA')
    not_is_upper = PasswordVerification('admin')
    assert is_upper.check_is_upper_letter() == True
    assert not_is_upper.check_is_upper_letter() == False


def test_lower_letter_in_password():
    is_lower = PasswordVerification('ADMINa')
    not_is_lower = PasswordVerification('ADMIN')
    assert is_lower.check_is_lower_letter() == True
    assert not_is_lower.check_is_lower_letter() == False


def test_special_char_in_password():
    is_special_char = PasswordVerification('Admin!')
    not_is_special_char = PasswordVerification('Admin')
    assert is_special_char.check_is_special_char() == True
    assert not_is_special_char.check_is_special_char() == False


def test_check_password():
    is_standard = PasswordVerification('Admin1@#')
    assert is_standard.check_password() == True
    assert PasswordVerification('Admin1@').check_password() == False
    assert PasswordVerification('AdminAdmin@').check_password() == False
    assert PasswordVerification('admin1@a').check_password() == False
    assert PasswordVerification('ADMIN1@A').check_password() == False
    assert PasswordVerification('Admin1admin').check_password() == False
