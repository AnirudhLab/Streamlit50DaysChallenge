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

### Day 2: Simple Calculator – Basic Arithmetic with User Inputs

- **Frontend:** Streamlit
- **Backend:** Flask (runs in a background thread)
- **Features:**
  - Users can input two numbers and select an arithmetic operation (Add, Subtract, Multiply, Divide).
  - Streamlit sends the calculation request to the Flask backend.
  - Flask performs the calculation and returns the result or an error (e.g., division by zero).
  - Streamlit displays the result or error message.
  - Uses Streamlit’s `st.cache_resource` to cache calculation results for repeated inputs.
  - Footer credits.

**Implementation Details:**
- The Flask backend exposes a `/calculate` POST endpoint that accepts JSON with `a`, `b`, and `operation`.
- The Streamlit frontend collects user input and sends it to the Flask backend using `requests.post`.
- Results are cached using `@st.cache_resource` for efficiency.
- The UI is organized with titles, markdown, and result/error display.

---

## 🛠️ How to Run

### To run with Streamlit (recommended for full demo):

```sh
streamlit run 01_helloWorld.py
streamlit run 02_calculator.py
```

### To run Flask only:

```sh
python 01_helloWorld.py
python 02_calculator.py
```

---

## 👨‍💻 Author

Created by Anirudh

---

## 📌 License

This project is for educational purposes.