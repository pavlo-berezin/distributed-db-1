import psycopg2
from random import randint

account_connection = psycopg2.connect("dbname=account")
fly_connection = psycopg2.connect("dbname=fly")
hotel_connection = psycopg2.connect("dbname=hotel")

id = randint(0, 10000)

account_connection.tpc_begin(account_connection.xid(id, 'transaction ID', 'connection 1'))
fly_connection.tpc_begin(fly_connection.xid(id, 'transaction ID', 'connection 2'))
hotel_connection.tpc_begin(hotel_connection.xid(id, 'transaction ID', 'connection 3'))

account_cursor = account_connection.cursor()
fly_cursor = fly_connection.cursor()
hotel_cursor = hotel_connection.cursor()

fly_cursor.execute("INSERT INTO booking (client_name,fly_number, fly_from, fly_to, fly_date) VALUES ('Nik', %s, 'NYC', 'LAC', '03/05/2020')", (str(randint(0, 100)),))
hotel_cursor.execute("INSERT INTO booking (client_name,hotel_name, arrival, departure) VALUES ('Nik', 'LAC', '2020-03-05', '2020-03-07')")
account_cursor.execute("UPDATE account SET amount=amount - 100 WHERE client_name='Nik'")

try:
  print('try')
  account_connection.tpc_prepare()
  fly_connection.tpc_prepare()
  hotel_connection.tpc_prepare()
except psycopg2.DatabaseError as e:
  print('error', e)
  account_connection.tpc_rollback()
  fly_connection.tpc_rollback()
  hotel_connection.tpc_rollback()
else:
  print('ok')
  account_connection.tpc_commit()
  fly_connection.tpc_commit()
  hotel_connection.tpc_commit()