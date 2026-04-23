char = input("enter anything: ")
alphs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for alphabets in char:
    if alphabets in alphs:
        print("it has alphabets")
        break
else:
    print("it does not have alphabets")