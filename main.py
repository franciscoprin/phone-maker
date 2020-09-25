from phone import Phone

phone_is_invalid = True
while phone_is_invalid:
    letters_phone_number = input("Enter a valid phone, please: ")
    print(letters_phone_number)
    phone_object = Phone(phone_letters=letters_phone_number)
    phone_is_invalid = not phone_object.validate_phone()
    # if phone_is_invalid:
    #     print("Your phone number is invalid.")

print(phone_object.get_string())
