class Question:
    """Represents a single quiz question."""
    def __init__(self, prompt, options, answer):
        self.prompt = prompt      # question in text
        self.options = options    # A list of choices(options)
        self.answer = answer      # The correct choice (e.g., 'A')

class Student:
    """Represents a student taking the quiz."""
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.attempts = []        # History of quiz results

class Quiz:
    """Manages the collection of questions and scoring logic."""
    def __init__(self, title):
        self.title = title
        self.questions = []       # List of Question objects

    def add_question(self, question_obj):
        """Adds a Question instance to the quiz."""
        self.questions.append(question_obj)