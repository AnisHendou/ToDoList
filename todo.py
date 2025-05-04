Exit=False
prompt =0
while(!Exit ):
    print("chose one of the options : ")
    print("1 -> add a task. ")
    print("2 -> remove the task.")
    print("3-> show all tasks ")
    print("4 -> delete a task " ) 
    print("5-> modify a task ")

    while ( prompt >5 or prompt<1 ) :
        def get_number_input (prompt):  
                while True:
                    input = input(prompt)
                    try:
                        return int(input)
                    except ValueError:
                        print("please give a valid number . /the number should be between 1 to 5 /")
                        
        


    
                        
                         



      