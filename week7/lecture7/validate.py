# email = input("What's your email? ").strip()

# if "@" in email:
#     print("valid")
# else:
#     print("Invalid")

# email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")


# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and "." in domain:
#     print("valid")
# else:
#     print("Invalid")

# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("valid")
# else:
#     print("Invalid")


# Regular Expressions
# import re

# email = input("What's your email? ").strip()

# if re.search(".*@.*", email):
#     print("valid")
# else:
#     print("Invalid")

# if re.search("..*@..*", email):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(".+@.+", email):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(".+@.+.edu", email):
#     print("valid")
# else:
#     print("Invalid")


# if re.search(r".+@.+\.edu", email):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(r"^.+@.+\.edu$", email):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(r"^[\w\s]+@\w+\.(com|edu|gov|net|org)$", email):
#     print("valid")
# else:
#     print("Invalid")


import re

email = input("What's your email? ").strip()
# email = input("What's your email? ").strip().lower()

# if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email.lower()):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
#     print("valid")
# else:
#     print("Invalid")


# if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
#     print("valid")
# else:
#     print("Invalid")

# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
#     print("valid")
# else:
#     print("Invalid")

if re.search(r"^[a-zA-Z0-9_\.]+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("valid")
else:
    print("Invalid")



