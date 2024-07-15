import random as rd
import string as st

special_char=list(st.punctuation)
digits=list(st.digits)
alpha=list(st.ascii_letters)

char = special_char + digits + alpha
# print(char)
password = ""

user = int(input("Enter the length of your password: "))
for i in range(0,user):
    a = rd.choice(char) 
    password = password + a

print(f"Your strong password is {password}")