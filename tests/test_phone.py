import unittest
from phone import Phone
from .helpers import phone_15559998888

class TestPhone(unittest.TestCase):

    def test_validate_phone_start_with_plus(self):
        phone_start_with_plus = Phone("+13463335555")
        phone_doesnt_start_with_plus = Phone("13463335555")
        assert phone_start_with_plus.validate_phone()
        assert not phone_doesnt_start_with_plus.validate_phone()

    def test_validate_phone_smaller_than_15_characters(self):
        phone_at_the_right_size = Phone("+13463335555")
        phone_greater_than_15_characters = Phone("+13463335555321412342134")
        assert phone_at_the_right_size.validate_phone()
        assert not phone_greater_than_15_characters.validate_phone()

    def test_validate_phone_doesnt_allow_special_characters(self):
        phone_without_special_characters = Phone("+13463335555")
        phone_with_special_characters = Phone("!~#$%^&*@|}{")
        assert phone_without_special_characters.validate_phone()
        assert not phone_with_special_characters.validate_phone()

    def test_get_string(self):
        phone = Phone("+15559998888")
        assert phone_15559998888 == phone.get_string()

    def test_get_number(self):
        phone = Phone("+13463335555")
        for number in range(10):
            assert phone.get_number(str(number)) == str(number)
        assert phone.get_number("A") == "2"
        assert phone.get_number("a") == "2"
        assert phone.get_number("B") == "2"
        assert phone.get_number("b") == "2"
        assert phone.get_number("C") == "2"
        assert phone.get_number("c") == "2"
        assert phone.get_number("D") == "3"
        assert phone.get_number("d") == "3"
        assert phone.get_number("E") == "3"
        assert phone.get_number("e") == "3"
        assert phone.get_number("F") == "3"
        assert phone.get_number("f") == "3"
        assert phone.get_number("G") == "4"
        assert phone.get_number("g") == "4"
        assert phone.get_number("H") == "4"
        assert phone.get_number("h") == "4"
        assert phone.get_number("I") == "4"
        assert phone.get_number("i") == "4"
        assert phone.get_number("J") == "5"
        assert phone.get_number("j") == "5"
        assert phone.get_number("K") == "5"
        assert phone.get_number("k") == "5"
        assert phone.get_number("L") == "5"
        assert phone.get_number("l") == "5"
        assert phone.get_number("m") == "6"
        assert phone.get_number("M") == "6"
        assert phone.get_number("N") == "6"
        assert phone.get_number("n") == "6"
        assert phone.get_number("O") == "6"
        assert phone.get_number("o") == "6"
        assert phone.get_number("P") == "7"
        assert phone.get_number("p") == "7"
        assert phone.get_number("Q") == "7"
        assert phone.get_number("q") == "7"
        assert phone.get_number("q") == "7"
        assert phone.get_number("R") == "7"
        assert phone.get_number("r") == "7"
        assert phone.get_number("S") == "7"
        assert phone.get_number("s") == "7"
        assert phone.get_number("T") == "8"
        assert phone.get_number("t") == "8"
        assert phone.get_number("U") == "8"
        assert phone.get_number("u") == "8"
        assert phone.get_number("V") == "8"
        assert phone.get_number("v") == "8"
        assert phone.get_number("W") == "9"
        assert phone.get_number("w") == "9"
        assert phone.get_number("Y") == "9"
        assert phone.get_number("y") == "9"
        assert phone.get_number("Z") == "9"
        assert phone.get_number("z") == "9"
