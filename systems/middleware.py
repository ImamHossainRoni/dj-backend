from systems.thread import local_thread


class GroupMiddleware(object):
    """ This middleware used to bind request to local thread for further uses where request is not accessible like
    models or any custom file need to maintain a good architecture"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        local_thread.__setattr__('request', request)
        response = self.get_response(request)
        return response

