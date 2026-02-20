# Medical Shop Management System

## Project Overview
The **Medical Shop Management System** is a Python-based application that helps manage medicines in a medical store. It provides functionalities such as adding medicines, checking stock levels, and processing sales transactions while maintaining customer details and order records. The system connects to an SQL Server database to store and retrieve information efficiently.

## Features
- **Add Medicines:** Add new medicines to the database or update existing stock levels.
- **Stock Management:** Check the availability of medicines, especially those running low in stock.
- **Sell Medicines:** Process customer purchases, generate bills, and calculate profits.
- **Customer Management:** Store customer details and maintain purchase records.
- **Database Integration:** Uses SQL Server for data storage and retrieval.

## Technologies Used
- **Programming Language:** Python
- **Database:** SQL Server
- **Libraries Used:**
  - `pyodbc` for database connection
  - SQL queries for CRUD operations

## How It Works
1. **Medicine Management:**
   - Users can add new medicines or update the stock of existing ones.
   - The system checks if a medicine exists before inserting new records.
   - If the medicine exists, its stock is updated instead of inserting a duplicate entry.
2. **Stock Checking:**
   - The system lists medicines that have an availability of **5 or less**.
3. **Sales Process:**
   - Displays all available medicines.
   - Customers can enter the medicine ID, and the system verifies availability.
   - If sufficient stock is available, the system calculates the total cost and profit.
   - Updates the stock after a successful sale.
4. **Order and Customer Management:**
   - Customers provide their details (name and phone number) before placing an order.
   - The system generates an order ID and inserts the customer information into the database.
   - Order details are stored in the `orders` table.
   - A profit record is created for each order.
   - The total bill amount is updated in the customer table.
5. **Closing Transactions:**
   - The system updates the availability of medicines in the database.
   - The connection to the database is closed once operations are completed.

## Database Structure
- **medicine (mid, mname, pcost, scost, availability)**: Stores medicine details.
- **customer (orderid, customername, phon, totalbill)**: Stores customer information.
- **orders (orderid, mname, pcost, quantity, bill)**: Stores order details.
- **profit (orderid, profit_amount, date)**: Stores profit details per order.

## How to Run the Project
1. **Install Python** (if not installed) from [python.org](https://www.python.org/).
2. **Set Up SQL Server** and create a database named `project2`.
3. **Update Database Credentials** in the Python script.
4. **Run the script** using the command:
   ```
   python medical_shop.py
   ```
5. Follow the on-screen prompts to manage medicines, check stock, and process sales.

## Future Enhancements
- Implement a graphical user interface (GUI) using Tkinter or PyQt.
- Integrate an invoice generation system.
- Improve database performance with indexing and optimization.
- Add support for multiple users and roles (Admin, Cashier, Manager).

## Conclusion
The **Medical Shop Management System** automates the process of managing medicines, sales, and customer records. By integrating SQL Server, the system ensures efficient data management, making it a valuable tool for medical stores.

//Git working flow check

// this changes is done in the v2 branch