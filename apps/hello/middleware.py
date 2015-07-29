from .models import Request

class LogRequestsMiddleware:
    def process_request(self, request):
        print request.method, request.build_absolute_uri()
        req = Request(data=request.method+" "+request.build_absolute_uri())
        req.save()
        return
