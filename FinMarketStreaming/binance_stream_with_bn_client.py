#https://gist.github.com/mayank311996/3d19f9af499c01f57fda6b2f9615a8b5
# https://python-binance.readthedocs.io/en/latest/websockets.html#websockets
# https://python-binance.readthedocs.io/en/latest/binance.html?highlight=trade_socket#binance.streams.BinanceSocketManager.trade_socket
"""
Websockets
There are 2 ways to interact with websockets, you can choose ThreadedWebsocketManager or BinanceSocketManager.
"""

from binance.client import Client
from dotenv import dotenv_values
import asyncio
from binance import AsyncClient, BinanceSocketManager
import datetime
# path_config=r'D:\AB_DB\Script_ImportData'
# # Loading keys from config file
# config_values= dotenv_values(dotenv_path=f'{path_config}\\.env')
# api_key = config_values['bn_key']
# api_secret =config_values['bn_secrete']
# client=Client(api_key,api_secret)




async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e a trade socket
    ts = bm.trade_socket('ETHBUSD')
    # then start receiving messages
    async with ts as tscm:
        while True:
                json_message = await tscm.recv()
                date_time = datetime.datetime.fromtimestamp(json_message['E']/1000).strftime('%Y-%m-%d %H:%M:%S')
                print("SYMBOL: "+json_message['s'])
                print("PRICE: "+json_message['p'])
                print("QTY: "+json_message['q'])
                print("TIMESTAMP: " + str(date_time))
                print("-----------------------------------------------------")

    await client.close_connection()

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())