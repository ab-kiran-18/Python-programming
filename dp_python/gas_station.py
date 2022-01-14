def gas_station(gas,cost):
    dif = 0
    for i in range(len(gas)):
        dif += gas[i] - cost[i]

    if dif < 0:
        return -1
    else:
        tank,start = 0,0
        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start

cost = list(map(int,input("enter values of gas array:").split()))
gas = list(map(int,input("enter cost array:").split()))
print(gas_station(gas, cost))