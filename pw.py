def lowerCase(password):
    small_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                  't', "u", "v", "w", "x", "y", "z"]
    for letter in password:
        for controller in small_list:
            if letter == controller:
                return True
    return False


def upperCase(password):
    big_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "S",
                "T", "U", "V", "W", "X", "Y", "Z"]
    for letter in password:
        for controller in big_list:
            if letter == controller:
                return True
    return False


def number(password):
    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for letter in password:
        for controller in number_list:
            if letter == controller:
                return True
    return False


def punctuation(password):
    punctuation_list = [".", ",", ":", ";", "!", "'", "^", "+", "%", "&", "/", "(", ")",
                        "=", "*", "?", "-", "_", "#", ">", "<", "é"]
    for letter in password:
        for controller in punctuation_list:
            if letter == controller:
                return True
    return False


def control(password):
    small = lowerCase(password)
    big = upperCase(password)
    num = number(password)
    punc = punctuation(password)
    if len(password) < 16 and len(password) > 6:
        length = True
    else:
        length = False
    if small == True and big == True and num == True and punc == True and length == True:
        print("Your password is best")
    else:
        print("Your password is bad")


user_password = input("Please enter the password: ")

control(user_password)
