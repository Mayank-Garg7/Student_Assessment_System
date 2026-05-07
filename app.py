import sys
from javascript_practice.models import Question, Student
from javascript_practice.database import setup_tables, add_question_to_db, create_connection

def main_menu():
    """Main entry point for the CLI application."""
    setup_tables()  # Ensure database tables exist at startup
    
    while True:
        print("\n--- Automated Student Assessment System ---")
        print("1. Trainer: Add a New Question")
        print("2. Student: Take the Quiz")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_new_question()
        elif choice == '2':
            run_quiz()
        elif choice == '3':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

def add_new_question():
    """Logic for the Trainer to add questions to the database."""
    print("\n--- Add New Question ---")
    prompt = input("Enter the question prompt: ")
    a = input("Option A: ")
    b = input("Option B: ")
    c = input("Option C: ")
    d = input("Option D: ")
    answer = input("Correct Answer (A/B/C/D): ").upper()
    
    add_question_to_db(prompt, a, b, c, d, answer)
    print("Question added successfully!")

def run_quiz():
    """Logic for the Student to take the assessment."""
    name = input("\nEnter your name: ")
    student = Student(name)
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    
    if not rows:
        print("No questions available. Please ask the trainer to add some.")
        return

    print(f"\nWelcome, {student.name}! Start your quiz now.")
    
    for row in rows:
        # row mapping: 0=id, 1=prompt, 2=A, 3=B, 4=C, 5=D, 6=answer
        print(f"\nQ: {row[1]}")
        print(f"A) {row[2]}  B) {row[3]}  C) {row[4]}  D) {row[5]}")
        
        # EXCEPTION HANDLING: Validating user input
        while True:
            student_answer = input("Your answer (A/B/C/D): ").upper()
            if student_answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input! Please enter A, B, C, or D.")
        
        if student_answer == row[6]:
            print("Correct!")
            student.score += 1
        else:
            print(f"Wrong! The correct answer was {row[6]}")

    print(f"\nQuiz Finished! {student.name}, your score: {student.score}/{len(rows)}")
    
    # Save result to database
    cursor.execute("INSERT INTO results (student_name, score, total) VALUES (?, ?, ?)", 
                   (student.name, student.score, len(rows)))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main_menu()