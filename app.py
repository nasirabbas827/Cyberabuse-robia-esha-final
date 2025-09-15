import os
from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

# Load models and vectorizer
def load_models():
    models = {
        'Multinomial Naive Bayes': joblib.load('models/multinomial_naive_bayes_model.joblib'),
        'Random Forest': joblib.load('models/random_forest_model.joblib'),
        'SVM (Linear Kernel)': joblib.load('models/svm_(linear_kernel)_model.joblib')
    }
    tfidf_vectorizer = joblib.load('models/tfidf_vectorizer.joblib')
    return models, tfidf_vectorizer

models, tfidf_vectorizer = load_models()

# Roman Urdu stop words (you can expand this list)
roman_urdu_stop_words = [
    'hai','aur','ko','mein','se','ne','ki','ka','ke','liye','ho','tha','thi','the','hum'
]

# Preprocessing function
def preprocess_input(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    words = text.split()
    filtered_words = [word for word in words if word not in roman_urdu_stop_words]
    return ' '.join(filtered_words)

@app.route('/', methods=['GET', 'POST'])
def home():
    predictions = {}
    if request.method == 'POST':
        user_comment = request.form['comment']
        cleaned_comment = preprocess_input(user_comment)
        comment_tfidf = tfidf_vectorizer.transform([cleaned_comment])

        for name, model in models.items():
            pred = model.predict(comment_tfidf)[0]
            predictions[name] = pred
    return render_template('index.html', predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
