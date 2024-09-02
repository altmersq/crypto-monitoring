import aiohttp


async def get_top_10_crypto():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            sorted_pairs = sorted(data, key=lambda x: float(x['quoteVolume']), reverse=True)
            top_10_symbols = [pair['symbol'] for pair in sorted_pairs if pair['symbol'].endswith('USDT')][:10]
            print(top_10_symbols)
            return top_10_symbols


async def get_price_change_last_hour(symbol):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit=2"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            if len(data) >= 2:
                previous_close = float(data[0][4])
                current_close = float(data[1][4])

                change_percent = ((current_close - previous_close) / previous_close) * 100
                return change_percent
            else:
                return None
