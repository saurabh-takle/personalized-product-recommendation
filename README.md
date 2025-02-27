# Hello Bhava, Kasa Aahes?

# Personalized Product Recommendation System

## **Project Overview**
This project implements a **Personalized Product Recommendation System** using **collaborative filtering**. The goal is to provide product recommendations based on user interactions, leveraging machine learning techniques. The model is trained on a dataset containing user-product interactions and is saved for future use.

## **Features**
- Data preprocessing and exploratory data analysis (EDA)
- Model training using **collaborative filtering** with Surprise library
- Evaluation using RMSE (Root Mean Squared Error)
- Saving and loading trained models
- Generating personalized recommendations

---

## **Project Structure**

```
📂Personalized-Product-Recommendation/
├── 📂data/                 # Datasets used for training/testing
├── 📂notebooks/            # Jupyter Notebooks for EDA & training
├── 📂models/               # Saved trained models
├── 📂src/                  # Core Python scripts
│   ├── data_processing.py  # Data loading & preprocessing
│   ├── train_model.py      # Training collaborative filtering model
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
```

---

## **Dataset**
The dataset contains user interactions with products, including ratings or implicit feedback. We process and split the data into training and testing sets before applying collaborative filtering techniques.

---

## **Tech Stack**
- **Python**
- **Jupyter Notebook**
- **Pandas, NumPy** (Data Handling)
- **Surprise** (Collaborative Filtering)
- **Matplotlib, Seaborn** (Data Visualization)
- **Pickle** (Model Saving & Loading)

---
## **Setup Instructions**

### 1. Clone the Repository
```bash
git clone https://github.com/saura-t/personalized-product-recommendation.git
cd personalized-product-recommendation
```

### 2. Create a Virtual Environment (Recommended)
```bash
conda create --name [venv_name] python=3.9 -y
conda activate [venv_name]
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---
## Data Preprocessing

### Load the Dataset
```python
import pandas as pd

df = pd.read_csv('data/reviews.csv')
print(df.head())
```

### Check for Missing Values
```python
print(df.isnull().sum())
df.dropna(inplace=True)
```

### Data Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,5))
sns.countplot(x='interaction_type', data=df)
plt.title('Distribution of Interaction Types')
plt.show()
```

---
## Model Training

### Train-Test Split
```python
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split

reader = Reader(rating_scale=(1, 5))
dataset = Dataset.load_from_df(df[['user_id', 'product_id', 'rating']], reader)
trainset, testset = train_test_split(dataset, test_size=0.2)
```

### Train Model
```python
from surprise import SVD
from surprise import accuracy

model = SVD()
model.fit(trainset)
```

### Evaluate Model
```python
predictions = model.test(testset)
rmse = accuracy.rmse(predictions)
print(f'RMSE: {rmse}')
```
---

## Model Training with Hyperparameter Tuning
We perform hyperparameter tuning using **GridSearchCV** to find the best parameters for the SVD model.
```python
from surprise.model_selection import GridSearchCV
from surprise import SVD

param_grid = {
    'n_factors': [50, 100, 150],
    'n_epochs': [10, 20],
    'lr_all': [0.002, 0.005],
    'reg_all': [0.02, 0.1]
}

grid_search = GridSearchCV(SVD, param_grid, measures=['rmse'], cv=3)
grid_search.fit(data)

# Best Parameters
print("Best RMSE Score:", grid_search.best_score['rmse'])
print("Best Parameters:", grid_search.best_params['rmse'])
```

---
## Save & Load Model

### Save Model
```python
import pickle

with open('models/recommendation_model.pkl', 'wb') as f:
    pickle.dump(model, f)
```

### Load Model
```python
with open('models/recommendation_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
```

---

## Model Evaluation

- Performance is measured using **Root Mean Squared Error (RMSE)**.
- A good RMSE value depends on the dataset but should ideally be **below 1.0**.

```python
from surprise import accuracy
predictions = best_model.test(testset)
rmse = accuracy.rmse(predictions)
print("Final RMSE:", rmse)
```

---
## Author
Your Name  
[LinkedIn Profile](https://linkedin.com/in/saurabhtakle)  
[GitHub](https://github.com/saura-t)

