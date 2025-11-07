from django import template
from ..models import StudentCBTAnswer

register = template.Library()

@register.filter
def get_exam_taken(user, scholarship_id):
    """Returns True if the student has already taken the exam."""
    return StudentCBTAnswer.objects.filter(student=user, scholarship_id=scholarship_id).exists()
