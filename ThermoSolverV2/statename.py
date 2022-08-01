from initialise import numberofstates
def adjstates(i):
    if i == numberofstates - 1:  # Here I make a counting system that allows us to compare with similar states
        nextstate = 0
    else:
        nextstate = i + 1
    if i == 0:
        prevstate = numberofstates - 1
    else:
        prevstate = i - 1
    return nextstate,prevstate