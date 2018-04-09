#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('sensu', 'password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.131.50',virtual_host='/sensu',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='prueba')
print(" [x] Sent 'Hello World!'")
connection.close()
