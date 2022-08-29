from rest_framework import serializers

from handout.models.category import Category
from handout.models.major_minor import Major, Minor
from handout.models.course import Course
from handout.models.professor import Professor
from handout.models.university import University, UniversityType
from handout.models.handout import Handout


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'logo')


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ('title')


class MinorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minor
        fields = ('title', 'major')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'logo', 'minor')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('name', 'picture', 'title')


class TypeUniSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityType
        fields = ('title')


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name', 'logo', 'type')


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