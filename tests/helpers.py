plus = [
  "    ___    ",
  "   |   |   ",
  " __|   |__ ",
  "|         |",
  "|__     __|",
  "   |   |   ",
  "   |___|   ",
]
space = [
  "  ",
  "  ",
  "  ",
  "  ",
  "  ",
  "  ",
  "  ",
]
number_one = [
  "  ____   ",
  " /    |  ",
  "/_/|  |  ",
  "   |  |  ",
  "   |  |  ",
  "  _|  |_ ",
  " |______|",
]
number_five = [
  " ______ ",
  "|  ____|",
  "|  |__  ",
  "|____ \\ ",
  " _   \\ |",
  "| |__| |",
  " \____/ ",
]
number_eight = [
  "  _____  ",
  " /  _  \\ ",
  "/  |_|  \\",
  "\\       /",
  "/   _   \\",
  "\\  |_|  /",
  " \\_____/ ",
]
number_nine = [
  "  _______ ",
  " /   _   |",
  "|   |_|  |",
  " \\___    |",
  "     |   |",
  "     |   |",
  "     |___|",
]

phone_15559998888 = ""
# +15559998888
phone_digit_shape_lists = [
  plus, space,
  number_one, space,
  number_five, space,
  number_five, space,
  number_five, space,
  number_nine, space,
  number_nine, space,
  number_nine, space,
  number_eight, space,
  number_eight, space,
  number_eight, space,
  number_eight, space,
]
number_of_rows = len(phone_digit_shape_lists[0])
number_of_columns = len(phone_digit_shape_lists)
for row_index in range(number_of_rows):
    for column_index in range(number_of_columns):
      phone_15559998888 += phone_digit_shape_lists[column_index][row_index]
    phone_15559998888 += "\n"
