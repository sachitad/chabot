import json
from datetime import datetime

from django.views.generic import TemplateView
from django.shortcuts import HttpResponse

bot_response = {'What"s your name?': '',
                'When were you born?': '',
                'Are you male or female?': '',
                'Are you a smoker': '',
                }


class IndexPage(TemplateView):
    template_name = 'chat/chat.html'


answers = []


def chat(request):
    questions = ["Hello, I am going to ask you few questions "
                 "that will help me know you better?",
                 "What is your name?",
                 'Are you male or female?',
                 'When were you born?',
                 'Are you a smoker?',
                 'Thank you. Press Done for Results']

    if request.is_ajax():

        # Page loads for the first time, send some greetings
        if request.GET.get('onload'):
            # Fire up 2 questions after page load
            return HttpResponse(
                json.dumps(questions[:2]))

        message = request.GET.get('message')
        done = request.GET.get("done")
        if done:
            if answers[3] == 'Yes':
                status = 'smoker'
            elif answers[3] == 'No':
                status = 'Non-smoker'
            else:
                status = 'smoker status: unknown'
            data = '{} was born in {} and is {} {}'.format(answers[0],
                                                           answers[2],
                                                           answers[1], status)
            return HttpResponse(data)
        answers.append(message)
        question = questions[int(request.GET.get('count')) + 1]
        print(answers)
        return HttpResponse(
            json.dumps({'message': message, 'question': question}))
