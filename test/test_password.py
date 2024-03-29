import unittest
import sys
sys.path.append(r'C:\Users\acer\Desktop\application\app')
from password_valid import Password
class TestPassword(unittest.TestCase):
    def test_password_exists(self):
        pswd=Password()
    def test_password_not_empty(self):
        pswd=Password()
        result=pswd.isNotNull('aJsj5Y@d!j')
        self.assertIsNotNone(result)
        self.assertEqual(1,result)
    def test_password_length_checker(self):
        pswd=Password()
        result=pswd.checkLength('aJsj5Y@d!j')
        self.assertEqual(1,result)
    def test_password_uppercase_checker(self):
        pswd=Password()
        result=pswd.checkUppercase('aJsj5Y@d!j')
        self.assertEqual(1,result)
    def test_password_lowercase_checker(self):
        pswd=Password()
        result=pswd.checkLowercase('aJsj5Y@d!j')
        self.assertEqual(1,result)
    def test_password_digit_checker(self):
        pswd=Password()
        result=pswd.checkDigit('aJsj5Y@d!j')
        self.assertEqual(1,result)
    def test_password_special_character_checker(self):
        pswd=Password()
        result=pswd.checkSpecialChar('aJsj5Y@d!j')
        self.assertEqual(1,result)
    def test_password_whitespace_checker(self):
        pswd=Password()
        result=pswd.checkSpace('aJsj5Y@d!j')
        self.assertEqual(1,result)
    def test_password_repeating_checker(self):
        pswd=Password()
        result=pswd.checkRepeat('aJsj5Y@d!j')
        self.assertEqual(1,result)
    def test_password_other_character_checker(self):
        pswd=Password()
        result=pswd.checkOther('aJsj5Y@d!j')
        self.assertEqual(1,result)
if __name__ == "__main__":
    unittest.main()
