import random
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

len_pass = int(input("Kaç haneli şifre istersiniz  "))
my_password = ""


for i in range(len_pass):
    my_password += random.choice(chars)


print(my_password)



