from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"profiles", views.UserProfileViewSet)
router.register(r"subjects", views.SubjectViewSet)
router.register(r"courses", views.CourseViewSet)
router.register(r"enrollments", views.EnrollmentViewSet)
router.register(r"grades", views.GradeViewSet)
router.register(r"timetables", views.TimetableEntryViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

