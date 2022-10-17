money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


def month_living(money_capital, salary, spend, increase):
    month = 0
    condition = True
    beginning_budget = money_capital
    while condition == True:
        delta = salary - spend * ((1 + increase)**(month))
        beginning_budget = beginning_budget + delta
        if beginning_budget > 0:
            month += 1
        else:
            condition = False
    print(month)

month_living(money_capital, salary, spend, increase)


