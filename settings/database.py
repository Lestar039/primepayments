import sqlalchemy

from secrets import Secret
db = Secret().db_creds()

db_driver = 'SQL Server'
db_url = database_url = f'mssql+pyodbc://{db.get("db_user")}:{db.get("db_pass")}@{db.get("db_host")}/{db.get("db_database")}?driver={db_driver}'
engine = sqlalchemy.create_engine(db_url)
