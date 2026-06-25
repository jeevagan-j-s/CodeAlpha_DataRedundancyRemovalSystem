# CodeAlpha_DataRedundancyRemovalSystem
# Data Redundancy Removal System

## Project Description
This project is developed as part of the CodeAlpha Cloud Computing Internship.

The system identifies and prevents duplicate data from being stored in the database. It validates each new record before insertion and only stores unique records.

## Features
- Add student records
- Check for duplicate email addresses
- Prevent redundant data storage
- Store only unique and verified records
- Simple and user-friendly interface

## Technologies Used
- Python
- Flask
- SQLite
- HTML

## Project Structure

CodeAlpha_DataRedundancySystem/
│
├── app.py
├── requirements.txt
└── templates/
    └── index.html

## How It Works
1. User enters Name and Email.
2. System checks whether the Email already exists.
3. If Email exists:
   - Shows "Duplicate Record Found!"
4. If Email does not exist:
   - Stores the record in the database.
   - Shows "Record Added Successfully!"

## Installation

Install Flask:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

## Output

### Unique Record
Record Added Successfully!

### Duplicate Record
Duplicate Record Found!

## Author
Jeevagan

## Internship
CodeAlpha Cloud Computing Internship
