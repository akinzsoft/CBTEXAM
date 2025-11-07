from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


    
class Profile(models.Model):
    ROLE_CHOICES = (
        ('User', 'User'),
        ('Admin', 'Admin'),
        ('Moderator', 'Moderator'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='img/avatars/avatar-4.jpg')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=10, choices=(('Male','Male'), ('Female','Female')), blank=True)
    marital_status = models.CharField(max_length=20, choices=(('Single','Single'),('Married','Married')), blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='User')

    def __str__(self):
        return self.user.username
    
    
class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    @property
    def total_questions(self):
        """
        Returns the number of questions linked to this course.
        """
        return self.questions.count()  # related_name in Question model


# ========================
# Question Model
# ========================
class Question(models.Model):
    course = models.ForeignKey(
        Course,
        related_name="questions",  # allows course.questions.count()
        on_delete=models.CASCADE
    )
    text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    mrk=models.CharField(max_length=200, default="0")
    correct_option = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
        ]
    )

    def __str__(self):
        return f"{self.course.title} - {self.text[:50]}..."
    
    
    
class CBTExam(models.Model):
    title = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.title
    
    
class ScholarshipProgram(models.Model):
    title = models.CharField(max_length=200)
    passing_score = models.PositiveIntegerField()
    exam_date = models.DateField()
    cbt_exam = models.ForeignKey(CBTExam, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tquestion = models.CharField(max_length=200, default="100")
    starttime=models.TextField(default="00:00")
    endtime=models.TextField(default="00:00")
    examduration = models.IntegerField(default=0) 

    def __str__(self):
        return self.title
    

 
 
class ScholarshipApplicant(models.Model):
    # Personal Information
    name = models.CharField(max_length=128, null=True, blank=True)
    country = models.CharField(max_length=100, default="Nigeria")
    gender = models.CharField(max_length=20, null=True, blank=True, choices=[("Male", "Male"), ("Female", "Female")])
    maritalstatus = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=[("Single", "Single"), ("Married", "Married"), ("Divorced", "Divorced")]
    )
    phoneno = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    lga = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    # Academic Information
    school_name = models.CharField(max_length=200, null=True, blank=True)
    level_of_study = models.CharField(max_length=100, null=True, blank=True)
    field_of_study = models.CharField(max_length=100, null=True, blank=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    scholarship_type = models.CharField(max_length=100, null=True, blank=True)
    essay = models.TextField(null=True, blank=True)
    previous_awards = models.TextField(null=True, blank=True)

    # Referee Information
    referee_name = models.CharField(max_length=128, null=True, blank=True)
    referee_contact = models.CharField(max_length=128, null=True, blank=True)
    wardname = models.CharField(max_length=500, null=True, blank=True)
    community = models.CharField(max_length=500, null=True, blank=True)
   
    # 📌 NEW: Link to Scholarship Program
    scholarship = models.ForeignKey(
        "ScholarshipProgram",  # assumes you have a ScholarshipProgram model
        on_delete=models.CASCADE,
        related_name="applicants",
        null=True,
        blank=True
    )

    # Documents & Hobbies dcard=files.get("passport_photo"),
    

    result = models.FileField(upload_to="results/", null=True, blank=True)
    passport_photo = models.ImageField(upload_to="photos/", null=True, blank=True)
    idcard = models.ImageField(upload_to="idcardphotos/", null=True, blank=True)
    lgacert = models.ImageField(upload_to="lgacertphotos/", null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    regdate = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name or "Unnamed Applicant"

        


class StudentCBTAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(ScholarshipProgram, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(
        max_length=1,
        choices=[('A','Option A'),('B','Option B'),('C','Option C'),('D','Option D')]
    )
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0) 
    submitted_at = models.DateTimeField(auto_now_add=True)
