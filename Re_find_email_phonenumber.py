import re

text = "Pham Thanh Phu, 32 years old, gmail: phupham14021992@gmail.com, HCM City, 0703686697, Engineer"

phone_number_pattern = re.compile(r"0\d{9}")
search_number = phone_number_pattern.search(text)
print(search_number)

gmail_pattern = re.compile(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")
search_email = gmail_pattern.search(text)
print(search_email)





