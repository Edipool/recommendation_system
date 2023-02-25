import os
import pandas as pd
from sqlalchemy import create_engine
from loguru import logger
from dotenv import load_dotenv

load_dotenv()  # pulling up passwords from a file .env
# data for connecting to the database
engine = create_engine(os.environ.get("PANDAS_CON"))

# Loading/unloading a table


def load_features() -> pd.DataFrame:
    '''
    An SQL query is written in this function,
    next, this request goes to the batch_load_sql() function
    '''
    logger.info('Function initialization load_features()')
    # passed the request to the batch_load_sql function
    return batch_load_sql('SELECT * FROM poljakov_13_features_lesson_22')


# the function takes a string SQL query, returns a dataframe
def batch_load_sql(query: str) -> pd.DataFrame:
    '''
    This function accepts an SQL query as a string, then connects to BD,
    and the installed chunks unloads the information and returns the dataframe connected from the chunks
    '''
    logger.info('Function initialization batch_load_sql()')
    CHUNKSIZE = 500  # chunk size

    conn = engine.connect().execution_options(stream_results=True)
    chunks = []  # storage location of the chunk
    # a string comes from the function, connection to the database, the size of the chunk
    for chunk_dataframe in pd.read_sql(query, conn, chunksize=CHUNKSIZE):
        chunks.append(chunk_dataframe)
    conn.close()
    return pd.concat(chunks, ignore_index=True)
