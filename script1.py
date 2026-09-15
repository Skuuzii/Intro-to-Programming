name = input("Please enter your name:")
print("Hello, " + name)

num1 = int(input("Please enter the first variable:"))
opp = input("Order of operation?: * or /")
num2 = int(input("Please enter the second variable:"))
ans = eval(num1 + opp + num2)

print("The answer to your query is:", ans)
