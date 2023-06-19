def base_decimal(num_str:"str",base:"int")->"int":
# Calculates in decimal system
    global dec_num
    if base == 2:
        dec_num = int(num_str, 2)
    elif base == 8:    
        dec_num = int(num_str, 8)
    elif base == 16:    
        dec_num = int(num_str, 16)
        
base_decimal("010", 16)         

def other_base(dec_num:"int", base:"int")->"int":
# Calculates in other systems
    if base == 2:
        new_num = bin(dec_num)
        print(new_num)
    elif base == 8:
        new_num = oct(dec_num)
        print(new_num)
    elif base == 16:
        new_num = hex(dec_num)
        print(new_num)    
            
other_base(dec_num, 2)


