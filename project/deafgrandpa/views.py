from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
import json

class GrandpaView(View):
    template = 'deafgrandpa/index.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        value = json.loads(request.body.decode("utf-8")) # get the jason object with the data 

        if len(value["data"]) > 1: # check to make sure there is something in the input 

            for letter in value["data"]:
                if letter.islower() == True: # check every letter for upper case 
                    answer={
                        'msg': "I can't hear you!"}
                    return JsonResponse(answer) # return a json object

                answer={
                    'msg': "Great to hear you!"}
                return JsonResponse(answer) # return a json object
        else:
            answer={
                'msg': "You didnt even say anything!"}
            return JsonResponse(answer) # return a json object




