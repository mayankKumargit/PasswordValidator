import unittest
import sys
sys.path.append(r'C:\Users\acer\Desktop\study\SEM VI\SE\Assignment2\PasswordValidator\app')
from password_valid import Password
class TestPassword(unittest.TestCase):
    def test_password_exists(self):
        pswd=Password()
    def test_password_not_empty(self):
        pswd=Password()
        result=pswd.isNull('rt5ybhs!')
        self.assertIsNotNone(result)
    def test_password_length_checker(self):
        pswd=Password()
        result=pswd.checkLength('afedsc33fd')
        self.assertEqual(1,result)
    def test_password_uppercase_checker(self):
        pswd=Password()
        result=pswd.checkUppercase('aJsj5Y@dj')
        self.assertEqual(1,result)
if __name__ == "__main__":
    unittest.main()
