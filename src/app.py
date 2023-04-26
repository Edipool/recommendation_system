import uvicorn
from typing import List
from datetime import datetime
from fastapi import FastAPI
from schema import PostGet
from loguru import logger
from load_table import load_features
from get_model import load_models

app = FastAPI()
logger.info('Сalling the model')
model = load_models()  # calling the model
logger.info('Calling the load_features function')
features = load_features()


def get_recommended_feed(id: int, time: datetime, limit: int = 5) -> List[PostGet]:
    """
    The function of getting recommendations

    Parameters
    ----------
    id : int
        User id
    time : datetime
        Time of recommendation
    limit : int, optional
        Number of recommendations, by default 5
    """
    # Creating a table on which the model was trained
    logger.info('Function initialization get_recommended_feed')

    # Uploaded features by users

    logger.info('Uploading features by users')
    # A filter to ensure that the user_id has an id submitted to the function
    user_features = features[2].loc[features[2].user_id == id]
    # We remove the column with user_id because it did not participate in the training of the model
    user_features = user_features.drop('user_id', axis=1)

    # Upload features by posts
    logger.info('Upload features by posts')
    # Removing the text column because it did not participate in the training of the model
    post_features = features[1].drop(['text'], axis=1)
    # Returning columns with content from the post_features table, where 'post_id', 'text', 'topic' and clusters from Berf work lie
    content = features[1][['post_id', 'text', 'topic']]

    # Let's combine these features
    # We take the vector of features, and attach each of their posts to the vector of features, we get a table of 7 thousand
    # - this will be a matrix of posts for the selected user
    logger.info('The deliciousness of these features')
    add_user_fetures = dict(
        zip(user_features.columns, user_features.values[0]))
    # creating a constant column with user features
    user_posts_features = post_features.assign(**add_user_fetures)
    user_posts_features = user_posts_features.set_index(
        'post_id')  # assign the post_id column to the index

    # Add information about the date of the recommendation from the time passed to the function
    logger.info('Adding information about the recommendation date')
    user_posts_features['hour'] = time.hour
    user_posts_features['month'] = time.month

    # Let's make predictions
    logger.info('Forming a prediction')
    # we make predictions and get the probability of a positive class
    predict = model.predict_proba(user_posts_features)[:, 1]
    # adding predictions to the table
    user_posts_features['predicts'] = predict

    # Let's remove the posts that the user has already liked
    logger.info('Lets remove the posts that the user has already liked')
    liked_posts = features[0]
    liked_posts = liked_posts[liked_posts.user_id == id].post_id.values
    filtered_ = user_posts_features[~user_posts_features.index.isin(
        liked_posts)]

    # we recommend the top 5 in the probability of posts
    logger.info('We recommend the top 5 in terms of the probability of posts')
    recommended_posts = filtered_.sort_values('predicts')[-limit:].index

    # We return the software from the content
    return [PostGet(**{
        'id': i,
        'text': content[content.post_id == i].text.values[0],
        'topic': content[content.post_id == i].topic.values[0],
    }) for i in recommended_posts
    ]


@app.get("/post/recommendations/", response_model=List[PostGet])
def recommended_posts(id: int, time: str, limit: int = 5) -> List[PostGet]:
    '''
    Main function for getting recommendations

    Parameters
    ----------
    id : int
        User id
    time : str
        Time of recommendation

    limit : int, optional
        Number of recommendations, by default 5

    Returns
    -------
    List[PostGet]
        List of recommended posts

    '''

    logger.info('Initialization end-point /post/recommendations/')

    time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return get_recommended_feed(id, time, limit)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)


