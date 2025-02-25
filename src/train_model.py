from pandas import read_csv

from surprise import Dataset, Reader, SVD, accuracy
from surprise.model_selection import cross_validate, train_test_split, GridSearchCV
from collections import defaultdict
import pickle

df = read_csv("../data/reviews.csv")

# Define reader with rating scale
reader = Reader(rating_scale=(df['rating'].min(), df['rating'].max()))

# Load data into Surprise dataset
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

# Split into train (80%) and test (20%)
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Train SVD
svd_model = SVD()
svd_model.fit(trainset)

# Make predictions on the test set
predictions = svd_model.test(testset)

# Calculate RMSE (Root Mean Square Error)
rmse = accuracy.rmse(predictions)

# Hyperparameter Tuning
param_grid = {
    'n_factors': [50, 100, 150],
    'n_epochs': [10, 20],
    'lr_all': [0.002, 0.005],
    'reg_all': [0.02, 0.1]
}

grid_search = GridSearchCV(SVD, param_grid, measures=['rmse'], cv=3)
grid_search.fit(data)

# Best model
best_model = grid_search.best_estimator['rmse']

# Save the trained model
with open("../models/recommendation_model.pkl", "wb") as model_file:
    pickle.dump(best_model, model_file)

print("Model saved successfully!")
