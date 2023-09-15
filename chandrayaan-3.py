
Directions={"N":["W","E"],"W":["S","N"],"S":["E","W"],"E":["N","S"],"U":["N","S"],"D":["W","E"]} # LEFT AND RIGHT FOR EACH DIRECTION
Initial_Direction=input() # take input - INTIAL DIRECTION
commands=[str(i) for i in input().split()] # TAKE INPUT COMMANDS

Starting_Position=[0,0,0]
final_position=Starting_Position
final_direction=Initial_Direction

for i in commands:
    if i=="l":
        final_direction=Directions[final_direction][0]
    elif i=="r":
        final_direction=Directions[final_direction][1]
    elif i=="u":
        final_direction="U"
    elif i=="d":
        final_direction="D"
    
    else:
        if i=="f":
            if final_direction=="N":
                final_position[1]+=1
            elif final_direction=="S":
                final_position[1]-=1
            elif final_direction=="E":
                final_position[0]+=1
            elif final_direction=="W":
                final_position[0]-=1
            elif final_direction=="U":
                final_position[2]+=1
            elif final_direction=="D":
                final_position[2]-=1
        elif i=="b":
            if final_direction=="N":
                final_position[1]-=1
            elif final_direction=="S":
                final_position[1]+=1
            elif final_direction=="E":
                final_position[0]-=1
            elif final_direction=="W":
                final_position[0]+=1
            elif final_direction=="U":
                final_position[2]-=1
            elif final_direction=="D":
                final_position[2]+=1
print("Final Direction is: ",final_direction)
print("Final Position is: ",final_position)
