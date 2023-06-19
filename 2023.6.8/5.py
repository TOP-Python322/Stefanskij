def central_tendency(num1:"float",num2:"float", *numbers:"tuple[float,float,float]")->"dict[str:float]":
# Finds some math parameters in definite numbers
    num_list = list(numbers)
    total = [num1, num2] + num_list
    
    med = (max(total) + 1)/2
    arith = (num1 + num2 + sum(num_list))/len(total)
    
    result = 1
    for number in num_list:
        result *= number
    geom = (num1 * num2 * result)**(1/len(total))
   
    summ = 0
    for number in total:
        summ += 1/number
    harm = len(total)/summ
    
    math_dict = {"median": med, "arithmetic": arith, "geometric": geom, "harmonic":harm}
    print(math_dict)
    
central_tendency(1, 2.3, 3.1, 4, 5, 6.6)