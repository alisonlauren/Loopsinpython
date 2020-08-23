#greeting statement
print("Hello! Need help creating a grocery list? I'm here to help. Let's get started.")
#setting my list as an empty string
g_list = []


#creating my while statement, setting the condition as always true
while True:
#creating input for user
    user_option = input("Would you like to add, remove or finish?: ")
    break
#second while statement
while True:
#my first if statement, which is relevant when user_option or user_pick is called
        if  user_option or user_pick == "add" :
            #setting variable item_input and calling user to add another item
            item_input = input("Add: ")
            #appending item_input to general grocery list
            g_list.append(item_input)
            #printing my grocery list so users can see where they're at
            print(g_list)
            #checking in each time if they'd like to add remove or finish
            user_pick = input("add, remove or finish?: ")
             #second if statement, relevant when the user inputs remove
        if  user_pick == "remove":
            #printing their current list
            print(g_list)
            #remove the input, ensuring its an int
            remove_input = int(input("Okay, which item would you like to remove?: "))
            #deleting from grocery list and removing input selected. using -1 so the user wont
            #have to understand that computers like to start their list at 0
            del g_list[remove_input-1]
            #printing string along with new grocery list
            print(f'Here is your new list {g_list}')
            #asking again, add, remove or finish
            user_pick =  input("add, remove or finish?: ")

            #giving the option for the user to choose finish
        if  user_pick == "finish":
            #printing string along with grocery list
            print(f'Head to the store now, and bring this list with you: {g_list}')
            #breaking, with the assumption the use is no longer relevant
            break
        #and now if they don't choose any relevant options, it will say sorry we dont understand
        #and it will jump to the top with add: again
        elif user_pick != "add" and user_pick != "remove" and user_pick != "finish":
            print("Sorry, we don't understand.")
            

       


    
            
                
        
        
            
            




        


            








    
  

        
