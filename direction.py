import math

pointA = [37.20553540890865,-89.98048343749997]
pointB = [37.71481966440855,-89.45142307373044]

LatA = math.radians(pointA[0] ) 
LongA = math.radians(pointA[1])   

LatB = math.radians( pointB[0] ) 
LongB = math.radians( pointB[1] ) 

def getDirection(LatA,LongA,LatB,LongB):
    Long = LongB - LongA
    X = math.cos(LatB) * math.sin(Long)
    Y = (math.cos(LatA) * math.sin(LatB))-(math.sin(LatA)* math.cos(LatB) * math.cos(Long))
    Be =math.degrees(math.atan2(X,Y))
    #Be = Bearer angle
    if Be == 0 :
        return 'North'
    elif 0 < Be < 45:
        return 'NorthNorthEast'
    elif Be == 45:
        return 'NorthEast'
    elif 45 < Be < 90:
        return 'NorthEastEast'
    elif Be == 90:
        return 'East'
    elif 90 < Be < 135:
        return 'SouthEastEast' 
    elif Be == 135:
        return 'SouthEast' 
    elif 135 < Be < 180:
        return 'SouthSouthEast'  
    elif Be == 180:
        return 'South'
    elif -135 > Be > -180:
        return 'SouthSouthWest'
    elif Be == -135:
        return 'SouthWest'
    elif -90 > Be > -135:
        return 'SouthWestWest'   
    elif Be == -90:
        return 'West'
    elif 0 > Be > -45:
        return 'NorthNorthWest'
    elif Be == -45:
        return 'NorthWest'  
    elif -45 > Be > -90:
        return 'NorthWestWest' 
    else:
        return 'Not a valid location' 

finalDirection = getDirection(LatA,LongA,LatB,LongB)
print(finalDirection)