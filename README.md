# Expense Tracker

A simple Flask-based web application for tracking expenses.

## Features
- Add new expenses with title, category, amount, and date.
- View a list of all recorded expenses.
- Automatically records the date of each expense.

## Technologies Used
- Flask (Python web framework)
- SQLite (Database)
- Jinja2 (Templating engine)
- HTML, CSS (Frontend)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python -c "from app import db, app; with app.app_context(): db.create_all()"
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open the app in your browser:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
- Navigate to the home page to view expenses and total spending.
- Click 'Add Expense' to add a new expense.
- Enter details and submit the form to save the expense.

## Folder Structure
```
expense-tracker/
│-- app.py  # Main Flask app
│-- templates/
│   ├── index.html  # Main page
│   ├── add_expense.html  # Form to add expenses
│-- static/
│   ├── style.css  # Stylesheets
│-- requirements.txt  # Dependencies
│-- README.md  # Project documentation
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See `LICENSE` for details.


