from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    op = data.get('operation')
    result = None
    error = None

    try:
        if op == 'Add':
            result = a + b
        elif op == 'Subtract':
            result = a - b
        elif op == 'Multiply':
            result = a * b
        elif op == 'Divide':
            if b == 0:
                error = "Division by zero!"
            else:
                result = a / b
        else:
            error = "Invalid operation"
    except Exception as e:
        error = str(e)

    return jsonify({'result': result, 'error': error})

def run_flask_app():
    app.run(port=5006, debug=False, use_reloader=False)

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

    st.title("Day 2: Simple Calculator")
    st.markdown("## Streamlit50DaysChallenge - Calculator")
    st.markdown("---")

    a = st.number_input("Enter first number (a):", value=0.0)
    b = st.number_input("Enter second number (b):", value=0.0)
    operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

    @st.cache_resource
    def calculate_backend(a, b, operation):
        url = "http://127.0.0.1:5006/calculate"
        try:
            resp = requests.post(url, json={'a': a, 'b': b, 'operation': operation}, timeout=3)
            if resp.status_code == 200:
                return resp.json()
            else:
                return {'result': None, 'error': f"HTTP {resp.status_code}"}
        except Exception as e:
            return {'result': None, 'error': str(e)}

    if st.button("Calculate"):
        result = calculate_backend(a, b, operation)
        if result['error']:
            st.error(f"Error: {result['error']}")
        else:
            st.success(f"Result: {result['result']}")

    st.markdown("---")
    st.markdown(
        "<div style='text-align: right; color: gray;'>Created by Anirudh</div>",
        unsafe_allow_html=True
    )
else:
    app.run(port=5006, debug=True)