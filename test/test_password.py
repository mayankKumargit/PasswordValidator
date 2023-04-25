import unittest
import sys
sys.path.append(r'C:\Users\acer\Desktop\study\SEM VI\SE\Assignment2\PasswordValidator\app')
from password_valid import Password
class TestPassword(unittest.TestCase):
    def test_password_exists(self):
        pswd=Password()
    def test_password_not_empty(self):
        pswd=Password()
        result=pswd.isNull('')
if __name__ == "__main__":
    unittest.main()
