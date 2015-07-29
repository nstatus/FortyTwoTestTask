class LogRequestsMiddleware:
    def process_request(self, request):
        print request.method, request.build_absolute_uri()
        return
