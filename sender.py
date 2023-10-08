import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

channel.queue_declare(queue='hello')

# Send 10000 messages
for i in range(1000000):
    message = f'Message count: {i+1}'
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent '{message}'")

connection.close()