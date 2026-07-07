from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # You can process/store the data here
        return render_template('success.html', name=name)

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)