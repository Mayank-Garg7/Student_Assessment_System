# 🛡️ Security Policy

## Supported Versions
Currently, security updates are provided for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

---

## 🔒 Security Features Implemented
This project incorporates several industry-standard security measures taught in my **Software Engineering labs**:

* **SQL Injection Prevention**: All database interactions in `database.py` use **Parameterized Queries** (`?` placeholders) rather than string formatting. This ensures that user input is never executed as code, protecting the system from malicious database manipulation.
* **Input Validation**: The system utilizes rigorous input sanitization loops to ensure that only expected data types (e.g., specific choices like A, B, C, or D) are processed.
* **Environment Isolation**: The project is designed to run within a **Python Virtual Environment**, ensuring that dependencies are managed securely and do not interfere with the host system.

---

## 🛠️ Planned Security Enhancements
As part of the **Future Implementation Roadmap**, the following security upgrades are prioritized:

* **Credential Hashing**: Implementation of the `bcrypt` or `hashlib` libraries to ensure that any future trainer credentials or sensitive student data are stored using one-way cryptographic hashes rather than plain text.
* **Database Encryption**: Exploring encryption-at-rest for the `assessment.db` file to protect student records from unauthorized physical access.
* **Role-Based Access Control (RBAC)**: Developing a secure login system to strictly separate **Trainer** (Admin) and **Student** (User) privileges.

---

## 🚩 Reporting a Vulnerability
If you discover a security vulnerability within this project, please do not report it via public issues. Instead, please follow these steps:

1.  **Email**: Contact me directly at [mayankgarg082@gmail.com](mailto:mayankgarg082@gmail.com).
2.  **Details**: Provide a detailed description of the vulnerability and steps to reproduce it.
3.  **Response**: I aim to acknowledge all security reports within **48 hours** and provide a resolution timeline shortly thereafter.
