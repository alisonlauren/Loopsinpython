#setting/defining varaible and its set of numbers
numbers = [-10, -20, -30, -40, 10, 20, 30, 40]
#creating a new list which for now, is left blank
new_list = []
#setting a for loop for my variable
for num in numbers:
    # setting condition, if num is greater than 0
    if num > 0:
        #appending or adding the numbers that fit the condition
        new_list.append(num)
#printing my new list of numbers
print(new_list)