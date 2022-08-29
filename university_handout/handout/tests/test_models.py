from os import minor
from django.test import TestCase

from handout.models.category import Category
from handout.models.major_minor import Major, Minor
from handout.models.course import Course
from handout.models.professor import Professor
from handout.models.university import University, UniversityType
from handout.models.handout import Handout, get_file_path


class CategoryTest(TestCase):

    def setUp(self):
        return Category.objects.create(
            title='title1'
        )

    def test_category_creation(self):
        cat = Category.objects.get(title='title1')
        self.assertTrue(isinstance(cat, Category))
        self.assertEqual(cat.__str__(), cat.title)


class MajorTest(TestCase):

    def setUp(self):
        return Major.objects.create(
            title = 'title1'
        )

    def test_major_creation(self):
        major = Major.objects.get(title='title1')
        self.assertTrue(isinstance(major, Major))
        self.assertEqual(major.__str__(), major.title)


class MinorTest(TestCase):

    def setUp(self):
        major = Major.objects.create(
            title = 'title1'
        )
        return Minor.objects.create(
            major=major,
            title='title2'
        )

    def test_minor_creation(self):
        minor = Minor.objects.get(title='title2')
        self.assertTrue(isinstance(minor, Minor))
        self.assertEqual(minor.__str__(), minor.title)



class CourseTest(TestCase):

    def setUp(self):
        major = Major.objects.create(
            title = 'title1'
        )
        minor = Minor.objects.create(
            major=major,
            title='title2'
        )
        return Course.objects.create(
            minor=minor,
            title='title3'
        )

    def test_course_creation(self):
        course = Course.objects.get(title='title3')
        self.assertTrue(isinstance(course, Course))
        self.assertEqual(course.__str__(), course.title)


class ProfessorTest(TestCase):

    def setUp(self):
        return Professor.objects.create(
            name='narjes'
        )

    def test_professor_creation(self):
        professor = Professor.objects.get(name='narjes')
        self.assertTrue(isinstance(professor, Professor))
        self.assertEqual(professor.__str__(), professor.name)


class UniversityTypeTest(TestCase):

    def setUp(self):
        return UniversityType.objects.create(
            title='sku'
        )

    def test_type_creation(self):
        type = UniversityType.objects.get(title='sku')
        self.assertTrue(isinstance(type, UniversityType))
        self.assertEqual(type.__str__(), type.title)


class UniversityTest(TestCase):

    def setUp(self):
        type = UniversityType.objects.create(
            title='sku'
        )
        return University.objects.create(
            name = 'shsku',
            type = type
        )

    def test_uni_creation(self):
        uni = University.objects.get(name='shsku')
        self.assertTrue(isinstance(uni, University))
        self.assertEqual(uni.__str__(), uni.name)


class HandoutTest(TestCase):

    def setUp(self):
        cat = Category.objects.create(
            title='title1'
        )
        major = Major.objects.create(
            title = 'title1'
        )
        minor = Minor.objects.create(
            major=major,
            title='title2'
        )
        course = Course.objects.create(
            minor=minor,
            title='title3'
        )
        return Handout.objects.create(
            title = 'titlehandout',
            category = cat,
            course = course,
            file = get_file_path('file1'),
        )
    
    def test_handout_creation(self):
        cat = Category.objects.get(title='title1')
        handout = Handout.objects.get(category=cat)
        self.assertTrue(isinstance(handout, Handout))
        self.assertEqual(handout.__str__(), handout.file.name)
