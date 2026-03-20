from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view()
def index(request):
    students = ["kaustubh" , "shwetu"]
    data = {
        "status" : True,
        "Name": "Kaustubh",
        "student" : students,
    }
    return Response(data)

