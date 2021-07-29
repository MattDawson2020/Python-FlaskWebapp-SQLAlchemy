from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
#implicitly declares get
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form['height_name']
    return render_template('success.html')


if __name__ == '__main__': #checks that the app is running and not being IMPORTED
    app.debug=True
    app.run()