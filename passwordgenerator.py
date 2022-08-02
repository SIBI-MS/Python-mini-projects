import random
#"length"It specifies length of the password
length=int(input("Please enter length of password:"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#Creating random passwords
password="".join(random.sample(s,length))
print('Password:',password)
