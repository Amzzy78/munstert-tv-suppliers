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
# Repeat request for data to loop until correct input
    while True:
        print("Please enter purchases data from previous month.")
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
        #[int(value) for value in values]  #only use if all numbers
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 cells with values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")  
        return False   

    return True         

    #print(values)    


 # Call def get_purchases_data function  
data = get_purchases_data() 

