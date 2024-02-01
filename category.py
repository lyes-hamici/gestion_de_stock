import getpass
import mysql.connector

class Category:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()


    def create_table_category(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS category (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255)
            )
        ''')


    def add_category(self,name):
        sql_query = "INSERT INTO category (name) VALUES (%s)"
        values = (name,)
        self.cursor.execute(sql_query, values)
        self.conn.commit()



    def del_category(self,id):
        self.cursor.execute(f"DELETE FROM category WHERE id = {id}")
        self.conn.commit()


    def read_produit(self):
        sql_query = "SELECT * FROM category"
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()
        return result       

    def update_category(self,name):
        sql_query = "UPDATE category SET name=%s"
        values = (name)
        self.cursor.execute(sql_query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()



'''user = getpass.getpass('Entrez votre nom user  : ')
mdp = getpass.getpass('Entrez votre mdp  : ')

produit = Category(host='localhost', user=user, password=mdp, database='store')

produit.create_table_category()
print(produit.read_produit())

produit.close_connection()'''
