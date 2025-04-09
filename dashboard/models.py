from django.db import models

# chandan's model
class PlacementOpportunity(models.Model):
    company_name = models.CharField(max_length=255)  
    job_title = models.CharField(max_length=150)  
    job_description = models.TextField()  
    job_location = models.CharField(max_length=150)  
    employment_type = models.CharField(
        max_length=50, 
        choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Internship', 'Internship')],
        default='Full-Time'
    )  
    salary_range = models.CharField(max_length=100, blank=True, null=True)  
    qualifications = models.TextField()  
    experience_required = models.CharField(max_length=50, blank=True, null=True)  
    skills_required = models.TextField(blank=True, null=True)  
    application_deadline = models.DateField(blank=True, null=True)  
    contact_email = models.EmailField()  
    company_website = models.URLField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


# siri's models

# Category model

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)  # Explicitly defining the primary key with custom name
    name = models.CharField(max_length=100, unique=True)  # Category name
    description = models.TextField(blank=True, null=True)  # Optional description of the category
   

    def __str__(self):
        return self.name

# Course model

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)  # Explicitly defining the primary key with custom name
    course_title = models.CharField(max_length=200)  # Course title
    course_description = models.TextField()  # Full description of the course
    course_category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)  # Category relation
    course_instructor = models.CharField(max_length=200)  # Name of the instructor
    course_price = models.DecimalField(max_digits=6, decimal_places=2)  # Price of the course
    course_level = models.CharField(
        max_length=50, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')]
    )  # Difficulty level of the course
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the course was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the course was last updated
    course_start_date = models.DateField()  # Course start date
    course_end_date = models.DateField()  # Course end date (if applicable)
    course_image = models.ImageField(upload_to='courses/', blank=True, null=True)  # Optional course image

    def __str__(self):
        return self.title


