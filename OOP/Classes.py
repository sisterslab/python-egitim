class Questions:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.index = 0

    def increaseScore(self):
        self.score += 100

    def getQuestionInfo(self):
        return self.questions[self.index]

    def showQuestion(self):
        question_info = self.getQuestionInfo()

        print(f"Soru {self.index + 1}: {question_info.question}")

        for i in question_info.choices:
            print("--> " + i)

        user_answer = input("Lütfen cevabınızı giriniz: ")
        if question_info.checkAnswer(user_answer):
            print("Tebrikler, doğru cevap")
            self.increaseScore()
        else:
            print(f"Üzgünüz yanlış cevap verdiniz. Doğru cevap: {question_info.answer} olacaktı.")

        self.index += 1
        if len(self.questions) != self.index:
            self.showQuestion()
        else:
            print(f"Tebrikler, {self.score} puanla yarışmayı tamamladınız.")