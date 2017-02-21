from django.http import HttpResponse

def index(request, *args, **kwargs):
    # only for testing:
    print(args)
    print(kwargs)
    return HttpResponse('This is homepage.')