import sys
import os
from datetime import date

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
    current_date = date.today().isoformat
    # Create the order directory if it does not already exist

    return 

# Split the sales data into individual orders and save to Excel sheets
def process_sales_data(sales_csv, orders_dir):
    # Import the sales data from the CSV file into a DataFrame
    # Insert a new "TOTAL PRICE" column into the DataFrame
    insert()
    # Remove columns from the DataFrame that are not needed
    drop()
    # Group the rows in the DataFrame by order ID
    # For each order ID:
        # Remove the "ORDER ID" column
        # Sort the items by item number
        # Append a "GRAND TOTAL" row
        # Determine the file name and full path of the Excel sheet
        # Export the data to an Excel sheet
        # TODO: Format the Excel sheet
    pass

if __name__ == '__main__':
    main()