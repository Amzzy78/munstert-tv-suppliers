import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')  
SCOPED_CREDS = CREDS.with_scopes(SCOPE) 
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) 
SHEET = GSPREAD_CLIENT.open('MunsterTv-Suppliers')  

#purchases = SHEET.worksheet('purchases')
#data = purchases.get_all_values()
#print(data)


# Requesting data from the user
# Function to collect purchase data from user
def get_purchases_data():
    """
    Get purchase figures input from the user
    """
# Repeat request for data to loop until correct input
    while True:
        print("Please enter purchases data.")
        print("Data covers 6 cells and to be seperated by commas.")
        print("Example: Date,Product,Quantity,Net Price,Tax and Supplier.\n")

        data_str = input("Enter your data here: ")
        #print(f"The data provided is {data_str}")

        # Split() method returns the broken up values as a list
        purchases_data = data_str.split(",")
        #print(purchases_data)

    # Call validate function
    #validate_data(purchases_data)

        if validate_data(purchases_data):
             print("Data is valid!")
             break

    return purchases_data

# Validate data function with a try statement
def validate_data(values):
    """
    Inside the try, converts all string values().
    Raise ValueError if strings cannot be converted into int,
    or if there arent exactly 6 cell values.
    """
    try:
        [str(value) for value in values]  
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 cells with values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")  
        return False   

    return True         

    #print(values) 
       

# Insert new entry to google purchases sheet 
def update_purchases_worksheet(data):
    """
    Update purchases worksheet, add new row with the list provided
    """
    print("Updating purchases worksheet...\n")
    purchases_worksheet = SHEET.worksheet('purchases')
    purchases_worksheet.append_row(data)
    print("Purchases worksheet updated successfully.\n")



# Get each suppliers name from supplier sheet
def calculate_suppliers_data(supplier_col):
    """
    Calculate how many suppliers
    """
    print("Calculating each suppliers name..\n")
    suppliers = SHEET.worksheet("suppliers").get_all_values()
    pprint(suppliers)

    # Insert new entry to google suppliers sheet 
def update_suppliers_worksheet(data):
    """
    Update suppliers worksheet, add new row with the list provided
    """
    print("Updating suppliers worksheet...\n")
    suppliers_worksheet = SHEET.worksheet('suppliers')
    suppliers_worksheet.append_row(data)
    print("Suppliers worksheet updated successfully.\n")


# Put function calls into main()
def main():
    """
    Run all program functions
    """
    # Call def get_purchases_data function  
    data = get_purchases_data() 
    purchases_data = [str(int) for int in data]
    # Call function def update_purchases_worksheet
    update_purchases_worksheet(purchases_data)
    calculate_suppliers_data(purchases_data)
    update_suppliers_worksheet(suppliers_data)

print("Welcome to Munster TV data automation")    
main()    
