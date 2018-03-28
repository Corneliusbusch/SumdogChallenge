from flask import Flask, request, Response, jsonify
from QuestionGenerator import *
from HelperClasses import *

app = Flask(__name__)


@app.route('/generate_addition')
def generate_addition():

    # Parse arguments from the url
    start = request.args.get('start')
    end = request.args.get('end')

    # Check for mal-formed requests
    if start.isdigit() and end.isdigit():

        if (0 <= int(start) <= 1000000) and (0 <= int(end) <= 1000000) and (int(start) <= int(end)):
            return json.dumps(generate_question(int(start), int(end)), cls=CustomEncoder)

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
