from rest_framework import serializers

from apis.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id','created_at','updated_at']    # rof ensures this data cant be edited