Hello, world!
This is my first project uploaded to GitHub!

This project implements a recommendation system based on classical and deep machine learning.
In the file app.py contains the logic of the microservice operation on the recommendation of posts.
In the get_model file.py contains the logic of loading the `catboost_model` file with the predictions of the CatBoostClassifier model
In the file load_table.py contains the logic of loading a table with already processed features
In the schema file.py contains the logic of a pydantic-based scheme


To start the service in Postman, you need to: open a terminal in the project folder and enter this command: `python -m unicorn app:app --reload`
then wait for the service to load, select the `GET` request type in Postman and enter the following command:
`localhost:8000/post/recommendations?id=200`
You can change the id and if a user with the entered id exists in the database, then a recommendation of five posts will be made for him
