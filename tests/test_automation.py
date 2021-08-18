from automation import __version__
from automation.automation import emails, get_phone_numbers, edit_format_phone_number

def test_version():
    assert __version__ == '0.1.0'


def test_auto_email():
    assert (emails("./potential-contacts.txt"))[0] == 'danielletaylor@hotmail.com'

def test_auto_phone():
    assert (get_phone_numbers("./potential-contacts.txt"))[0] == '178-383-0937'