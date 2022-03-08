from sql import *
from config import *
import pandas as pd
from simpledbf import Dbf5
from sqlalchemy import *

DBF_FILE = 'DH5188.DBF'  # 'SC5174.DBF'
SQL_TABLE = ''  # 'TypeOfServices'


if __name__ == '__main__':
    insert_into_sql_table_from_dbf(DBF_FILE)
