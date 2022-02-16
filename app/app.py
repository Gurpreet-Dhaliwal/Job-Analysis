from flask import Flask, redirect, url_for, render_template, request, session
import json 
app = Flask(__name__)
# -------- extract data and sent to frontend ---------------------------------------------------------- #

@app.route('/', methods=['GET', 'POST'])
def mainfun():
    d = { 'title':'Title', 'data' :"dfdfdf"}
    l = [1,2,3,4,5]
    return render_template('index.html', dictionary= json.dumps(d), list= l)
       

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5001)
