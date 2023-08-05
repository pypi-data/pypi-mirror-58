from django.contrib.sessions.models import Session
from .models import Visitor
from django.contrib.auth.models import User


class OneSessionPerUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if isinstance(request.user, User):
            current_key = request.session.session_key
            if hasattr(request.user, 'visitor'):
                active_key = request.user.visitor.session_key
                if active_key != current_key:
                    Session.objects.filter(session_key=active_key).delete()
                    request.user.visitor.session_key = current_key
                    request.user.visitor.save()
            else:
                Visitor.objects.create(
                    pupil=request.user,
                    session_key=current_key,
                )

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
