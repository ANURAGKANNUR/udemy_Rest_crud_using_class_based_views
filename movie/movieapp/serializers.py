from rest_framework import serializers
from .models import Movie
#by using validator
def dis_lengh(value):
       if len(value)<2:
           raise serializers.ValidationError("Discrption too short!!")
       else:
           return  value
class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    discription=serializers.CharField(validators=[dis_lengh])
    active=serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.discription=validated_data.get('discription',instance.discription)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance

#field level validation
    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("Name too short!!!!")
        else:
            return value

# #object level validation
#     def validated_data(self,data):
#         if data['name']==data['discription']:
#             raise serializers.ValidationError("Name and Discription should be diffrent")
#         else:
#             return data



