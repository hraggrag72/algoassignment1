# Hrag Ayntabli
# 100894158
# Algorithms and Data Structures
# Assignment 1

import time
products = []

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.id:^10}{self.name:^20}{self.price:^10.2f}{self.category:^20}"

def insert_product(id, name, price, category):
    products.append(Product(id, name, price, category))

# Load product data
def load_product_data(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            id, name, price, category = line.strip().split(',')
            insert_product(int(id), name, float(price), category)

# Sort products by price using Bubble Sort
def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j].price > products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]

# Load and sort product data
print("Printing intial products list...")
load_product_data('product_data.txt')
bubble_sort(products)

# Print products formatted
def print_all_products(products):
    print(f"{'Product':^10}{'Name':^20}{'Price':^10}{'Category':^20}")
    print("-" * 60)
    for product in products:
        print(product)

print("")
print_all_products(products)
print("")

def record_sorting_times():
    start_time = time.time()
    bubble_sort(products)
    sorted_time = time.time() - start_time
    print(f"Time taken to sort already sorted data: {sorted_time:.4f} seconds")

# Reverse list section
    products.reverse()
    start_time = time.time()
    bubble_sort(products)
    reversed_time = time.time() - start_time
    print(f"Time taken to sort reverse ordered data: {reversed_time:.4f} seconds")
    bubble_sort(products)

record_sorting_times() # Print out how much time it took to sort the list

def user_input(prompt):
    return input(prompt)

def main():
    print("Welcome to the Data Organizer")
    print("How would you like to proceed? \n")
    print("Insert: Efficiently add new products.")
    print("Update: Modify existing product details.")
    print("Delete: Remove products while preserving data structure integrity.")
    print("Search: Efficiently find products using key attributes (e.g., ID, Name). \n")
    print("View: View all the products at any given time. \n")
    print("Please type the name or initial of the operation you would like to proceed with!")
    while True:
        operation = user_input("To exit the program at any time, type 'Exit'.\n").lower()
        if operation in ["insert", "i"]:
            insert()
        elif operation in ["update", "u"]:
            update()
        elif operation in ["delete", "d"]:
            delete()
        elif operation in ["search", "s"]:
            search()
        elif operation in ["view", "v"]:
            view()
        elif operation in ["exit", "e"]:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Please enter the appropriate operator!")

def view():
    bubble_sort(products)
    record_sorting_times()
    print_all_products(products)

def insert():
    id = user_input("Please add the ID of the product: ")
    name = user_input("Please add the Name of the product: ")
    price = float(user_input("Please add the Price of the product: "))
    category = user_input("Please add the Category of the product: ")
    insert_product(id, name, price, category)
    print("Product successfully added!")



def update():
    while True:
        try:
            id = int(user_input("Please insert the ID of the product you would like to update: "))
            product_exists = any(product.id == id for product in products)
            if not product_exists:
                print("Product not found. Please try again.")
                continue

            name = user_input("Please insert the new name of the product: ")
            price = float(user_input("Please insert the new price of the product: "))
            category = user_input("Please insert the new category of the product: ")
            if update_product(id, name, price, category):
                print("Product updated successfully!")
                break
            else:
                print("Update failed. Please try again.")
        except ValueError:
            print("Incorrect input. Please try again.")

def update_product(id, name, price, category):
    for product in products:
        if product.id == id:
            product.name = name
            product.price = price
            product.category = category
            return True
    return False

def delete():
    id = int(user_input("Please enter the ID of the product you would like to delete: "))
    delete_product(id)
    print("Product successfully deleted!")
    print_all_products(products)

def delete_product(id):
    global products
    for i, product in enumerate(products):
        if product.id == id:
            del products[i]
            return True
    return False

def search():
    search_type = str(user_input("Would you like to search your product by ID or by Name? Type in ID or Name to proceed: ")).lower()
    if search_type not in ['id', 'name']:
        print("Invalid search type. Please type 'ID' or 'Name' to proceed.")
        return

    if search_type == 'id':
        id = int(user_input("Please enter the ID of the product: "))
        result = [product for product in products if product.id == id]
    else:
        name = str(user_input("Please enter the exact name of the product: "))
        result = [product for product in products if name.lower() in product.name.lower()]

    if result:
        print_all_products(result)
    else:
        print("No products found with the given search criteria.")

main()