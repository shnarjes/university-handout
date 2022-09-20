from rest_framework import serializers

from handout.models.handout import Handout
from handout.models.category import Category
from handout.models.professor import Professor
from handout.models.university import University


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'logo')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('name', 'picture', 'title')


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name', 'logo', 'type')


class HandoutSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    professor = ProfessorSerializer()
    university = UniversitySerializer()

    class Meta:
        model = Handout
        fields = (
            'category',
            'course',
            'file',
            'year',
            'professor',
            'university',
            'author',
            'description',
            'title',
            'logo',
            'is_processed'
            )
    

    def create(self, validated_data):
        cat_data = validated_data.pop('category')
        professor_data = validated_data.pop('professor')
        uni_data = validated_data.pop('university')
        handout = Handout.objects.create(**validated_data)
        for c in cat_data:
            Category.objects.create(handout=handout, **c)
        
        for p in professor_data:
            Professor.objects.create(handout=handout, **p)
        
        for u in uni_data:
            University.objects.create(handout=handout, **u)
        return handout
