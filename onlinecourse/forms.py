# forms.py
from django import forms
from .models import Question, Lesson, Course

class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['lesson'].queryset = Lesson.objects.filter(course_id = course_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['lesson'].queryset = self.instance.course.lesson_set

    class Meta:
        model = Question
        fields = ('course', 'lesson', "question_text", "grade")
        widgets = {
            'course': forms.Select(attrs = {'class': 'course-selector'}),
        }