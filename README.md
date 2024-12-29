# BakeryManagementSystem
🛒 Order Management System
This Python-based Order Management System is designed to streamline the process of managing customer orders, ensuring data persistence, efficiency, and user-friendliness. It uses the powerful pandas library to handle order data in a CSV file, making it ideal for small-scale businesses or learning projects.

🚀 Key Features
✅ Persistent Order Tracking
Reads existing orders from a CSV file (BOM.csv) and initializes the system with the highest order_id for continuity.
Automatically handles cases where the file is missing or empty, ensuring seamless operation.
✅ Dynamic Order Creation
Use the enter_data() function to add new orders by providing:
Item name
Customer name
Quantity
Automatically generates a unique order_id for every new order.
Saves new orders to BOM.csv for future retrieval.
✅ Easy Order Search
The search_order(order_id) function lets users search for specific orders by their unique order_id.
Displays full details if the order is found; otherwise, notifies the user that the order ID doesn’t exist.
✅ Efficient Data Export
The export_data() function appends new orders to the CSV file without overwriting existing data.
Creates the file automatically if it doesn’t exist, ensuring data persistence.
✅ Interactive Menu
The main() function provides a menu-driven interface with options to:
Add a new order
Search for an order
Exit the program
🌟 Why Use This System?
Data Reliability: Ensures all orders are securely saved in a CSV file.
Scalability: Capable of handling large order datasets with minimal changes.
Simple & Intuitive: Ideal for beginners in Python, providing clear functions and logic for managing data.
Real-World Application: Perfect for learning how to manage and process data without requiring a database.
🔧 How It Works
The program reads the BOM.csv file (if available) to load existing orders.
Users can interact with the system through a menu to add or search orders.
New orders are appended to the file, ensuring no data is lost.
A unique order_id is generated automatically for each new order.
This project is a great starting point for anyone learning about Python data handling, file management, and basic order processing workflows. It’s simple yet practical, with room for future enhancements like database integration or advanced analytics.
