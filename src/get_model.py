import os
from catboost import CatBoostClassifier
from loguru import logger

# Uploading a file with the model


def get_model_path(path: str) -> str:
    """
    This function takes the path to the model file and returns the model

    Parameters
    ----------
    path : str
        Path to the model file

    Returns
    -------
    MODEL_PATH : str
        Path to the model file
    """
    logger.info('Function initialization get_model_path')
    if os.environ.get("IS_LMS") == "1":
        MODEL_PATH = '../models'
    else:
        MODEL_PATH = path

    return MODEL_PATH


# functions for local use
def load_models():
    """
    This function calls the model along the path that was passed to the get_model_path function

    Parameters
    ----------
    None

    Returns
    -------
    from_file : CatBoostClassifier
        Model
    """
    logger.info('Initializing the load_models() function: loading the model')
    from_file = CatBoostClassifier()  # calling the model for local use
    # for local use, the model name was passed to the variable filename for local use
    filename = '../models/catboost_model'
    logger.info(
        'The model has loaded')
    # calling the model dump via the get_model_path function, which specifies the address to the model file for local use
    return from_file.load_model(filename)
