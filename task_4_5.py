from task_4_3 import currency_rates
import sys

try:
    print(currency_rates(sys.argv[1]))

except IndexError:
    print(currency_rates('usd'))
    print(currency_rates('EUR'))
