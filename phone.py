from symbol_factory import SymbolFactory

class Phone:
    def __init__(self, phone_letters):
        self.symbol_factory_object = SymbolFactory()
        pass

    def validate_phone(self):
        """
          Return false if a phone is not valid.
          A valid phone number should match these characteristics:
          - It should start with +.
          - It shouldn't be greater than 15 characters.
          - Aside from the + no other special character should be permitted (i.e: #,@,%,etc).
        """
        pass

    def get_string(self):
        """Returns the corresponding phone's string shape of the using only |, _, -, /, \ """
        phone_digit_shape = ""
        for symbol in self.phone_letters:
            symbol_digit = self.get_number(symbol)
            phone_digit_shape += self.symbol_factory_object.get_string(symbol_digit)
            # Adding space Between digits.
            phone_digit_shape += self.symbol_factory_object.get_string(" ")
        return phone_digit_shape

    def get_number(self, symbol):
        """
          Should convert letter to digit (see image in the README.md)
          clue 1: use a dictionary.
        """
        pass