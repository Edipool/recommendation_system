# Project Description

This project is an updated version of a recommender system built for a fictional social network. The recommender system has been refactored into logical modules, the connection to the remote database has been removed (all tables have been downloaded and are located in the dataset module), data logging has been added through DVC, a Dockerfile has been added to build an image and run a container, Docstrings have been added to all functions, and the approach to recommendation formation has been rethought. The previous version had unstable logic in recommendation formation, and text processing using TF-IDF has been added to improve *hitrate@5* metric from 0.45 to 0.53.
This recommendation system implements the "Content Approach". The data approach is more suitable than the "Collaborative Approach" because of the large amount of data and speed. The content approach is an approach that recommends to the user similar to those that he has already viewed. In this case, the recommendation system recommends to the user posts that he has not yet viewed, but which are similar to those that he has already viewed. The recommendation system is implemented in the form of a microservice that accepts requests and returns responses. The *hitrate@5* metric is used as a recommendation quality metric. The *hitrate@5* metric is the percentage of recommendations that the user has viewed.


# Project Structure
The `dataset module` contains datasets, which are logged using DVC. The `df_feed_data.csv` file contains information on viewed posts. The `df_text_plus_clustering.csv` file contains information on post text, text clustering, and new features based on clustering. The `df_post_text.csv` file contains information on post text. The `df_user_data.csv` file contains information on users. The `dists_df.csv` file contains information on text clusters. The reason for creating a separate dataframe for clusters is that clustering takes time and resources. If you want to cluster the texts, you can do so by uncommenting cell 11 in the Experiments_with_the_recommendation system.app file. The `.csv.dvc` file extension is a DVC log and is not directly involved in the code's operation.

The models module contains models, which are logged using DVC. The catboost_model file is a CatBoost classifier model. The model_tree_classifier file is a Decision Tree Classifier model. The .dvc file extension is a DVC log and is not directly involved in the code's operation.

The src module contains the project's source code. The app.py file launches the microservice, processes specific requests, and generates responses. The `get_model.py` file loads the CatBoost classifier model. The `load_table.py` file loads the partially processed tables and the tables that need to be further processed for each specific request. The `schema.py` file validates input data. The app.py file contains the microservice's logic, based on message recommendations.

# Running the code

The command to run docker: `docker run --rm -p 8000:8000 recommendation_system`
The command in Postman: `http://localhost:8000/post/recommendations?id=767&time=2022-12-12 21:10:16&limit=5`
In the postman, you can change the user `id`, `time` from `2021-12-29 23:39:35` to `2021-10-01 06:06:44` and the `limit`

# Main libraries used
![Pyhon](https://img.shields.io/badge/-Python_3.9.12-090909?style=for-the-badge&logo=python) ![Fastapi](https://img.shields.io/badge/-Fastapi_v0.75.1-090909?style=for-the-badge&logo=Fastapi) ![Catboost](https://img.shields.io/badge/-Catboost_v1.0.6-090909?style=for-the-badge&logo=Catboost) ![Scikit_learn](https://img.shields.io/badge/-Scikit_learn_v1.1.1-090909?style=for-the-badge&logo=Scikit_learn) ![Pandas](https://img.shields.io/badge/-pandas_v1.4.2-090909?style=for-the-badge&logo=pandas) ![Numpy](https://img.shields.io/badge/-Numpy-090909?style=for-the-badge&logo=Numpy) ![Pydantic](https://img.shields.io/badge/-pydantic_v1.9.1-090909?style=for-the-badge&logo=pydantic) ![Docker](https://img.shields.io/badge/-Docker-090909?style=for-the-badge&logo=Docker) ![mlflow](https://img.shields.io/badge/-mlflow_v1.19.0-090909?style=for-the-badge&logo=mlflow)
