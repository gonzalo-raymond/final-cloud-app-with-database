# forms.py
from django import forms
from .models import Question, Lesson, Course

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get the course field from the form data
        course_field = self['course']

        # If the course field has a value, use it to filter the lessons queryset
        if course_field.value():
            course_id = course_field.value()
            self.fields['lesson'].queryset = Lesson.objects.filter(course_id=course_id)
        else:
            # If the course field is empty, show an empty queryset for the lessons field
            self.fields['lesson'].queryset = Lesson.objects.all()