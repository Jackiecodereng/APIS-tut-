# remove the render import its only used i pure html but add a decorator
from http import HTTPStatus

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apis.models import Student
from apis.my_serializers import StudentSerializer


# Create your views here.
@api_view(['GET'])
def students_list(request):
    students = Student.objects.all() # fetches all students now convert the data to Json
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def single_student(request ,student_id):
    student = get_object_or_404(Student, pk=student_id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['PUT'])
def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request ,student_id):
    student = get_object_or_404(Student,pk=student_id)
    student.delete()
    return Response(status=HTTPStatus.NO_CONTENT)

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.CREATED)

    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

#200 --ok ,300-redirect the user, 400- definately an error, 500 -something is bad on the server side