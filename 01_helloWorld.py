from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

def run_flask_app():
    app.run(port=5005, debug=False, use_reloader=False)

def is_streamlit():
    import sys
    return 'streamlit' in sys.modules

if is_streamlit():
    import streamlit as st
    import requests
    import time

    flask_thread = threading.Thread(target=run_flask_app, daemon=True)
    flask_thread.start()
    time.sleep(1)  # Give Flask time to start

    st.title("Day 1: Streamlit Headers, Formatting, Markdown")
    st.markdown("## Streamlit50DaysChallenge")
    st.markdown("---")

    # Categorized output
    st.subheader("🖥️ Frontend")
    st.info("Streamlit")

    st.subheader("🛠️ Backend")
    st.info("Flask (running on port 5005)")

    st.subheader("💬 Message from Backend")
    try:
        response = requests.get('http://127.0.0.1:5005/')
        st.success(response.text)
    except Exception as e:
        st.error(f"Error connecting to Flask app: {e}")

    st.markdown("---")
    st.markdown(
        "<div style='text-align: right; color: gray;'>Created by Anirudh</div>",
        unsafe_allow_html=True
    )
else:
    app.run(port=5005, debug=True)