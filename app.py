class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    expenses = Expense.query.all()
    total = sum(exp.amount for exp in expenses)
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        amount = float(request.form['amount'])
        new_expense = Expense(title=title, category=category, amount=amount)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_expense.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
