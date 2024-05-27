from datetime import datetime, timedelta
import platform
import aiohttp
import asyncio
import sys


def get_currency_data(data, currency_list):
    result = {}
    result[data["date"]] = {}

    list_currency = ["EUR", "USD"]

    for cur in currency_list:
        list_currency.append(cur.upper())

    for rate in data["exchangeRate"]:
        if rate["currency"] in list_currency:
            result[data["date"]][rate["currency"]] = {
                "sale": rate.get("saleRate", rate.get("saleRateNB")),
                "purchase": rate.get("purchaseRate", rate.get("purchaseRateNB")),
            }
    return result


async def main():

    start_date = datetime.now().date()
    numb_day = int(sys.argv[1])

    async with aiohttp.ClientSession() as session:
        if numb_day <= 10:
            return_list = []
            for i in range(numb_day):
                current_date = start_date - timedelta(days=i)
                date_str = current_date.strftime("%d.%m.%Y")

                url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date_str}"
                async with session.get(url) as response:
                    # print(f"Status: {response.status}")
                    # print(f"Content-type: {response.headers['content-type']}")
                    # print(f"Cookies: {response.cookies}")
                    # print(response.ok)

                    result = await response.json()

                    return_list.append(result)
            return return_list


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    for i in r:
        print(get_currency_data(i, (sys.argv[2:])))
