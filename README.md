# Personalized Product Recommendation System

## **Project Overview**

This project implements a **Personalized Product Recommendation System** using **collaborative filtering**. It leverages Google Cloud Platform (GCP) for scalable data processing and deployment. The system suggests products to users based on past interactions and is deployed as an API for real-world applications.

---

## **Features**

- **Data Collection**: Utilizes publicly available datasets or live retail APIs (e.g., Amazon, Best Buy)
- **Preprocessing**: Cleans and structures data for efficient recommendations
- **Modeling**: Uses **Surprise Library** for collaborative filtering techniques
- **Evaluation**: Measures performance using RMSE
- **API Development**: Flask-based API for serving recommendations
- **Frontend Interface**: Streamlit-based user interface
- **Deployment**: Hosted on **Google Cloud Platform (GCP)**

---

## **Project Structure**

```
Personalized-Product-Recommendation/
├── data/                 # Datasets used for training/testing
├── notebooks/            # Jupyter Notebooks for EDA & training
├── models/               # Saved trained models
├── src/                  # Core Python scripts
│   ├── data_processing.py  # Data loading & preprocessing
│   ├── train_model.py      # Training collaborative filtering model
│   ├── recommend.py        # Generating recommendations
├── api/                  # Flask API for model inference
├── frontend/             # Streamlit-based UI
├── deployment/           # Docker, CI/CD, GCP deployment
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
├── config.yaml           # Configuration settings
├── setup.py              # Python package setup (optional)
```

---

## **Setup Instructions**

### **1. Create a Virtual Environment**

```bash
conda create --name rec_sys python=3.9 -y
conda activate rec_sys
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Download & Prepare Data**

- Use **Amazon Fine Food Reviews** or **Best Buy API**.
- Place datasets in the `data/` directory.
- Run preprocessing script:

```bash
python src/data_processing.py
```

### **4. Train the Recommendation Model**

```bash
python src/train_model.py
```

### **5. Run API for Recommendations**

```bash
cd api/
python app.py
```

### **6. Run the Streamlit Frontend**

```bash
cd frontend/
streamlit run app.py
```

---

## **Model Evaluation**

- Performance is measured using **Root Mean Squared Error (RMSE)**.
- A good RMSE value depends on the dataset but should ideally be **below 1.0**.

---

## **Deployment on Google Cloud**

### **1. Build Docker Image**

```bash
docker build -t rec_sys_api .
```

### **2. Deploy on Google Cloud Run**

```bash
gcloud run deploy rec-sys-api --image gcr.io/[PROJECT-ID]/rec_sys_api --platform managed
```

### **3. Access the API**

```bash
curl -X GET "https://[CLOUD-RUN-URL]/recommend?user_id=123"
```

---

## **Showcase & Sharing**

- **GitHub**: Repository includes well-documented code and examples.
- **LinkedIn Post**: Highlights real-world use case, architecture, and demo.
- **Screenshots/GIFs**: Demonstrates API & UI functionalities.
- **Call to Action**: Invites feedback & contributions from the community.

---

## **Future Enhancements**

- Implement **hybrid recommendations** (collaborative + content-based filtering)
- Use **Google BigQuery** for scalable storage
- Integrate with **real-time retail APIs** for dynamic recommendations

---

## **Author**

Project developed to showcase **Machine Learning & Data Engineering skills** using GCP.

---

### **Let’s Connect!**

- **GitHub**: [Your GitHub Profile]
- **LinkedIn**: [Your LinkedIn Profile]
