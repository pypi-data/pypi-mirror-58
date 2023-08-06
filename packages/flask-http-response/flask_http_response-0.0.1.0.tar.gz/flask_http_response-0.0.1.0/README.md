# Flask http response
A Flask http custom response

## Description
This is a flask http custom reponse made by flask jsonify module.

## Dependencies
Flask

## Uses
Install it by runing
- `pip install flask-http-response`

Import into your project
- `from flask_http_response import success, result, error`

Use it in your http response
- `return success.return_response(message='Successfully Completed', status=200)`

If you use any type of response without passing parameter into it. No problem it will always return a default message. For `result.return_response()` you can pass data or object as a message into it.
