# how lambda works

mylambda = lambda x: x[0] + x[-1] 
print(mylambda("Oh Hi Mark!")) # O!

#---------------------------------------------

def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x
    
# lambda converted result
myf_unction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x



# lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]


