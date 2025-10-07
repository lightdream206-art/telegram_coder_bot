# app.py
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def editor_page():
    return render_template('editor.html')

if __name__ == '__main__':
    # Deploy paytida portni muhit o'zgaruvchisidan olish muhim
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
