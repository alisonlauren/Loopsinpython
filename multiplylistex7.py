#setting/defining my variable and its list of numbers
number_list = [11, 54, 67, 12, 9, 77]
#printing an f string for just extra information
print(f"Here's my number list {number_list}, I'll multiply them all by 4.")
#setting the variable and my factor number
choosen_fact = 4
#setting my variable empty
multiplied_numbers = []
#setting a for loop relevant to my number_list variable previously stated
for num in number_list:
    #bringing back in my new variable and multiply the number and choosen factor of 4
    multiplied_numbers.append(num * choosen_fact)
#printing my variable, now multiplied with 4
print(multiplied_numbers)