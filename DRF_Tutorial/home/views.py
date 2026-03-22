from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student

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

@api_view(['POST'])
def createRecord(request):
    data = request.data
    Student.objects.create(**data)
    print(data)
    return Response(
        {   "status" : True,
            "message" : "Record created"
        }
    )
    
    
@api_view(['DELETE'])
def deleteData(request ,id):
    try :
        st = Student.objects.get(id=id).delete()
        return Response(
            {   "status" : True,
                "message" : "Record Deleted"
            }
        )
    except Exception as e:
        return Response(
            {   "status" : False,
                "message" : "Record not deleted"
            }
        )
        
    