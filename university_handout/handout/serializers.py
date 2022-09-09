from rest_framework import serializers

from handout.models.handout import Handout
from handout.models.category import Category
from handout.models.professor import Professor
from handout.models.university import University


class HandoutSerializer(serializers.ModelSerializer):

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


# class MajorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Major
#         fields = ('title')


# class MinorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Minor
#         fields = ('title', 'major')


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ('title', 'logo', 'minor')


# class TypeUniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UniversityType
#         fields = ('title')
