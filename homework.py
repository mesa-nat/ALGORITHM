# EX_1
text = "mesa"
for char in text:
    print(char)

# EX-2___________________________________________
text = input("enter text: ")
for i in range (len(text)):
    print(i)

# Ex-3_____________________________________________
text = input("enter text: ")
result = "no"
for cha in text:
    if cha.isupper():
        result = "yes"
print(result)

# Ex-4______________________________________________
    # Q-1
text = "3 4 5 6"
result = ""
for num in text:
   if num != " ":
    result += num
    print(result)
    # Q-2
text = "3 4 5 6"
total = 0
for num in text:
    if num != " ":
      total += int(num)
print(total)

# Ex-5_________________________________________________
    # Q-1
input = "454639"
coun_odd = 0
coun_even = 0
for i in range (len(input)):
    if i % 2 == 0:
        coun_even += 1
    if i % 2 == 1:
        coun_odd += 1
print(coun_even)
print(coun_odd)
    # Q-2
input = "454639"
result = 0
for num in input:
    result += int(num)
print(result)
    #  Q-3
input = '454639'
result = 0
for char in input:
    if int(char) % 2 == 0:
        result += int(char)
print(result)
    #  Q-4
input = '454639'
result = 0
for num in input:
    result = input[::-1]
print(result)

# Ex-6___________________________________________________
num = input("enter num: ")
if num % 2 == 1:
    print("odd")
else:
    print("even")

# Ex-7____________________________________________________
num = 21
if num >= 10 and num <= 20:
    print("continue")
if num > 20:
    print("out of range")

# Ex-8_____________________________________________________
    # Q-1
input = '93948884039'
coun = 0
for num in input:
    if num == '8':
        coun += 1
print(coun)
    # Q-2
isFound = False
index = 0
while not isFound:
    input = '93948884039'
    if input[index] == '8':
        first_index = index
        isFound = True
        print(first_index)
    index += 1

# Ex-9________________________________________________________
input = "3 4 5 6"
result = ""
for num in input:
    if num != " ":
        result += num
print(result)
    #  Q-2
text = ("3456 ")
result = 0
for cha in text:
    if cha != " ":
       result = int(cha)*2
       print(result)

# Ex-10_______________________________________________
num1 = int(input("Number 1: "))
max_value = num1
min_value = num1
for i in range(2,6):
    num = int(input("Number " + str(i) + ": ")) 
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print("Max: " , max_value)
print("Min: " , min_value)






    




