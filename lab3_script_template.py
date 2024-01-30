import sys
import os
from datetime import date
import pandas as pd

def main():
    sales_csv = get_sales_csv()
    orders_dir = create_orders_dir(sales_csv)
    process_sales_data(sales_csv, orders_dir)

# Get path of sales data CSV file from the command line
def get_sales_csv():
    if len(sys.argv) < 2:
        print("Incorrect parameters")
        sys.exit(1)

    # Check whether command line parameter provided
    if not os.path.isfile(sys.argv[1]):
        print("Error, this is an invalid filepath")
        sys.exit(1)

    # Check whether provide parameter is valid path of file
    return sys.argv[1]

# Create the directory to hold the individual order Excel sheets
def create_orders_dir(sales_csv):
    # Get directory in which sales data CSV file resides
    sales_csv_path = os.path.abspath(sales_csv)
    sales_csv_dir = os.path.dirname(sales_csv_path)
    # Determine the name and path of the directory to hold the order data files
    current_date = date.today().isoformat()
    orders_folder = f"orders_{current_date}"
    orders_directory = os.path.join(sales_csv_dir, orders_folder)
    # Create the order directory if it does not already exist
    if not os.path.isdir(orders_directory):
        os.makedirs(orders_directory)

    return orders_directory

# Split the sales data into individual orders and save to Excel sheets
def process_sales_data(sales_csv, orders_dir):
    # Import the sales data from the CSV file into a DataFrame
    sales_dataframe = pd.read_csv(sales_csv)
    # Insert a new "TOTAL PRICE" column into the DataFrame
    sales_dataframe = sales_dataframe.insert(7, "TOTAL PRICE", sales_dataframe["ITEM QUANTITY"] * sales_dataframe["ITEM PRICE"])
    # Remove columns from the DataFrame that are not needed
    sales_dataframe.drop(columns=["ADDRESS", "CITY", "STATE", "COUNTRY", "POSTAL CODE"] inplace=True)
    
    # Group the rows in the DataFrame by order ID
    order_ID = sales_dataframe.sort_values(by="ORDER ID")
    # For each order ID:
    for orders in order_ID:
        # Remove the "ORDER ID" column
        sales_dataframe = sales_dataframe.drop(orders)
        # Sort the items by item number
        sales_dataframe = sales_dataframe.sort_values("ITEM NUMBER")
        # Append a "GRAND TOTAL" row
        grand_total = sales_dataframe("TOTAL PRICE").sum()
        sales_dataframe = sales_dataframe.append("GRAND TOTAL", {grand_total})
        # Determine the file name and full path of the Excel sheet

        # Export the data to an Excel sheet

        # TODO: Format the Excel sheet
    pass

if __name__ == '__main__':
    main()