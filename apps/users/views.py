from django.contrib.auth import login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_GET
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import RegisterSerializer

@require_GET
@ensure_csrf_cookie
def csrf_token_view(request):
    # Ensure the session is created
    if not request.session.session_key:
        request.session.create()
    
    # Retrieve the CSRF token
    csrf_token = get_token(request)

    response = JsonResponse({'csrfToken': csrf_token})
    
    # # Set the CSRF token in the cookie explicitly
    # response.set_cookie('csrftoken', '12345')
    
    return JsonResponse({'csrfToken': csrf_token})

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()  # Required by the view
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)

        
