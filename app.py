from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# File path to store the contact form data
data_file_path = 'contact_data.txt'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Print the data to the console
        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")

        # Store the data in a text file
        with open(data_file_path, 'a') as file:
            file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")

        return redirect('/#contact')  # Redirect back to the contact section

if __name__ == '__main__':
    app.run(debug=True)

