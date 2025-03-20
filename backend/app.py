from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
from surprise import Dataset, Reader

app = Flask(__name__)
CORS(app)

# Load dataset (Ensure ratings.csv exists in the data folder)
df = pd.read_csv("../data/reviews.csv")

# Convert user_id and item_id to numeric
df['user_id'] = df['user_id'].astype('category').cat.codes
df['item_id'] = df['item_id'].astype('category').cat.codes

# Load trained recommendation model
with open("../models/recommendation_model.pkl", "rb") as file:
    model, train = pickle.load(file)

# reader = Reader(rating_scale=(1, 5))
# data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
# train = data.build_full_trainset()  # Build trainset


def get_top_n_recommendations(user_id, model, train, df, n=5):
    # Returns the top N product recommendations for a given user

    all_products = df['item_id'].unique()

    # Check if user exists in training set
    try:
        inner_user_id = train.to_inner_uid(user_id)
    except ValueError:
        print(f"User ID {user_id} not found in training data.")
        return []  # Return empty if user is not in the dataset
    
    user_products = df[df['user_id'] == user_id]['item_id'].unique()
    unseen_products = [p for p in all_products if p not in user_products]

    if not unseen_products:
        return []
    
    # Generate predictions & filter low-confidence recommendations
    predictions = [(item, model.predict(inner_user_id, item, train).est)
                   for item in unseen_products]
    predictions = [p for p in predictions if p[1] > 3.5]  # Keep only high-rated predictions
    predictions.sort(key=lambda x: x[1], reverse=True)

    return [item[0] for item in predictions[:n]]


@app.route('/recommend', methods=['GET'])
def recommend():
    # API Endpoint to get recommendations for a user.
    user_id = request.args.get("user_id", type=int)
    if user_id is None:
        return jsonify({"error": "Please provide a valid user_id"}), 400

    recommendations = get_top_n_recommendations(user_id, model, train, df, n=5)

    if not recommendations:
        return jsonify({"message": f"No recommendations found for user {user_id}."}), 200
    
    recommendations = [int(item) for item in recommendations]

    return jsonify({"user_id": int(user_id), "recommendations": recommendations})


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)