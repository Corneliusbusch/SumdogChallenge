# MathQuestionAPI

Sumdog Coding Challenge
========================

Addition question generation
-----------------------------
Our developers need to deliver maths questions in our games. We would like you to develop a
HTTP API that returns a maths question together with the correct answer and three wrong
answers in JSON.

The questions should be integer addition questions where the answer is within a range defined
by the client. For example, if the answer range is 11 to 20, one of the questions might be 7 + 8.
An error should be thrown if the client specifies a range outside of 0 and 1,000,000.
The main backend languages we use at Sumdog are Ruby and Scala. We would prefer if your
solution uses one these.


Questions:

1. What kind of libraries, if any, are we allowed to use? 
    - You can use any libraries they like.
2. Should the returned answer always be in the same format with the first answer being the correct one followed by three wrong answers or should it be randomly mixed already? 
    - Randomly mixed
3. Should the HTTP error code for "Bad Request" (400) be returned for a specified range outside of 0 and 100000 or would you prefer a more specific error code? 
    - A 400 error is fine
    
The implementation is done is Python using the Flask framework. To test the functionality of the actual task, 
please open localhost and visit the route '/generate_addition'. Add the parameters 'end' and 'start' to the url
like '/generate_addition?start=11&end=20'. The API's response will then be printed on the screen. 

The response will look similar to the the following: 

{"firstSummand": 4, "secondSummand": 12, "correct": 16, "other": [19, 16, 11, 17]}

'firstSummand' is the first number of the addition question and 'secondSummand' ist the second number. Therefore,
the question is "4 + 12". 
The field 'correct' includes the correct answers and the field 'others' a list of possible solutions.

It is assumed that the range can be widened, when creating random possible solutions, if it is not possible to 
generate four distinct solutions. Further, the API has been tested by running the possible input combinations: 

1. No parameters
2. Only one parameter given
3. start parameter greater than end parameter
4. valid parameters
5. two parameters with the same value
6. parameters out of range




