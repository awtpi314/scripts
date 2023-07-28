import re

with open("phone_numbers_in") as inputData:
    phone_numbers = inputData.readlines()
    with open("phone_numbers_out", "w") as outputStream:
        correct_numbers = []
        for phone_number in phone_numbers:
            phone_number = re.sub(r"\+|\(|\)|-| ", "", phone_number)
            if phone_number[0] == "1":
                phone_number = phone_number[1:]
            if len(phone_number.rstrip()) == 0:
                correct_numbers.append("\n")
            else:
                correct_numbers.append("+1" + phone_number)
        outputStream.write("".join(correct_numbers))
