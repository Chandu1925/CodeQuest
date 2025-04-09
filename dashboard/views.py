import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from django.views.generic import TemplateView,ListView
from dashboard.models import PlacementOpportunity,Course,Category

from django.shortcuts import render
from django.http import JsonResponse
from .models import Course,Category
from django.views.decorators.csrf import csrf_exempt

def admin_low(request):
    return render(request,'dashboard/index.html')
    
def createplacement(request):
    return render(request,'dashboard/createplacement.html')

def updateplacement(request):
    return render(request,'dashboard/updateplacement.html')

def readplacement(request):
    return render(request,'dashboard/readplacement.html')

def viewplacement(request):
    userdata = PlacementOpportunity.objects.all()
    return render(request,'dashboard/viewplacement.html',{'userdata':userdata})

def create_placement_opportunity(request):
    if request.method == 'POST':
        try:
            data = request.POST

            placement = PlacementOpportunity.objects.create(
                company_name=data.get('company_name'),
                job_title=data.get('job_title'),
                job_description=data.get('job_description'),
                job_location=data.get('job_location'),
                employment_type=data.get('employment_type'),
                salary_range=data.get('salary_range', ''),
                qualifications=data.get('qualifications'),
                experience_required=data.get('experience_required', ''),
                skills_required=data.get('skills_required', ''),
                application_deadline=data.get('application_deadline'),
                contact_email=data.get('contact_email'),
                company_website=data.get('company_website', '')
            )
            
            return JsonResponse({'success': True, 'message': 'Placement opportunity created successfully.'})
        
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})



class view_placement(ListView):
    template_name = 'dashboard/viewplacement.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userdata = PlacementOpportunity.objects.all()
        context = {'userdata': userdata}
        return context
    
class delete_placement(APIView):
    def post (self,request):
        id=request.POST["id"]
        PlacementOpportunity.objects.filter(id=id).delete()
        return JsonResponse({"status": "pass"})



#####update####
class edit_placement(TemplateView):
    template_name = 'dashboard/updateplacement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('id')
        userdata = get_object_or_404(PlacementOpportunity, id=id)
        context['userdata'] = userdata
        return context

class update_placement(APIView):
    def post(self, request):
        try:
            # Print incoming data
            print("Received data:", request.POST)

            # Extract ID and ensure it is a valid number
            placement_id = request.POST.get('id')
            print('placement_id',placement_id)
            if not placement_id:
                print("Invalid input data. Placement ID is missing.")
                return JsonResponse({'success': False, 'message': 'Placement ID is required'}, status=400)
            
            try:
                placement_id = int(placement_id)  # Convert to an integer
            except (ValueError, TypeError):
                print("Invalid input data. Placement ID must be a valid number.")
                return JsonResponse({'success': False, 'message': 'Invalid Placement ID'}, status=400)

            # Extract other data from the request
            company_name = request.POST.get('company_name', '').strip()
            job_title = request.POST.get('job_title', '').strip()
            job_description = request.POST.get('job_description', '').strip()
            job_location = request.POST.get('job_location', '').strip()
            employment_type = request.POST.get('employment_type', '').strip()
            salary_range = request.POST.get('salary_range', '').strip()
            qualifications = request.POST.get('qualifications', '').strip()
            experience_required = request.POST.get('experience_required', '').strip()
            skills_required = request.POST.get('skills_required', '').strip()
            application_deadline = request.POST.get('application_deadline', '').strip()
            contact_email = request.POST.get('contact_email', '').strip()
            company_website = request.POST.get('company_website', '').strip()

            # Fetch the existing PlacementOpportunity object
            userdata = get_object_or_404(PlacementOpportunity, id=placement_id)
            print("Placement before update:", userdata)

            # Update the PlacementOpportunity object
            userdata.company_name = company_name
            userdata.job_title = job_title
            userdata.job_description = job_description
            userdata.job_location = job_location
            userdata.employment_type = employment_type
            userdata.salary_range = salary_range
            userdata.qualifications = qualifications
            userdata.experience_required = experience_required
            userdata.skills_required = skills_required
            userdata.application_deadline = application_deadline
            userdata.contact_email = contact_email
            userdata.company_website = company_website
            userdata.save()

            print("Placement updated successfully:", userdata)
            return JsonResponse({'success': True, 'message': 'Placement updated successfully'}, status=200)

        except Exception as e:
            print("Error updating placement:", str(e))
            return JsonResponse({'success': False, 'message': 'Error updating placement: ' + str(e)}, status=400)
    
    
#####read####
class read_placement(TemplateView):
    template_name = 'dashboard/readplacement.html'

    def get(self, request, id):
        userdata = get_object_or_404(PlacementOpportunity, id=id)
        return render(request, self.template_name, {'userdata': userdata})
    


