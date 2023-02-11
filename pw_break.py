# log into device via serial port and attempt passwords.    Username is needed.

# import re
# import time
# import serial

# serial port variables
s_port = "COM5"
s_baud = 9600

username = "ADMIN"              # default username
prompt = "#"

starting_pw = "abxcc"

# characters = "abcdefghijklmnopqrstuvwxyzABCEDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=/"
characters = "abcde/"
end_char = "c"


def pw_increment(old_pw):
    new_pw = ""
    pw_range = range(0, len(old_pw) - 1)
#    print(f"the length of old_pw = {len(old_pw)}")

#    for x in pw_range:
#        print(old_pw[x])

    for letter in pw_range:
        new_pw += old_pw[letter]
#        print (f"new_pw = {new_pw}")

    last_letter = old_pw[len(old_pw) - 1]
    letter_location = characters.index(last_letter)

    if last_letter == "/":
        new_pw += "a"
    else:
        new_pw += characters[(letter_location + 1)]

    return new_pw


def rollover(pw_length):
    new_pass = ""
    for x in range(0, (pw_length + 1)):
        new_pass += "a"
    return new_pass



def pw_inc(old_pw):
    new_pass = ""
    pw_len = len(old_pw)
    end_count = 0
    small_count = 0

    for letter in range(pw_len, 0, -1):
        print(old_pw[letter])




    return new_pass







if __name__ == "__main__":

    password = starting_pw

    for z in range(0,5):
        #new_password = pw_increment(password)
        new_password = pw_inc(password)
        print (new_password)
        password = new_password