user = int(input("Enter The Size: "))  # Jaise 5

a = 0   # pehla number
b = 1   # dusra number

print("Fibonacci Series:")

for i in range(user):
    print(a)         # pehle a print karo
    c = a + b        # next number = a + b
    a = b            # a ko aage badhao
    b = c            # b ko bhi aage badhao
