from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from django.utils import timezone

class MyConsumer(WebsocketConsumer):

    def connect(self):
        self.id = self.scope['url_route']['kwargs']['room_id'].strip() #Es muy importante eliminar los espacios porque si no vamos a tener error al conectarse el socket 
        self.room_group_name = 'sala_chat_%s' % self.id.replace(' ', '_')  #Igual aqui
        self.user = self.scope['user']

        print("PILLE PUES ÑERO " + self.room_group_name)
        print("Conexión hecha, channel_name: " + self.channel_name)

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()

    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            # Obtener el id de quien manda el mensaje.
            if self.scope['user'].is_authenticated:
                sender_id = self.scope['user'].id
            else:
                sender_id = None

            if sender_id:
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': message,
                        'username': self.user.username,
                        'datetime': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S'),
                        'sender_id': sender_id
                    }
                )
        except json.JSONDecodeError as e:
            print('Problemas decodificando el JSON: ', e)
        except KeyError as e:
            print('Falta una clave en el JSON: ', e)
        except Exception as e:
            print('Error inesperado: ', e)

    def chat_message(self, event):
        message = event['message']
        username = event['username']
        datetime = event['datetime']
        sender_id = event['sender_id']

        current_user_id = self.scope['user'].id

        if sender_id != current_user_id:
            self.send(text_data=json.dumps({
                'message': message,
                'username': username,
                'datetime': datetime
            }))

    def disconnect(self, close_code):
        print('Desconectado')
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

