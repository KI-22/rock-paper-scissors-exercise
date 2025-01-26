import os
from flask import Flask, request, render_template, redirect, url_for
# import re

app = Flask(__name__)

#################
### CODE HERE ###
#################

@app.route('/index')
def get_index():
    return render_template('index.html')

@app.route('/your-move')
def get_your_move_page():
    return render_template('your_move.html')

@app.route('/your-move', methods=['POST']) ## TBC
def post_your_move():
    player_move = request.form['player_move']
    return redirect(url_for('get_result'))

@app.route('/result')
def get_result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
