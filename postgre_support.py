import psycopg2

class PostgreSupport:
    def __init__(self, user="serg",
                 password="aiWgIDHKPdHr",
                 host="localhost",
                 port="5432",
                 database="OTUS",
                 ):
        self.connection = None
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def __del__(self):
        if self.connection:
            self.connection.close()
            print("Соединение с PostgreSQL закрыто")

    def connect_db(self):
        try:
            self.connection = psycopg2.connect(user=self.user,
                                               password=self.password,
                                               host=self.host,
                                               port=self.port,
                                               dbname=self.database
                                               )
            print("Соединение с PostgreSQL открыто")
            return True
        except(Exception, psycopg2.Error) as error:
            print("Ошибка соединения с PostgreSQL:", error)
            return False


    def add_user_post(self, **user_data):
        if self.connection is not None:
            cursor = self.connection.cursor()
            try:
                cursor.execute(
                    'INSERT INTO users_posts (id_user, post) VALUES (%s, %s)',
                    (user_data['id_user'], user_data['post']))
                self.connection.commit()
            except (Exception, psycopg2.Error) as error2:
                print(f"Не удалось вставить {user_data['id_user'], user_data['post']}: ", error2)
            finally:
                cursor.close()
            return 0
