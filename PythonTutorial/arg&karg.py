def super_func(name, *args,i='hi', **kwargs):
    total = 0
    for items in kwargs.value():
        total +=      items
    return sum(args) + total


print(super_func('andy',1,2,3,4,5, num1=5, num2=10))

#Rule: params, *arg, default, parameters, **kwargs