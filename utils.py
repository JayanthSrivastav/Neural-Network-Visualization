import math

translate_y = 0

def lerp(A, B, t):
    return int(A +(B-A)*t)

def translateY(y):
    return y + translate_y

def translate(y):
    global translate_y
    translate_y = y + 200

def getIntersection(A, B, C, D):
    tTop = (D[0] - C[0]) * (A[1] - C[1]) - (D[1] - C[1]) * (A[0] - C[0])
    uTop = (C[1] - A[1]) * (A[0] - B[0]) - (C[0] - A[0]) * (A[1] - B[1])
    bottom = (D[1] - C[1]) * (B[0] - A[0]) - (D[0] - C[0]) * (B[1] - A[1])

    if bottom != 0:
        t = tTop/bottom
        u = uTop/bottom
        if( t>= 0 and t <= 1  and u >= 0 and u <= 1):
            return [lerp(A[0], B[0], t), lerp(A[1], B[1], t), t]

def polysIntersect(poly1, poly2):
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            touch = getIntersection(poly1[i], poly1[(i+1)%len(poly1)], poly2[j], poly2[(j+1)%len(poly2)])
            if touch:
                return True
    return False

def getRGBA(value):
    alpha = math.fabs(value)
    if value < 0: 
        R = 0
        B = 255
    else: 
        R = 255
        B = 0
    G = R
    # return (int(alpha * 255), int(alpha * 255), int(alpha * 255))
    # return((int(255 - (R - (R * (alpha*255/255)))), int(255 -( G - (G * (alpha*255/255)))), int(255 -(B - (B * (alpha*255/255))))))
    return (int(R - (R * ((1-alpha)*255/255))), int( G - (G * ((1-alpha)*255/255))), int(B - (B * ((1-alpha)*255/255))))
    # if value > 0:
    #     return (255,255,255)
    # else:
    #     return( 0,0,0)
    # return (int(R), int(G), int(B))