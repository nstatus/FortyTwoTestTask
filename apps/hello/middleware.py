from .models import Request

class LogRequestsMiddleware:
    def process_request(self, request):
        req = Request(data=request.method+" "+request.build_absolute_uri())
        req.save()
        for obj in Request.objects.all()[10:]:
            obj.delete()
        return
