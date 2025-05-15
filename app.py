from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this in production

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    if request.method == 'POST':
        name = request.form.get('name')
        reservation_code = request.form.get('reservation_code')
        if not name or not reservation_code:
            flash('Please fill in all fields.', 'danger')
            return redirect(url_for('checkin'))
        # Here you would add logic to verify reservation
        flash('Check-in successful! Welcome, {}.'.format(name), 'success')
        return redirect(url_for('landing'))
    return render_template('checkin.html')

if __name__ == '__main__':
    app.run(debug=True) 