import json
import websocket
import datetime
from google.cloud.pubsublite.cloudpubsub import PublisherClient
from google.cloud.pubsublite.types import (
    CloudRegion,
    CloudZone,
    MessageMetadata,
    TopicPath,
)
# projects/780371717407/locations/us-central1/topics/testTopic
# https://cloud.google.com/pubsub/lite/docs/publish-receive-messages-console#pubsublite-quickstart-publisher-python

project_number =780371717407
cloud_region = "asia-southeast1"
zone_id = "a" 
topic_id = "ethbusd-bn-topic"
regional = True

if regional:
    location = CloudRegion(cloud_region)
else:
    location = CloudZone(CloudRegion(cloud_region), zone_id)
print(str(location))

topic_path = TopicPath(project_number, location, topic_id)
print(topic_path)

#https://medium.com/mlearning-ai/how-to-get-live-crypto-data-from-binance-7a5e5ec10de4
# https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams
#================Binance============================
def ws_trades(symbol='ethbusd'): 
    socket = f'wss://stream.binance.com:9443/ws/{symbol}@trade'
    def on_message(wsapp,message):  
        json_message = json.loads(message)
        crypto_date_str=f"{str(datetime.datetime.fromtimestamp(json_message['E']/1000).strftime('%Y-%m-%d %H:%M:%S'))}|{json_message['s']}|{json_message['p']}|{json_message['q']}"
        print(crypto_date_str)
        # PublisherClient() must be used in a `with` block or have __enter__() called before use.
        with PublisherClient() as publisher_client:
            
            api_future = publisher_client.publish(topic_path, crypto_date_str.encode("utf-8"))
            # result() blocks. To resolve API futures asynchronously, use add_done_callback().
            message_id = api_future.result()
            message_metadata = MessageMetadata.decode(message_id)
            print(
                f"Published {symbol} {topic_path} with partition {message_metadata.partition.value} and offset {message_metadata.cursor.offset}."
            )

    def on_error(wsapp,error):
        print(error)

    wsapp = websocket.WebSocketApp(socket, on_message=on_message, on_error=on_error)
    wsapp.run_forever()

ws_trades()

