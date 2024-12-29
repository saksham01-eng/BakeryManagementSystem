import pandas as pd 

# Initialize the order ID
order_id = 0

# Read existing data from the CSV file
try:
    existing_data = pd.read_csv("BOM.csv")
    # Check if the CSV file is empty
    if existing_data.empty:
        order_id = 0
    else:
        # Set the order_id to the maximum existing order_id in the file
        order_id = existing_data.loc[:,"order_id"].max()
except FileNotFoundError:
    # If the file does not exist, initialize the order ID to 0
    existing_data = pd.DataFrame()
    order_id = 0

# Initialize an empty list to store orders
order = []

# Function to enter new order data
def enter_data():
    global order_id 
    # Increment the order ID for each new order
    order_id += 1

    # Collect order details from the user
    item = input("Item: ")
    customer_name = input("Customer Name: ")
    quantity = input("Quantity: ")

    # Create an order record
    o = [order_id, item, customer_name, quantity]
    print("Your order ID is:", order_id)

    # Append the order to the orders list
    order.append(o)

    # Export the order data to the CSV file
    export_data()

# Function to search for an order by its ID
def search_order(order_id_to_search):
    try:
        # Read the data from the CSV file
        order_1 = pd.read_csv("BOM.csv")

        # Search for the order ID in the data
        result = order_1[order_1['order_id'] == order_id_to_search]

        # If the order is found, print its details
        if not result.empty:
            print(result.to_string(index=False))
        else:
            print("Order ID not found.")
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("BOM.csv file not found. Please provide valid input.")

# Function to export the order data to the CSV file
def export_data():
    # Create a DataFrame from the orders list
    order_1 = pd.DataFrame(order, columns=["order_id", "item", "name", "quantity"])
    try:
        # Read existing data from the CSV file
        data2 = pd.read_csv("BOM.csv")

        # If the CSV file is empty, write with headers
        if data2.empty:
            order_1.to_csv("BOM.csv", mode='a', index=False)
        else:
            # Append to the file without writing headers
            order_1.to_csv("BOM.csv", mode='a', header=False, index=False)
    except FileNotFoundError:
        # If the file does not exist, create it and write the data
        order_1.to_csv("BOM.csv", mode='a', index=False)

    print(order_1)

# Main function to run the program
def main():
    while True:
        # Display menu options to the user
        print("Choose the operation:")
        print("1. Add order")
        print("2. Search for your order")
        print("3. Exit")

        # Get the user's choice
        choice = int(input("Enter the desired operation: "))

        # Perform actions based on user choice
        if choice == 1:
            enter_data()
        elif choice == 2:
            search_for = int(input("Enter order ID: "))
            search_order(search_for)
        elif choice == 3:
            exit(1)

# Run the main function
main()
