# fibrenest_db_models
This is the DB schema and sqlalchemy db models for fibrenest

# Usage
You would want to install this module in your project and then import the 
needed db model.  
There is separate model if the backend DB is postgres. 

#### Installation
`pip install fibrenest-db-models`

#### Import for postgres
`from fibrenest_db_models.postgres import ONT, CPE, CUSTOMER`

#### Import for all other DBs
`from fibrenest_db_models import ONT, CPE, CUSTOMER`

## Models
1) ONT: DB table for ONTs info
2) CPE: DB table for CPEs
3) CUSTOMER: DB table for customers
