name = input("Please enter your name:")
print("Hello, " + name)

num1 = int(input("Please enter the first variable:"))
opp = input("Order of operation?: *, %, +, -, /")
num2 = int(input("Please enter the second variable:"))
ans = eval(str(num1) + opp + str(num2))

print("The answer to your query is:", str(num1) , opp , str(num2),"=", ans)

  
