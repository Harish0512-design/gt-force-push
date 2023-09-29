def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def floor_div(a,b):
    return a//b

def calculate_profit(cp,sp):
    res = sub(sp,cp)
    if res > 0:
        return f"profit is {res}"
    else:
        return f"loss is {res}"

def calculate_profit_percentage(profit,cp):
    return (profit//cp)*100
