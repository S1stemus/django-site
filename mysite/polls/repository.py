from .models import Question, Choice

def get_last_5_questions():
    return Question.objects.order_by('-pub_date')[:5]