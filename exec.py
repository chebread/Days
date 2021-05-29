# N 월에 며칠까지 있는지 확인해요
import sys
import calendar as clnd
def Input():
    month = sys.argv[1]
    return int(month)
def Days(m):
    month = clnd.monthrange(2021, m)
    return month[1]
def Scope(m):
    if m > 12 or m < 1:
        print(-1)
        return exit()
month = Input()
Scope(month)
print(Days(month))