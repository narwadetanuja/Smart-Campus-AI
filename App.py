import streamlit as st
import pandas as pd
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ML Training
texts = [
    "wifi is not working","internet connection is slow","network is unavailable",
    "projector is not working","classroom fan is broken","classroom lights are not working",
    "lab computer is not working","laboratory system has stopped",
    "electricity is unavailable","power failure in building",
    "bus is late","college bus did not arrive",
    "library book is missing","library timing problem",
    "hostel water problem","hostel room issue"
]

labels = [
    "Network","Network","Network","Classroom","Classroom","Classroom",
    "Laboratory","Laboratory","Electricity","Electricity",
    "Transport","Transport","Library","Library","Hostel","Hostel"
]

vec = TfidfVectorizer()
model = LogisticRegression().fit(vec.fit_transform(texts), labels)

def classify(text):
    return model.predict(vec.transform([text]))[0]

# Priority
def priority(text):
    text = text.lower()
    high = ["emergency","danger","fire","accident","security",
            "electric shock","not working for days"]
    medium = ["urgent","broken","slow","problem","issue"]

    for w in high:
        if w in text: return "High", f"High-risk keyword detected: {w}"
    for w in medium:
        if w in text: return "Medium", f"Medium-priority keyword detected: {w}"
    return "Low", "No high or medium priority indicator found"

# Database
def db():
    con = sqlite3.connect("complaints.db")
    con.execute("""CREATE TABLE IF NOT EXISTS complaints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, complaint TEXT, category TEXT,
        priority TEXT, department TEXT, reason TEXT)""")
    con.close()

def add(data):
    con = sqlite3.connect("complaints.db")
    con.execute("INSERT INTO complaints(name,complaint,category,priority,department,reason) VALUES(?,?,?,?,?,?)", data)
    con.commit()
    con.close()

def get_data():
    con = sqlite3.connect("complaints.db")
    df = pd.read_sql("SELECT * FROM complaints ORDER BY id DESC", con)
    con.close()
    return df

departments = {
    "Network":"IT Department", "Classroom":"Administration",
    "Laboratory":"Lab Department", "Electricity":"Electrical Department",
    "Transport":"Transport Department", "Library":"Library Department",
    "Hostel":"Hostel Department"
}

db()

# Streamlit UI
st.set_page_config(page_title="Smart Campus AI", page_icon="🎓", layout="wide")
st.title("🎓 Smart Campus AI")
st.write("AI-assisted campus complaint classification and priority prediction system")

menu = st.sidebar.selectbox("Select Module", ["Submit Complaint","Admin Dashboard"])

if menu == "Submit Complaint":
    st.header("📝 Submit Campus Complaint")
    name = st.text_input("Student Name")
    complaint = st.text_area("Describe your problem",
                              placeholder="Example: Wi-Fi is not working in Lab 3...")

    if st.button("🤖 Analyze Complaint"):
        if not name.strip() or not complaint.strip():
            st.warning("Please enter your name and complaint.")
        else:
            category = classify(complaint)
            level, reason = priority(complaint)
            dept = departments.get(category, "Administration")

            st.subheader("🔍 AI Analysis Result")
            c1,c2,c3 = st.columns(3)
            c1.metric("Category", category)
            c2.metric("Priority", level)
            c3.metric("Department", dept)
            st.info(f"💡 Reason: {reason}")

            add((name,complaint,category,level,dept,reason))
            st.success("✅ Complaint submitted successfully!")

else:
    st.header("📊 Admin Dashboard")
    df = get_data()

    if not df.empty:
        c1,c2,c3 = st.columns(3)
        c1.metric("Total Complaints", len(df))
        c2.metric("High Priority", (df["priority"]=="High").sum())
        c3.metric("Categories", df["category"].nunique())

        st.subheader("📋 Complaint Records")
        st.dataframe(df, use_container_width=True)

        st.subheader("📈 Complaints by Category")
        st.bar_chart(df["category"].value_counts())
    else:
        st.info("No complaints have been submitted yet.")