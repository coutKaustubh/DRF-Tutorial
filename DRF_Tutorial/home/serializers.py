from rest_framework import serializers
from .models import Student


class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"   #brings all the field from student model
        # fields = [
        #     "Name" ,
        #     "DOB"
        # ]   explicitly aise mention or
        
        # exclude = [
        #     "id","canVote"
        # ]   exludes specicfic fields


# class CreateRecordSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ["Name", "Age", "DOB", "canVote"]


# class DeleteRecordSerializers(serializers.Serializer):
#     id = serializers.IntegerField()


