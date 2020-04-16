from django.http import JsonResponse


def ping(request):
    return JsonResponse({"ping": "pong"})


def version(request):
    return JsonResponse({"version": "0.0.1"})
