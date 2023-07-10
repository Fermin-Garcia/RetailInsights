#import the libraries we are working with 
import pandas as pd 
import os 
import env


# First we need to use our env file to access our mysql data base
def get_connection():
    
    '''
    This function will return the link to access mysql database. 
    '''
    user=env.username
    password=env.password
    host=env.host
    db=env.db
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    
# next we define the query that we are calling from sql 
query = """
select `Order ID`, `Order Date`, `Ship Date`, `Country`, `City`, `State`, `Postal Code`, `Sales`, `Quantity`, `Discount` , `Profit`, `Category`, `Sub-Category`, `Product Name` 
from orders
left join regions using(`Region ID`)
left join categories using(`Category ID`)
left join products using(`Product ID`)
where Segment = 'Consumer'


"""


# then we get this and use it to make a fucntion that 
# will check to see if a csv file containing the telco file named 
# telco.csv is it doesn't then the code will then run the query through 
# pymysql and cache the file locally so it is fastly accessiable 


def get_sales_data():
    if os.path.exists('sales.csv') == True:
        return pd.read_csv('sales.csv')
    else:
        df = pd.read_sql(query, get_connection())
        df.to_csv('sales.csv')
        return pd.read_csv('sales.csv', index_col=0)
