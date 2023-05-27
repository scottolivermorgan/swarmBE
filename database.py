from dotenv import dotenv_values
from sqlalchemy import create_engine

# Load enviroment variables to build connection string from credentials
config = dotenv_values(".env.development")
connection_string = f"mysql+{config['DRIVERNAME']}://{config['USERNAME']}:{config['PASSWORD']}@{config['SERVER']}:{config['PORT']}/{config['DBNAME']}"

print(connection_string)
# Connect to MySQL database
engine = create_engine(connection_string, echo=True)