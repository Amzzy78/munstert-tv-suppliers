import gspread
from google.oauth2.service_account import Credentials

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
    Get purchase figures input form the user
    """
    print("Please enter purchases data from previous month.")
    print("Data covers 6 cells.")
    print("Example: Date,Product,Quantity,Net Price,Tax and Supplier.\n")

    data_str = ("Enter your data here: ")
    print(f"The data provided is {data_str}")


 # Call def get_purchases_data function  
get_purchases_data() 

