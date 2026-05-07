import sqlite3

def create_connection():
    """Create a database connection to the SQLite database."""
    # This creates a file named 'assessment.db' in your project folder
    conn = sqlite3.connect('assessment.db')
    return conn

def setup_tables():
    """Create the necessary tables for questions and results."""
    conn = create_connection()
    cursor = conn.cursor()
    
    # Table for Quiz Questions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    
    # Table for Student Scores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def add_question_to_db(prompt, a, b, c, d, answer):
    """Inserts a new question into the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO questions (prompt, option_a, option_b, option_c, option_d, answer)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (prompt, a, b, c, d, answer))
    conn.commit()
    conn.close()