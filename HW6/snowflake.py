"""Draws a snowflake shape."""

from turtle import *

def snowflake(length, depth, branchno=6):
    """Draws a snowflake shape with branches going to
    a given depth.
    """
    # local auxiliary function that draws one branch:
    def branch(length, depth):
        """One branch only"""
        if depth == 0:
            return    # base case
        else:
            width(depth)
            forward(length)
            branch(length/2, depth-1)  # forward
            backward(length*1/3)
            left(60)
            branch(length/3, depth-1)  # left
            right(120)
            branch(length/3, depth-1)  # right
            left(60)
            # leave turtle facing the original direction
            backward(length*2/3)
            
    # draw 6 symmetric branches.
    #   -- illustates how to use recursion to do a loop:
    if branchno > 0:
        branch(length, depth)

        # "tail recursion":
        snowflake(length, depth, branchno - 1)
    

clearscreen()
delay(0)
snowflake(160, 5)
