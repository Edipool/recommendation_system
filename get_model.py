import os
import pandas as pd
from catboost import CatBoostClassifier
from loguru import logger
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()  # pulling up passwords from a file .env
# data for connecting to the database
engine = create_engine(os.environ.get("PANDAS_CON"))

# We upload a file with the model (gradient boosting) that we threw into the LMS


def get_model_path(path: str) -> str:
    """
    This function takes the path to the model file and returns the model
    """
    logger.info('Function initialization get_model_path()')
    # We check where the code is executed in the bos, or locally. A little magic, if in LMS, then the address is below
    if os.environ.get("IS_LMS") == "1":
        MODEL_PATH = '/workdir/user_input/model'
    else:  # if locally, then the passed address is substituted in the function
        MODEL_PATH = path
    return MODEL_PATH


def load_models():
    """
    This function calls the model along the path that was passed to the get_model_path function
    """
    logger.info('Function initialization load_models()')
    # address of the model location
    model_path = get_model_path("/workdir/user_input/model")
    from_file = CatBoostClassifier()  # calling the model
    # for local use, we passed the model name to the filename variable
    filename = 'catboost_model'
    # calling the model dump via the get_model_path function, which specifies the address to the model file
    return from_file.load_model(filename)
