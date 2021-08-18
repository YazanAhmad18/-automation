from automation import __version__
from automation.automation import emails, phone, edit_format_phone_number

def test_version():
    assert __version__ == '0.1.0'


def test_auto_email():
    assert (emails("./potential-contacts.txt"))[0] == 'danielletaylor@hotmail.com'

def test_auto_phone():
    assert (phone("./potential-contacts.txt"))[0] == '178-383-0937'

def test_auto_email_2():
    assert (emails("./potential-contacts.txt"))[2] == 'megan54@kramer-solis'

def test_auto_phone_2():
    assert (phone("./potential-contacts.txt"))[1] == '048-736-2919'
