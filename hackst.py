f = open("dictionary.txt", "r")
print("Can you survive a dictonary attack?")
test_password = input("Choose your password:")
password = test_password.strip()
#found = False
password_1 = password.lower()
for line in f:
    line_stripped = line.strip()
    if password_1 == line_stripped:
        print("No. Just no.")
        break
