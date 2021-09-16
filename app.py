from flask import Flask, render_template, request
import numpy as np
from joblib import load
import pandas as pd

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/', methods=['GET', 'POST'])
def hello():
    request_type_str=request.method
    if request_type_str=='GET':
        return render_template('index.html', jcarlo='https://images.gr-assets.com/books/1476631991m/28118846.jpg')
    else:
        text = request.form['search']
        path = 'https://images.gr-assets.com/books/1363694399m/17661282.jpg'
        return render_template('index.html', jcarlo=path)