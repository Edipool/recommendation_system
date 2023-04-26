import pandas as pd
from loguru import logger


# Loading/unloading a table
def load_features() -> pd.DataFrame:
    """
    The function of loading local features

    Parameters
    ----------
    None

    Returns
    -------
    liked_posts : pd.DataFrame
        Table with liked posts
    post_features : pd.DataFrame
        Table with post features
    user_features : pd.DataFrame
        Table with user features
    
    """
    logger.info('Loading features')
    logger.info('df_user_data.csv')
    user_features = pd.read_csv('../datasets/df_user_data.csv', sep=';')

    logger.info('Loading df_post_text_plus_clustrs.csv')
    post_features = pd.read_csv('../datasets/df_post_text_plus_clustrs.csv', sep=';')

    logger.info('Loading df_feed_data.csv')
    liked_posts = pd.read_csv('../datasets/df_feed_data.csv', sep=';')

    logger.info('Features loaded')
    return liked_posts, post_features, user_features,
