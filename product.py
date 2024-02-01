import getpass
import mysql.connector

class Product:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()


    def create_table_product(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS product (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                description TEXT,
                price INT,
                quantity INT,
                id_category INT
            )
        ''')


    def add_product(self,name,description,price,quantity,id_category):
        sql_query = "INSERT INTO product (name,description,price,quantity,id_category) VALUES (%s,%s,%s,%s,%s)"
        values = (name,description,price,quantity,id_category)
        self.cursor.execute(sql_query, values)
        self.conn.commit()



    def del_product(self,id):
        self.cursor.execute(f"DELETE FROM product WHERE id = {id}")
        self.conn.commit()


    def read_produit(self):
        sql_query = "SELECT * FROM product"
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()
        return result

    def update_product(self, name, description, price, quantity, id_category, id):
        sql_query = "UPDATE product SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s WHERE id=%s"
        values = (name, description, price, quantity, id_category, id)
        self.cursor.execute(sql_query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


    def return_conn(self):
        return self.conn


'''user = getpass.getpass('Entrez votre nom user  : ')
mdp = getpass.getpass('Entrez votre mdp  : ')

produit = Product(host='localhost', user=user, password=mdp, database='store')

produit.create_table_product()

produit.add_product("Pâte","C'est des pâte achete",2,5,4)


print(produit.read_produit())

produit.close_connection()
'''



#------------------------------------------!!!!!!!!!!!!-----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#------------------------------------------!!!!!!!!!!!!-----------------------------------------------------


#AJOUTER LES DONNER DANS UN FICHIER TEXT PUIS LES BLIT --> read_produit 
#Passer par des input pour le del/add