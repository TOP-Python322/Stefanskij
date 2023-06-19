def countable_nouns(num:"int", *nouns:"tuple[str,str,str]")-> "str":
# Chooses correct form of noun
    str_num = str(num)
    noun_list = list(*nouns)
    
    if str_num[-1] == "1":
        print(noun_list[0])
    elif str_num[-1] == "2" or str_num[-1] == "3" or str_num[-1] == "4":
        print(noun_list[1])
    else:
        print(noun_list[2])


countable_nouns(4255653, ("год", "года", "лет"))