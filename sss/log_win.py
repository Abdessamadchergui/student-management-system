
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

from conn_myql

cursor = conn.cursor()

class ShopManagementSystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Shop Management System")
        self.window.geometry('639x360')
        self.window.resizable(False, False)

        # Load background image
        self.bg_image = PhotoImage(file)
        self.canvas = tk.Canvas(self.window, width=700, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bg_image)

        # Labels and Entries
        self.name_label = tk.Label(self.window, text="Product Name:")
        self.name_label.place(x=50, y=100)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.place(x=200, y=100)

        self.price_label = tk.Label(self.window, text="Price:")
        self.price_label.place(x=50, y=150)
        self.price_entry = tk.Entry(self.window)
        self.price_entry.place(x=200, y=150)

        self.quantity_label = tk.Label(self.window, text="Quantity:")
        self.quantity_label.place(x=50, y=200)
        self.quantity_entry = tk.Entry(self.window)
        self.quantity_entry.place(x=200, y=200)

        # Buttons
        self.add_button = tk.Button(self.window, text="Add Product", command=self.add_product)
        self.add_button.place(x=200, y=250)

        self.view_button = tk.Button(self.window, text="View Products", command=self.view_products)
        self.view_button.place(x=300, y=250)

        self.window.mainloop()

    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()

        if name and price and quantity:
            try:
                price = float(price)
                quantity = int(quantity)
                # Assuming you have a 'products' table in your database
                query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
                data = (name, price, quantity)
                cursor.execute(query, data)
                conn.commit()
                messagebox.showinfo("Success", "Product added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Price and quantity must be numeric!")
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

    def view_products(self):
        # Assuming you have a 'products' table in your database
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()
        if products:
            for idx, product in enumerate(products, start=1):
                messagebox.showinfo("Product {}".format(idx), "Name: {}\nPrice: {}\nQuantity: {}".format(*product))
        else:
            messagebox.showinfo("No Products", "No products available.")

if __name__ == "__main__":
    ShopManagementSystem()
