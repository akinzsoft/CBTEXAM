from django import forms
from .models import Profile,ScholarshipApplicant


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        
class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'gender', 'marital_status']  # your profile fields
        
        
class ScholarshipApplicantForm(forms.ModelForm):
    class Meta:
        model = ScholarshipApplicant
        fields = "__all__"   # include all fields
        #exclude = ["scholarship"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable user field
        if "user" in self.fields:
            self.fields["user"].disabled = True
            self.fields["scholarship"].disabled = True
        


