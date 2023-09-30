from django.http import httpsResponse

# Create your views here.
def Home_page_view(request):
    return httpsResponse("Hello, Emarex")