from werkzeug.local import Local, release_local


_local = Local()
request = _local('request')


class TLSRequestMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        _local.request = request

        response = self.get_response(request)
        release_local(_local)

        return response

    def process_exception(self, request, exception):
        release_local(_local)
