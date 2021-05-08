def IR(salary: int):
    ret = 0
    if salary > 1000 and salary <= 2000:
        ret = ret + (salary - 1000.0) * (0.15)
    if salary > 2000:
        ret = ret + 150 + (salary - 2000.0) * (0.20)
    if salary > 3000:
        ret = ret + (salary - 3000.0) * (0.05)
    return ret