import random as r


class QuestionGenerator:

    def __init__(self, numberOfAnswers):
        self.numberOfAnswers = numberOfAnswers

    def generate_addition_question(self, start, end):

        # Randomly select a solution in the given range
        solution = r.randint(start, end)

        # Generate the addition question
        firstSummand = r.randint(1, solution)
        secondSummand = solution - firstSummand

        # Widen the radius of possible solutions if the
        # range is not enough for the specified answers
        if (end - start) < self.numberOfAnswers:
            end += self.numberOfAnswers
            if start > self.numberOfAnswers:
                start = 0

        others = [solution]
        # Generate the wrong solutions
        while len(others) < self.numberOfAnswers:
            current = r.randint(start, end)
            if current not in others:
                others.append(current)

        # Return the question in dictionary form
        return {"firstSummand": firstSummand, "secondSummand": secondSummand,
                "solution": solution, "answers": self.shuffle_answers(others)}

    def shuffle_answers(self, answers):
        r.shuffle(answers)
        return answers
