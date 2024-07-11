def calculator():

    statement = input("Enter numbers and operatores(+, -, /, *) using spaces only\n : ").strip()
    
    lis = statement.split(" ")
    
    while len(lis) > 1:
        if '/' in lis:
            item = '/'
            item_index = lis.index(item)
            num1 = float(lis[item_index - 1] )  
            num2 = float(lis[item_index + 1] )
            
            new_num = float(num1 / num2)
            lis[lis.index('/')] = new_num
            lis.remove(lis[lis.index(new_num) - 1 ])
            lis.remove(lis[lis.index(new_num) + 1 ])
    
        elif '*' in lis:
            item = '*'
            item_index = lis.index(item)
            num1 = float(lis[item_index - 1] )  
            num2 = float(lis[item_index + 1] )
            
            new_num = float(num1 * num2)
            lis[lis.index('*')] = new_num
            lis.remove(lis[lis.index(new_num) - 1 ])
            lis.remove(lis[lis.index(new_num) + 1 ])
            
        elif '+' in lis:
            item = '+'
            item_index = lis.index(item)
            num1 = float(lis[item_index - 1] )  
            num2 = float(lis[item_index + 1] )
            
            new_num = float(num1 + num2)
            lis[lis.index( '+')] = new_num
            lis.remove(lis[lis.index(new_num) - 1 ])
            lis.remove(lis[lis.index(new_num) + 1 ])
            
        elif '-' in lis:
            item = '-' 
            item_index = lis.index(item)
            num1 = float(lis[item_index - 1] )  
            num2 = float(lis[item_index + 1] )
            
            new_num = float(num1 - num2)
            lis[lis.index('-' )] = new_num
            lis.remove(lis[lis.index(new_num) - 1 ])
            lis.remove(lis[lis.index(new_num) + 1 ])
    
    result = lis[0]
     
    print(f"Result: {result}")

    calulate_again = input("Do you want to continue? (yes or no): ").lower()
    if calulate_again == "yes":
        calculator()

calculator()