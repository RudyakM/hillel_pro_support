from django.http import JsonResponse

# import json
# from django.http import HttpResponse
# from http import HTTPStatus
# def home(request):
#     headers = {"Content-Type": "application/json"}
#     # message = "{'message': 'hello'}"
#     data = {"message": "hello"}
#     message = json.dumps(data)
#     return HttpResponse(message, headers=headers, status=HTTPStatus.OK)


def home(request):
    data = {"message": "hello from json response"}
    return JsonResponse(data)
