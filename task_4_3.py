import requests
from decimal import Decimal
import datetime


def currency_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.text
    content_list = content.split('</NumCode><CharCode>')
    currency_dict = {}

    the_date = content_list[0].split('Date="')[1].partition('"')[0]
    the_date = datetime.date(int(the_date.split('.')[2]), int(the_date.split('.')[1]), int(the_date.split('.')[0]))
    currency_dict['Date'] = the_date

    for el in content_list[1:]:
        valuta, nominal, name_cur, value, *num_code = el.split('</')
        nominal = Decimal(nominal.rpartition('>')[2])
        value = Decimal(value.rpartition('>')[2].replace(',', '.')) / nominal
        currency_dict[valuta] = value
    return f'{currency_dict.get(currency.upper())}, {currency_dict.get("Date")}' if currency_dict.get(
        currency.upper()) else None


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('EUR'))
