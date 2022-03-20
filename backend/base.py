from flask import Flask
from interviewapi.interviewapi_client import InterviewapiClient
from interviewapi.models import interviewer
from interviewapi.exceptions.api_exception import APIException
import random
import json

api = Flask(__name__)
client = InterviewapiClient()

@api.route('/questions')
def get_question():
    try:
        controller = client.random_inteviewer
        result = json.loads(controller.interview())
        response_body = random.choice(result)
        return response_body
    except APIException as e:
        print(e)
