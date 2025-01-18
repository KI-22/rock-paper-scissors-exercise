import os
from flask import Flask, request, render_template, redirect, url_for
# import re

app = Flask(__name__)

#################
### CODE HERE ###
#################

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
