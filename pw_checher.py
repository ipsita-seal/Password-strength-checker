import re
print("A strong password must contain Upper and lower cases, digits and special charecters. \nIt will be better to have a password of length greater than or equal to 8")
has_upper = re.search("[A-Z]", password)
has_lower = re.search("[a-z]", password)
has_digit = re.search("[0-9]", password)
has_special = re.search("[!@#$%^&*()_+]", password)
while True:
    password = input("\nEnter password (or type quit): ")
    if password == "quit":
        print("Goodbye!")
        break
    length_pword = len(password)
    if length_pword < 8:
      print("Password is weak.")
    elif length_pword >= 8 and has_lower and not has_digit and not has_special and not has_upper:
        print("Password strength: Weak")
    elif length_pword >= 8 and has_lower and has_digit and not has_special and not has_upper:
        print("Password strength: Medium")
    elif length_pword >= 8 and (has_lower or has_upper) and has_special and not has_digit:
        print("Password strength: Medium")
    elif length_pword >= 8 and has_lower and has_upper and has_digit and has_special:
        print("Password strength: Strong")
    else:
        print("Password strength: Medium")
