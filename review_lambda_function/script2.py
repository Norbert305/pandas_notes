

# Let's convert our battle city function into a lambda function


def age(x):
    if x >= 13:
        return "Welcome to BattleCity!"
    else:
        return "You must be 13 or older"
        
print(age(5))


my_lambda = lambda x : "Welcome to BattleCity" if x >= 13 else "You must be 13 or older"


print(my_lambda(14))


# remember --->   lambda x: [outcome if true] if [conditional] else [outcome if false]


   
   
