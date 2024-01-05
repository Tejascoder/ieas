
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/ieas')
def land():  # put application's code here
    return render_template('base.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/submit', methods= ['POST'])
def submit():
    if request.method == 'POST':
        name= request.form['name']
        email= request.form['email']
        mob = request.form['mob']


        msg= request.form['message']


        data= {name: 'name', email: 'email', msg: 'msg'}
        print(data)
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText


        # Email credentials
        sender_email = 'ieas.pune01@gmail.com'  # Replace with the sender's email address
        receiver_email = 'amolphopase2018@gmail.com'  # Replace with the recipient's email address
        password = 'bylg qfqj udix rumw'  # Replace with the sender's email password

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'Thanks for registering, A representative will get back to you soon!!'

        # Add body to email
        body = 'Data recieved: ' + '\n' + 'Name: ' + name + '\n' + 'Email: ' + email +'\n' + 'Mobile: ' + mob +'\n' + 'Message: ' + msg
        message.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())

        return render_template('base.html')

@app.route('/courses', methods= ['GET'])
def courses():
    return render_template('courses.html')


@app.route('/contact')
def contact():  # put application's code here
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
