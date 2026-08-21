# 🏫 Smart Campus AI

**Smart Campus AI** is an AI-powered campus management application designed to make college services smarter, faster, and more efficient.

The project uses **Artificial Intelligence and Machine Learning** to help students and campus departments manage common campus-related queries and complaints.

## 🚀 Features

* 🤖 AI-powered campus assistant
* 📝 Student complaint registration
* 🏷️ Automatic complaint classification
* ⚡ Complaint priority detection
* 🏢 Department-wise complaint management
* 💾 Database storage
* 📊 Simple and user-friendly dashboard
* 🌐 Streamlit web application

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Machine Learning**
* **Scikit-learn**
* **Pandas**
* **SQLite**
* **TF-IDF Vectorization**
* **Logistic Regression**

## 📂 Project Structure

```text
Smart-Campus-AI/
│
├── app.py
├── classifier.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🧠 Machine Learning

The system uses **TF-IDF Vectorization** to convert complaint text into numerical features.

A **Logistic Regression** model is then used to classify complaints into different campus departments.

### Complaint Categories

* 🌐 Network
* 🏫 Classroom
* 🔬 Laboratory
* ⚡ Electricity
* 🚌 Transport
* 📚 Library
* 🏠 Hostel

## 💾 Database

The application uses **SQLite** to store complaint information.

Example fields:

```text
ID
Name
Complaint
Category
Priority
Department
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Smart-Campus-AI.git
cd Smart-Campus-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install dependencies

```bash
pip install streamlit pandas scikit-learn
```

### 4. Upgrade pip

```bash
python.exe --m pip install --upgrade pip
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 Objectives

* Improve campus complaint management
* Reduce manual complaint processing
* Automatically categorize complaints
* Help departments respond efficiently
* Provide students with an easy-to-use digital platform
