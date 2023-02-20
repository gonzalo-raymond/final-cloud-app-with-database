from django.contrib import admin
from django import forms
from .forms import QuestionForm
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

"""
class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        course_id = self.initial.get('course')

        if course_id:
            self.fields['lesson'].queryset = Lesson.objects.filter(course_id = course_id)
        else:
            self.fields['lesson'].queryset = Lesson.objects.all()
"""

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
    list_display = ('name', 'pub_date')
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
