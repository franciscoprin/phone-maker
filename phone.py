from symbol_factory import SymbolFactory

class Phone:
    def __init__(self, phone_letters):
        self.symbol_factory_object = SymbolFactory()
        self.phone_letters = phone_letters

    def validate_phone(self):
        """
          Return false if a phone is not valid.
          A valid phone number should match these characteristics:
          - It should start with +.
          - It shouldn't be smaller than 15 characters.
          - Aside from the + no other special character should be permitted (i.e: #,@,%,etc).
        """
        if self.phone_letters:
            if self.phone_letters[0] == "+" and len(self.phone_letters) < 15:
                return True
        return False

    def get_string(self):
        """Returns the corresponding phone's string shape of the using only |, _, -, /, \ """
        phone_digit_shape_lists = []
        for symbol in self.phone_letters:
            symbol_digit = self.get_number(symbol)
            phone_digit_shape_lists.append(self.symbol_factory_object.get_string(symbol_digit))
            # Adding space Between digits.
            phone_digit_shape_lists.append(self.symbol_factory_object.get_string(" "))
        # Render numbers in a row.
        phone_digit_shape = ""
        number_of_rows = len(phone_digit_shape_lists[0])
        number_of_columns = len(phone_digit_shape_lists)
        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                phone_digit_shape += phone_digit_shape_lists[column_index][row_index]
            phone_digit_shape += "\n"
        return phone_digit_shape

    def get_number(self, symbol):
        """
          Should convert letter to digit (see image in the README.md)
          clue 1: use a dictionary.
        """
        pass