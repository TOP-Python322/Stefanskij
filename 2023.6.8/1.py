def strong_password(password: "str")-> "bool":
 #   Checks difficulty of password
    if len(password) >= 8:
        test1 = True    
    else:
        test1 = False
        
    if password.islower():
        test2 = False
    else: 
        test2 = True  
    
    if password.isalnum():
        test3  = False
    else:
        test3 = True
    
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]    
    num_pas = []
    
    for nums in password:
        if nums in numbers:
            num_pas.append(nums)
            
    if len(num_pas) >= 2:
        test4 = True
    else:
        test4 = False
        
    if test1 == True and test2 == True and test3 == True and test4 == True:
        print(True)
    else:
        print(False)
        
           
        
strong_password(password = "rewekiwr%60wQWts_us")        