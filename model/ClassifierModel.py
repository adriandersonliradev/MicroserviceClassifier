import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Carregar o modelo e o vetorizer salvos
vectorizer = joblib.load('model/vectorizer.pkl')
logistic_model = joblib.load('model/logistic_model.pkl')
