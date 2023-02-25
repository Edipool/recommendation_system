import os
import pandas as pd
from typing import List
from fastapi import FastAPI
from schema import PostGet
from loguru import logger
from dotenv import load_dotenv
from load_table import load_features
from get_model import load_models
from sqlalchemy import create_engine

# adding logs where you need to report that everything worked correctly
logger.add("file.log", level="INFO")

load_dotenv()  # pulling up passwords from a file .env
# data for connecting to the database
engine = create_engine(os.environ.get("PANDAS_CON"))

# Connecting to the database
logger.info('Initializing the Connect to BD function')
app = FastAPI()

model = load_models()  # in this variable lies the model
# called the load_features function, which returned a table with X
features = load_features()
post_df = pd.read_sql("""SELECT * FROM public.post_text_df;""",
                      con=engine)  # table with posts


# Creating an endpoint in which a model is called that makes predictions for the XXI
logger.info('Initialization endpointa /post/recommendations/')


@app.get("/post/recommendations/", response_model=List[PostGet])
def recommended_posts(id: int, limit: int = 5) -> List[PostGet]:

    # the sequence is as follows
    # 1. Made a prediction and took one column
    # 2. added these predictions to table X
    # 3. next, you will need to add the text of posts by posta id to df
    # 4. sorting
    # 5. collecting posts
    # 6. we return the response in accordance with the scheme described in the Post Get

    # 1. Made a prediction and took one column the prediction variable contains tables c X
    logger.info('Function initialization predict_proba the model has')
    prediction = model.predict_proba(features)[:, 1]

    # 2. added these predictions to the new dataframe
    logger.info('Initializing adding model predictions to a new one df_new')
    df_new = pd.DataFrame(features)
    df_new['prediction'] = prediction

    # 3. next, you will need to add the text of posts by posta id to df
    logger.info(
        'Initializing join df_new by post_df text from the post_df table')
    # merjim to BD the text of posts by post_id is already in the new dataframe
    df_new = df_new.merge(post_df, on='post_id', how='left')
    # sorting probabilities in descending order (from higher to lower)
    logger.info(
        'Initialization sorting in descending order of the prediction column')
    df_new = df_new.sort_values(by='prediction', ascending=False).reset_index()

    # Selection of posts
    logger.info('Initialization of selection limit-постов')
    df_new = df_new.loc[:limit - 1]

    return [PostGet(**{
        'id': post_id,
        'text': df_new[df_new['post_id'] == post_id]['text'].values[0],
        'topic': df_new[df_new['post_id'] == post_id]['topic'].values[0]
    }) for post_id in df_new['post_id']]

################# the model works well, your quality 0.450 Hitrate #################
