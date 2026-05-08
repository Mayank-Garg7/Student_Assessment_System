# 🎓 Automated Student Assessment System

A modular, **Object-Oriented** command-line application designed to streamline classroom assessments and track student performance in real-time. This project serves as a practical demonstration of **Python logic-building**, **Database Management**, and **Clean Code** principles.

---

## 🚀 Overview
This system was engineered to solve a common challenge in technical training: the need for an efficient, local, and automated way to evaluate student progress. It features a dual-mode interface:
1. **Trainer Mode**: For creating and managing quiz questions stored in a persistent database.
2. **Student Mode**: For taking timed assessments with instant logic-based feedback.

---

## 🛠️ Technical Stack & Engineering Principles
This project showcases 2+ years of professional engineering and instructional experience:

* **Language**: Python 3.x.
* **Architecture**: **Object-Oriented Programming (OOP)**. Utilizes classes and encapsulation to ensure modularity and scalability.
* **Database**: **SQLite**. Implements standard SQL CRUD operations for data persistence and result tracking.
* **Error Handling**: Robust input validation and **Exception Handling** to prevent runtime failures during student interactions.
* **Version Control**: Managed via Git/GitHub following professional workflow standards.

---

## 🏗️ Folder Architecture
The project follows a **Modular Design** pattern, separating concerns between data, logic, and presentation—a core concept I teach in my Software Engineering labs:

```text
StudentAssessmentSystem/
├── models.py      # OOP definitions (Student, Question, Quiz) 
├── database.py    # SQL logic and DBMS connectivity 
├── app.py         # Main controller and CLI logic 
└── README.md      # Project documentation 
```

---

## 💎 Advanced Implementation Details
This project incorporates several high-level concepts to ensure production-like stability and academic clarity:

* **Schema Normalization**: Designed a relational database schema that separates questions from student results, ensuring data integrity and efficient querying.
* **Input Sanitization**: Implemented custom validation loops to handle edge cases in user input, preventing the application from crashing during runtime.
* **Modular Reusability**: Classes in `models.py` are designed to be independent, allowing them to be imported into other educational tools without modification.

---

## 💡 Key Features for Recruiters & Hiring Managers
* **Scalable Data Structure**: Uses list comprehensions and optimized loops for fetching and displaying quiz content.
* **Relational Database Design**: Includes a schema for tracking multiple students and their historical scores, demonstrating **DBMS** proficiency.
* **Instructor-Led Design**: Built with the pedagogical intent to demonstrate **Time Complexity** and **logic flow** to junior developers.

---

## 🔧 Installation & Usage
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mayank-Garg7/StudentAssessmentSystem.git
   ```
2. **Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Run the Application**:
   ```bash
   python app.py
   ```

---

[View Future Roadmap](./FUTURE_IMPLEMENTATION.md) | [View Security Features](./SECURITY.md)
