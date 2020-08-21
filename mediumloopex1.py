letter_change = ( ('A', '4'), ('E','3'), ('G','6'), ('I','1'),
                 ('O','0'), ('S','5'), ('T','7') )
my_string = "i am an elite hacker."
new_string = my_string.upper()
for old, new in letter_change:
    new_string = new_string.replace(old, new)

print ( new_string )