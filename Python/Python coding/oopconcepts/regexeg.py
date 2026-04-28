# # import re
# #
# # txt = input("Enter a text: ")
# # bpat = input("Enter Beginning Pattern: ")
# # epat = input("Enter Ending Pattern: ")
# #
# #
# # if re.search('^' +bpat,string=txt):
# # # if re.match(pattern=bpat, string=txt):
# #     print("Beginning pattern available")
# # else:
# #     print("Beginning pattern not found")
# #
# # if re.search(epat + r"$", txt):
# #
# # # if re.match(pattern=epat, string=txt):
# #     print("Ending pattern available")
# # else:
# #     print("Ending pattern not found")
#
#
#
# #digit matching
#
#
# # import re
# #
# # txt = input("Enter a text: ")
# #
# # if re.fullmatch(r"\d+", txt):
# #     print("Digit found in the text")
# # else:
# #     print("No digit found")
# # #
# # import re
# # phone = input('Enter the Phno :')
# # pat = '[0-9]'
# # if re.search(pattern=pat,string=phone):
# #     print("Only digits")
# #
# # else:
# #     print("Other digits")
#
#
#
# # import re
# #
# # txt = input("Enter a text: ")
# #
# # # ^\d+$ means: start → digits → end
# # if re.fullmatch(r"\d+", txt):
# #     print("Valid: only numbers allowed")
# # else:
# #     print("Invalid: contains non-numeric characters")
#
#
# # #username
# # import re
# # un = input("Enter the user name ")
# #
# # pat = r"^[a-z_]{8,}$"
# #
# # if re.match(pattern = pat , string = un):
# #     print('valid')
# # else:
# #     print('Invalid')
#
# #
# # import re
# # email = input("enter the email :")
# # pat=r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"
# # if re.match(pattern = pat , string = email):
# #     print('valid')
# # else:
# #     print('Invalid')
#
# #password
#
# import re
#
# password = input("Enter your password: ")
#
# # Regex pattern for strong password
# # pat = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
# pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[_@-]).{8,}$"
# if re.fullmatch(pat, password):
#     print("Valid password")
# else:
#     print("Invalid password")


import re

txt = input('Text : ')
pat = r"\s+"

# print(re.sub(pattern=pat , string=txt,repl=' '))

print(re.split(pattern=pat , string=txt))


