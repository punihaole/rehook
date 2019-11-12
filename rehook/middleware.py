def get_client_ip(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0]
    else:
        ip = request.META['REMOTE_ADDR']
    return ip.strip()


def get_client_proto(request):
    if 'HTTP_X_FORWARDED_PROTO' in request.META:
        proto = request.META['HTTP_X_FORWARDED_PROTO']
    else:
        proto = request.scheme
    return proto


def get_client_host(request):
    if 'HTTP_X_FORWARDED_HOST' in request.META:
        host = request.META['HTTP_X_FORWARDED_HOST']
    else:
        host = request.get_host()
    return host


class RemoteMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def before_request(self, request):
        request.remote_ip = get_client_ip(request)
        request.remote_scheme = get_client_proto(request)
        request.remote_host = get_client_host(request)

    def after_response(self, request, response):
        pass

    def __call__(self, request):
        self.before_request(request)
        response = self.get_response(request)
        self.after_response(request, response)
        return response
