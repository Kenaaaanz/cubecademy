from django.contrib import admin
from .models import User, Profile, Quiz, Question, Course, Tutorial, Notes, Instructor, Announcement, Answer, Learner, LearnerAnswer

# Custom admin class for Instructor
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Customize fields to display in the admin list view
    search_fields = ('user__username',)  # Add search functionality

# Check if the Instructor model is already registered
if Instructor in admin.site._registry:
    admin.site.unregister(Instructor)

# Re-register the Instructor model with the custom admin class
admin.site.register(Instructor, InstructorAdmin)

# Register other models
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Course)
admin.site.register(Tutorial)
admin.site.register(Notes)
admin.site.register(Announcement)
admin.site.register(Answer)
admin.site.register(Learner)
admin.site.register(LearnerAnswer)

