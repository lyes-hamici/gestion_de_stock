from category import Category
from product import Product
import getpass
from tkinter import *
from tkinter.ttk import *
class PyMysql:
    def __init__(self):
        self.user = getpass.getpass('Entrez votre nom user  : ')
        self.mdp = getpass.getpass('Entrez votre mdp  : ')
        self.prod = Product(host='localhost', user=self.user, password=self.mdp, database='store')
        self.categ = Category(host='localhost', user=self.user, password=self.mdp, database='store')



    # fenêtre principale
        
    def main_page(self):

        fenetre = Tk()

        fenetre.title('Manage Produit')

            

        # libellé

        libelle = Label(fenetre, text = 'Produit')

        libelle.pack(padx = 10, pady = 10)

    

        #tableau

        tableau = Treeview(fenetre, columns=('id', 'name','description' ,'price','quantity','id_category','category'))

        tableau.heading('id', text='Id')

        tableau.heading('name', text='Name')

        tableau.heading('description', text='Description')

        tableau.heading('price', text='Price')

        tableau.heading('quantity', text='Quantity')

        tableau.heading('id_category', text='Id_category')

        tableau.heading('category',text='category')

        tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert

        tableau.pack(padx = 10, pady = (0, 10))

        

        # bouton pour terminer le programme

        bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

        bouton_terminer.pack(padx = 10, pady = (0, 10))

        

        

        # lecture et affichage des données
        if len(self.prod.read_produit_with_categ()):

            for enreg in self.prod.read_produit_with_categ():


                tableau.insert('', 'end', iid=enreg[0], values=(enreg[0],enreg[1], enreg[2], enreg[3],enreg[4],enreg[5],enreg[6]))

        else:

            libelle.configure(text = 'Il n\'y a présentement aucun produit.')

            tableau.pack_forget()

        
        bouton_add = Button(fenetre, text = 'Add product', command = self.add_page)

        bouton_add.pack(padx = 10, pady = (0, 10))

        bouton_del = Button(fenetre, text = 'Del Product', command = self.del_page)

        bouton_del.pack(padx = 10, pady = (0, 10))


        bouton_update = Button(fenetre, text = 'Update Product', command = self.update_page)

        bouton_update.pack(padx = 10, pady = (0, 10))


        fenetre.mainloop()



    def add_page(self):
        fenetre = Tk()

        fenetre.title('Add Produit')

            

        # libellé

        libelle = Label(fenetre, text = 'Add Produit')

        libelle.pack(padx = 10, pady = 10)

        Label(fenetre, text="Enter Name", font=('Calibri 10')).pack()
        self.name = Entry(fenetre)
        self.name.pack()
        
        Label(fenetre, text="Enter description", font=('Calibri 10')).pack()
        self.description = Entry(fenetre)
        self.description.pack()
        
        Label(fenetre, text="Enter price", font=('Calibri 10')).pack()
        self.price = Entry(fenetre)
        self.price.pack()
        

        Label(fenetre, text="Enter quantity", font=('Calibri 10')).pack()
        self.quantity = Entry(fenetre)
        self.quantity.pack()
        
        

        
        Label(fenetre, text="Enter id_category", font=('Calibri 10')).pack()
        self.id_category = Entry(fenetre)
        self.id_category.pack()
        

       


        bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

        bouton_terminer.pack(padx = 10, pady = (0, 10))

        bouton=Button(fenetre, text="Ajout Article", command=self.add)
        bouton.pack(side=TOP, padx=50, pady=10)

         
        fenetre.mainloop()



    def add(self):
        name = self.name.get()
        description = self.description.get()
        price = self.price.get()
        quantity = self.quantity.get()
        id_category = self.id_category.get()

        self.prod.add_product(name,description,price,quantity,id_category)



    def del_page(self):
        fenetre = Tk()

        fenetre.title('Del Produit')

            

        # libellé

        libelle = Label(fenetre, text = 'Del Produit')

        libelle.pack(padx = 10, pady = 10)

        Label(fenetre, text="Remove id", font=('Calibri 10')).pack()
        self.id = Entry(fenetre)
        self.id.pack()


        bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

        bouton_terminer.pack(padx = 10, pady = (0, 10))

        bouton=Button(fenetre, text="Del Produit", command=self.del_prod)
        bouton.pack(side=TOP, padx=50, pady=10)

         
        fenetre.mainloop()



    def del_prod(self):
        id = self.id.get()
        self.prod.del_product(id)




    def update_page(self):
        fenetre = Tk()

        fenetre.title('Del Produit')

            

        # libellé

        libelle = Label(fenetre, text = 'Del Produit')

        libelle.pack(padx = 10, pady = 10)

        Label(fenetre, text="Update id", font=('Calibri 10')).pack()
        self.id = Entry(fenetre)
        self.id.pack()


        Label(fenetre, text="Enter New Name", font=('Calibri 10')).pack()
        self.name = Entry(fenetre)
        self.name.pack()
        
        Label(fenetre, text="Enter New  description", font=('Calibri 10')).pack()
        self.description = Entry(fenetre)
        self.description.pack()
        
        Label(fenetre, text="Enter New price", font=('Calibri 10')).pack()
        self.price = Entry(fenetre)
        self.price.pack()
        

        Label(fenetre, text="Enter New quantity", font=('Calibri 10')).pack()
        self.quantity = Entry(fenetre)
        self.quantity.pack()
        
        

        
        Label(fenetre, text="Enter New id_category", font=('Calibri 10')).pack()
        self.id_category = Entry(fenetre)
        self.id_category.pack()


        bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

        bouton_terminer.pack(padx = 10, pady = (0, 10))

        bouton=Button(fenetre, text="Update Produit", command=self.update_prod)
        bouton.pack(side=TOP, padx=50, pady=10)

         
        fenetre.mainloop()



    def update_prod(self):
        id = int(self.id.get())
        name = self.name.get()
        description = self.description.get()
        price = int(self.price.get())
        quantity = int(self.quantity.get())
        id_category = int(self.id_category.get())
        self.prod.update_product(name,description,price,quantity,id_category,id)





        

