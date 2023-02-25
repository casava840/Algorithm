def solution(brown, yellow):
    a = (brown+4)/2 #x+y
    b = brown + yellow #x*y
    y = (a-(a**2-4*b)**(1/2))/2
    x = b/y
    if x<y:
        x,y = y,x
    return [x,y]