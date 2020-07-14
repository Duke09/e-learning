import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # accpet connection
        self.accept()

    def disconnect(self, close_code):
        pass

    # receive message from websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mesage = text_data_json['message']
        # send message to websocket
        self.send(text_data=json.dumps(
            {'message': mesage}
        ))