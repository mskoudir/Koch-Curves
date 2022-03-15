from turtle import *
def curve ( n, m ) :
    if n == 0: 
        return forward(m)
    else:
            curve (n-1 ,m)
            left(60)
            curve (n-1 ,m)
            right(120)
            curve (n-1 ,m)
            left(60)
            curve (n-1 ,m)
