from drivers import History

exhanges = ['binance', 'bittrex']
ohlc = ['1h',]

history = History()

# for i in exhanges:
#     for j in ohlc:
#         history.update_ohlc(i, j, ['BTC/USDT'])

for i in history.exchanges():
    markets = history.exchange_symbols(i)
    print('binance', markets)

symbol =  history.get_symbol('binance', 'BTC/USDT')
print(symbol['ohlc']['1h'].tail())

