from flask import Flask, request, jsonify
from QuestionGenerator import QuestionGenerator
from HelperClasses import InvalidUsage

app = Flask(__name__)


@app.route('/generate_addition')
def generate_addition():

    # Parse arguments from the url
    startParam = request.args.get('start')
    endParam = request.args.get('end')

    if startParam is None or endParam is None:
        raise InvalidUsage('Bad Request')

    # Check for mal-formed requests
    if startParam.isdigit() and endParam.isdigit():

        start = int(startParam)
        end = int(endParam)

        if (0 <= start <= 1000000) \
                and (0 <= end <= 1000000) \
                and (start <= end):
            return jsonify(generate_question(start, end))

    raise InvalidUsage('Bad Request')


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def generate_question(start, end):
    # Request a question with four possible answers as described in the task
    question_generator = QuestionGenerator(4)
    return question_generator.generate_addition_question(start, end)


if __name__ == '__main__':
    app.run()
