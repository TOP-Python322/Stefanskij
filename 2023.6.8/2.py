def taxi_cost(distance:"int",time = 0)-> "int":
# Show cost of taxi
    base = 80
    if distance >= 150:    
        step = distance // 150
        cost = base + step * 6 + time * 3
        print(cost)
    elif 0 < distance < 150:
        cost = base + time * 3
        print(cost)
    elif distance == 0:
        canceled = True
        cost = base * 2 + time * 3
        print(cost)
    else:
        print(None)

taxi_cost(450, 2)
