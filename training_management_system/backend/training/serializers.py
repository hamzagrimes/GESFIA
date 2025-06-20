from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Subject, Course, Enrollment, Grade, TimetableEntry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ["user", "user_type", "phone", "address", "date_of_birth", "created_at"]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source="teacher.get_full_name", read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    
    class Meta:
        model = Course
        fields = ["id", "title", "subject", "subject_name", "teacher", "teacher_name", 
                  "description", "start_date", "end_date", "is_active", "created_at"]

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.get_full_name", read_only=True)
    course_title = serializers.CharField(source="course.title", read_only=True)
    
    class Meta:
        model = Enrollment
        fields = ["id", "student", "student_name", "course", "course_title", 
                  "enrollment_date", "status"]

class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.get_full_name", read_only=True)
    course_title = serializers.CharField(source="course.title", read_only=True)
    graded_by_name = serializers.CharField(source="graded_by.get_full_name", read_only=True)
    
    class Meta:
        model = Grade
        fields = ["id", "student", "student_name", "course", "course_title", 
                  "assignment_name", "score", "max_score", "graded_by", "graded_by_name", "graded_at"]

class TimetableEntrySerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source="course.title", read_only=True)
    
    class Meta:
        model = TimetableEntry
        fields = ["id", "course", "course_title", "day_of_week", "start_time", 
                  "end_time", "room_number"]