##### siri's views
def create_course(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/create_course.html',{'categories':categories})



def edit_course(request):
    
    return render(request, 'dashboard/edit_course.html')

def edit_category(request):
    
    return render(request, 'dashboard/edit_category.html')


def read_course(request):
    
    return render(request, 'dashboard/read_course.html')

def read_category(request):
    
    return render(request, 'dashboard/read_category.html')




def create_course_opportunity(request):
    if request.method == 'POST':
        try:
            course_title = request.POST.get('course_title')
            course_description = request.POST.get('course_description')
            course_category = request.POST.get('course_category')
            course_instructor = request.POST.get('course_instructor')
            course_price = request.POST.get('course_price')
            course_level = request.POST.get('course_level')
            course_start_date = request.POST.get('course_start_date')
            course_end_date = request.POST.get('course_end_date')
            course_image = request.FILES.get('course_image')  # For handling image uploads

            # Fetch the category object
            category = Category.objects.get(category_id=course_category)

            # Create the course
            course = Course.objects.create(
                course_title=course_title,
                course_description=course_description,
                course_category=category,
                course_instructor=course_instructor,
                course_price=course_price,
                course_level=course_level,
                course_start_date=course_start_date,
                course_end_date=course_end_date,
                course_image=course_image,  # Make sure your model has an ImageField
            )

            return JsonResponse({'success': True, 'message': 'Course created successfully.'})
        
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


def category_page(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/category.html', {'categories': categories})

def create_category(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            if not name:
                return JsonResponse({'success': False, 'error': 'Category name is required.'})
            
            Category.objects.create(name=name)
            return JsonResponse({'success': True, 'message': 'Category created successfully.'})
        
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


class course_view(TemplateView):
    template_name = 'dashboard/course_view.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()
        context = {'courses':courses}
        return context    
    


class delete_course(APIView):
    def post(self, request):
        courseTitle = request.POST["course_title"]
        Course.objects.filter(course_title=courseTitle).delete()
        return JsonResponse({"status": "pass"}) 
    


      
class edit_course(TemplateView):
    template_name = 'dashboard/edit_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs.get('course_id')
        courses = get_object_or_404(Course, course_id=course_id)
        categories = Category.objects.all()  # Add this line to retrieve all categories
        context['courses'] = courses
        context['categories'] = categories  # Pass categories to the template
        return context
    

class read_course(TemplateView):
    template_name = 'dashboard/read_course.html'

    def get(self, request, course_id):
        courses = get_object_or_404(Course, course_id=course_id)
        return render(request, self.template_name, {'courses':courses})    

class category_view(TemplateView):
    template_name = 'dashboard/category_view.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context = {'category':category}
        return context    
    


class delete_category(APIView):
    def post(self, request):
        categoryName = request.POST["name"]
        Category.objects.filter(name=categoryName).delete()
        return JsonResponse({"status": "pass"}) 
    


   



class edit_category(TemplateView):
    template_name = 'dashboard/edit_category.html'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.kwargs.get('name')
        category = get_object_or_404(Category, name=name)
        categories = Category.objects.all()
        context['category'] = category
        context['categories'] = categories
        return context
    

    
class read_category(TemplateView):
    template_name = 'dashboard/read_category.html'

    def get(self, request, name):
        category = get_object_or_404(Category, name=name)
        return render(request, self.template_name, {'category':category})
    





class update_course(APIView):
    def post(self, request):
        try:
            # Print incoming data
            print("Received data:", request.POST)

            # Extract ID and ensure it is a valid number
            course_id = request.POST.get('course_id')
            print('course_id@@@@@@@@@@@@@@@@@',course_id)
            if not course_id:
                print("Invalid input data. Course ID is missing.")
                return JsonResponse({'success': False, 'message': 'Course ID is required'}, status=400)
            
            try:
                course_id = int(course_id)  # Convert to an integer
            except (ValueError, TypeError):
                print("Invalid input data. Course ID must be a valid number.")
                return JsonResponse({'success': False, 'message': 'Invalid Course ID'}, status=400)

            # Extract other data from the request
            course_id = request.POST.get('course_id', '').strip()
            course_title = request.POST.get('course_title', '').strip()
            course_description = request.POST.get('course_description', '').strip()
            course_category = request.POST.get('course_category', '').strip()
            course_instructor = request.POST.get('course_instructor', '').strip()
            course_price = request.POST.get('course_price', '').strip()
            course_level = request.POST.get('course_level', '').strip()
            course_start_date = request.POST.get('course_start_date', '').strip()
            course_end_date = request.POST.get('course_end_date', '').strip()
            course_image = request.POST.get('course_image', '').strip()
           

            # Fetch the existing Course object
            courses = get_object_or_404(Course, course_id=course_id)
            print("Course before update:", courses)

            # Update the Course object
            courses.course_id = course_id
            courses.course_title = course_title
            courses.course_description = course_description
            courses.course_category = course_category
            courses.course_instructor = course_instructor
            courses.course_price = course_price
            courses.course_level = course_level
            courses.course_start_date = course_start_date
            courses.course_end_date = course_end_date
            courses.course_image = course_image
            courses.save()

            print("Course updated successfully:", courses)
            return JsonResponse({'success': True, 'message': 'Course updated successfully'}, status=200)

        except Exception as e:
            print("Error updating Course:", str(e))
            return JsonResponse({'success': False, 'message': 'Error updating Course: ' + str(e)}, status=400)    