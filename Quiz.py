class Quiz:
    def _init_(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question)
        answer = input("Your answer: ")
        return answer.lower()

    def run_quiz(self):
        for question, correct_answer in self.questions.items():
            user_answer = self.display_question(question)
            if user_answer == correct_answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")

    def show_score(self):
        print(f"Your score: {self.score}/{len(self.questions)}")

def main():
    quiz_questions = {
        "What is the capital of France?": "Paris",
        "Which planet is known as the Red Planet?": "Mars",
        "What is the largest mammal in the world?": "Blue Whale",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the powerhouse of the cell?": "Mitochondria",
        "What is the Capital  of the India?": "Delhi",
        "Who is the current CM of MP?": "Mohan Yadav", 
        "What is the capital of Assam?": "Dispur",
    }
    quiz = Quiz(quiz_questions)

    print("Welcome to the Quiz Game!")
    quiz.run_quiz()
    quiz.show_score()

if _name_ == "_main_":
    main()
