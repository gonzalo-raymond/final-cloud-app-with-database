from django.contrib import admin
from django import forms
from .forms import QuestionForm
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Register QuestionInline and ChoiceInline classes here

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 4

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):

    inlines = [LessonInline]
    list_display = ('name', "description", "instructor")
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', "course")

class QuestionAdmin(admin.ModelAdmin):

    inlines = [ChoiceInline]
    list_display = ("id", "question_text", "grade", "lesson", "course")

    form = QuestionForm

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "choice_text", "is_correct")

# Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)
