import math

pointA = [37.20553540890865,-89.98048343749997]
pointB = [37.79155875890545,-90.56378879638669]

LatA = math.radians(pointA[0] ) 
LongA = math.radians(pointA[1])   

LatB = math.radians( pointB[0] ) 
LongB = math.radians( pointB[1] ) 

def getDirection(LatA,LongA,LatB,LongB):
    Long = LongB - LongA
    X = math.cos(LatB) * math.sin(Long)
    Y = (math.cos(LatA) * math.sin(LatB))-(math.sin(LatA)* math.cos(LatB) * math.cos(Long))
    # print("LatA: ",LatA)
    # print("LongA: ",LongA)
    # print("LatB: ",LatB)
    # print("LongB: ",LongB)
    # print("x: ",X)
    # print("y: ",Y)
    Be =math.degrees(math.atan2(X,Y))
    # print('Bearing Angle : ',Be)
    if Be == 0 :
        return ("North")
    elif 0 < Be < 90:
        return("NorthEast")
    elif Be == 90:
        return("East")
    elif 90 < Be < 180:
        return("SouthEast")  
    elif Be == 180:
        return("South")
    elif -90 > Be > -180:
        return("SouthWest") 
    elif Be == -90:
        return("West")
    elif 0 > Be > -90:
        return("NorthWest")
    else:
        return 'Not a valid location' 

finalDirection = getDirection(LatA,LongA,LatB,LongB)
print(finalDirection)