import os

from dotenv import load_dotenv

load_dotenv()


class Secret:

    def payment_creds(self):
        return {
            "project_number": os.getenv("PROJECT_NUMBER"),
            "secret_one": os.getenv("PAYMENT_SECRET_ONE"),
            "secret_two": os.getenv("PAYMENT_SECRET_TWO"),
        }

    def host_creds(self):
        return {
            "host": os.getenv("HOST"),
            "port": os.getenv("PORT")
        }

    def db_creds(self):
        return {
            "db_host": os.getenv("DB_HOST"),
            "db_port": os.getenv("DB_PORT"),
            "db_user": os.getenv("DB_USER"),
            "db_pass": os.getenv("DB_PASS"),
            "db_database": os.getenv("DB_DATABASE")
        }
