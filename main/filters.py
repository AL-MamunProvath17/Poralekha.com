import django_filters
from .models import Tutor,Tution


class TutorFilter(django_filters.FilterSet):

    class Meta:
        model=Tutor
        fields={
            'address_district': ['icontains'],
            'address_covered': ['icontains'],
            'preffered_medium': ['icontains'],
            'preffered_class': ['icontains'],
            'preffered_subject': ['icontains'],
            'gender': ['icontains'],
        }

class TutionFilter(django_filters.FilterSet):

    class Meta:
        model=Tution
        fields={
            'student_location': ['icontains'],
            'student_gender': ['icontains'],
            'requirement_gender': ['icontains'],
            'requirement_teaching_time': ['icontains'],
            'student_subjects': ['icontains'],
            'salary': ['icontains'],
            'student_class': ['icontains'],
            'requirement_days_per_week': ['icontains'],
        }
