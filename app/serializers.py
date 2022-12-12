from rest_framework import serializers
from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['id','name' , 'email' , 'batch' , 'age','fees','date']

    def update(self, instance, validated_data): 
        instance.name = validated_data.get('name', instance.name)
        instance.batch = validated_data.get('batch', instance.batch)
        instance.age = validated_data.get('age', instance.age)
        instance.fees = validated_data.get('fees', instance.fees)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance