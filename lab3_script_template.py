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
    sales_dataframe.drop(columns= ["ADDRESS", "CITY", "STATE", "COUNTRY", "POSTAL CODE"], inplace=True)

    # Group the rows in the DataFrame by order ID
    sales_dataframe = sales_dataframe.groupby("ORDER ID")
    # For each order ID:
    for order_ID, order_df in sales_dataframe:
        # Remove the "ORDER ID" column
        order_df.drop(columns=["ORDER ID"], inplace=True)
        # Sort the items by item number
        order_df.sort_values("ITEM NUMBER", inplace=True)
        # Append a "GRAND TOTAL" row
        g_t = order_df["TOTAL PRICE"].sum()
        g_t_df = pd.DataFrame({"ITEM PRICE":["GRAND TOTAL"], "TOTAL PRICE":[g_t]})
        order_df = pd.concat([order_df, g_t_df])
        # Determine the file name and full path of the Excel sheet
        excel_file = f"Order_{order_ID}.xlsx"
        excel_path = os.path.join(orders_dir, excel_file)

        # Export the data to an Excel sheet
        order_df.toexcel(excel_path, index=False)
        # TODO: Format the Excel sheet
    pass

if __name__ == '__main__':
    main()