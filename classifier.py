from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

training_texts = [
    "wifi is not working",
    "internet connection is slow",
    "network is unavailable",
    "projector is not working",
    "classroom fan is broken",
    "classroom lights are not working",
    "lab computer is not working",
    "laboratory system has stopped",
    "electricity is unavailable",
    "power failure in building",
    "bus is late",
    "college bus did not arrive",
    "library book is missing",
    "library timing problem",
    "hostel water problem",
    "hostel room issue"
]

training_labels = [
    "Network",
    "Network",
    "Network",
    "Classroom",
    "Classroom",
    "Classroom",
    "Laboratory",
    "Laboratory",
    "Electricity",
    "Electricity",
    "Transport",
    "Transport",
    "Library",
    "Library",
    "Hostel",
    "Hostel"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(training_texts)

model = LogisticRegression()

model.fit(X, training_labels)


def classify_complaint(text):

    text_vector = vectorizer.transform([text])

    category = model.predict(text_vector)[0]

    return category