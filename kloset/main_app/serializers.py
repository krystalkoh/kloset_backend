from rest_framework import serializers
from .models import Clothes
from .models import Users

##tells which data to use to serialize the data
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'
        # excludes= ['completed',]

##validating title .. can validate_completed etc.
    # def validate_title(self, value): #value parameter is what you're validating -- must name it as value
    #     if len(value) < 5:
    #         raise serializers.ValidationError('Title has to be at least 5 characters long')
    #
    #     return value
