from django import template
from ..models import StudentCBTAnswer

register = template.Library()

@register.filter
def get_exam_taken(user, scholarship_id):
    """
    Returns True if this user has already taken the exam.
    Ensure 'user' is a User instance, not Profile.
    """
    if not user or not user.is_authenticated:
        return False
    return StudentCBTAnswer.objects.filter(student=user, scholarship_id=scholarship_id).exists()
