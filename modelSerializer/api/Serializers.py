from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # #to give argument explicitly
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        # fields = ['id', 'name', 'roll', 'city']
        # fields = '__all__'
        exclude = ['id']
        # #to give arguments explicitly to multiple fields
        # read_only_fields = ['name', 'roll']
        # #multiple arguments
        extra_kwargs = {'name': {'read_only': True}, 'roll': {'required': True}}

        def validate_roll(self, value):
            if value>=200:
                raise serializers.ValidationError
            return value

