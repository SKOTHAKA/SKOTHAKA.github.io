from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'datauser123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usersdata.db'
db = SQLAlchemy(app)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)
    college = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    degree_status = db.Column(db.String(20), nullable=False)
    domain = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    terms = db.Column(db.Boolean, nullable=False)
    resume_agree = db.Column(db.Boolean, nullable=False)
    queries = db.Column(db.Text, nullable=True)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        contact_no = request.form['contact_no']
        college = request.form['college']
        gender = request.form['gender']
        degree = request.form['degree']
        degree_status = request.form['degree_status']
        domain = request.form['domain']
        source = request.form['source']
        country = request.form['country']
        terms = request.form.get('terms') is not None
        resume_agree = request.form.get('resume_agree') is not None
        queries = request.form['queries']

        new_registration = Registration(
            email=email, name=name, contact_no=contact_no, college=college,
            gender=gender, degree=degree, degree_status=degree_status, domain=domain,
            source=source, country=country, terms=terms, resume_agree=resume_agree, queries=queries
        )

        try:
            db.session.add(new_registration)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except:
            flash('An error occurred during registration. Please try again.', 'danger')
            return redirect(url_for('register'))

    return render_template('land page.html')

@app.route('/front_end')
def front_end():
    return render_template('front end.html')

@app.route('/back_end')
def back_end():
    return render_template('Back End.html')

@app.route('/full_stack')
def full_stack():
    return render_template('FullStack.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/learnmore')
def learnmore():
    return render_template('LearnMore.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)