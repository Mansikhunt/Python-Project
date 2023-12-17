import random

print("Password Generator")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,"
number = int(input("Number of password to generate: "))
length = int(input("Enter your password length: "))

print("\nHere are your passwords: ")

for pwd in range(number):
    passwords = ""
    for p in range(length):
        passwords += random.choice(chars)
    print(passwords)