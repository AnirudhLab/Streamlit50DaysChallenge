# Streamlit50DaysChallenge

Welcome to the **Streamlit50DaysChallenge**!  
This repository documents my journey of learning and building with [Streamlit](https://streamlit.io/) for 50 days, often integrating it with Flask and other Python tools.

---

## 🚀 Project Overview

- **Goal:** Build and learn something new with Streamlit every day for 50 days.
- **Technologies:**  
  - [Streamlit](https://streamlit.io/) for interactive data apps  
  - [Flask](https://flask.palletsprojects.com/) for backend APIs  
  - Python standard libraries

---

## 📅 Daywise Program

### Day 1: Streamlit Headers, Formatting, Markdown, and Flask Integration

- **Frontend:** Streamlit
- **Backend:** Flask (runs in a background thread)
- **Features:**
  - Demonstrates Streamlit headers, markdown, and basic formatting.
  - Starts a Flask server in the background when running with Streamlit.
  - Streamlit fetches and displays a message from the Flask backend.
  - Categorized output for frontend, backend, and backend message.
  - Footer credits.

**Implementation Details:**
- The script checks if it is running under Streamlit.
- If yes, it starts Flask in a background thread and uses Streamlit to display categorized sections.
- If not, it runs only the Flask server.
- Uses `st.title`, `st.markdown`, `st.subheader`, `st.info`, and `st.success` for clear UI.

---

## 🛠️ How to Run

### To run with Streamlit (recommended for full demo):

```sh
streamlit run 01_helloWorld.py
```

### To run Flask only:

```sh
python 01_helloWorld.py
```

---

## 👨‍💻 Author

Created by Anirudh

---

## 📌 License

This project is for educational purposes.