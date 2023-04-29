translate_y = 0

def lerp(A, B, t):
    return int(A +(B-A)*t)

def translateY(y):
    return y + translate_y

def translate(y):
    global translate_y
    translate_y = y + 280