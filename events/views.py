
from .models import Registration
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    event_name = request.GET.get('event', '')

    if request.method == "POST":
        student_name = request.POST['student_name']
        college_name = request.POST['college_name']
        department = request.POST['department']
        event_name = request.GET.get('event', '')
        email = request.POST['email']
        phone = request.POST['phone']

        Registration.objects.create(
            student_name=student_name,
            college_name=college_name,
            department=department,
            event_name=event_name,
            email=email,
            phone=phone
        )

        return render(request,'success.html')

    return render(request,'register.html')

def sports(request):
    return render(request, 'sports.html')

def cultural(request):
    return render(request,'cultural.html')

def symposium(request):
    return render(request,'symposium.html')

def cs_events(request):
    return render(request,'cs_events.html')

def paper_presentation(request):
    return render(request,'paper_presentation.html')

def web_designing(request):
    return render(request,'web_designing.html')

def debugging(request):
    return render(request,'debugging.html')

def coding_contest(request):
    return render(request,'coding_contest.html')

def technical_quiz(request):
    return render(request,'technical_quiz.html')

def commerce_events(request):
    return render(request,'commerce_events.html')

def business_quiz(request):
    return render(request,'business_quiz.html')

def marketing_challenge(request):
    return render(request,'marketing_challenge.html')

def startup_pitching(request):
    return render(request,'startup_pitching.html')

def maths_events(request):
    return render(request,'maths_events.html')

def math_quiz(request):
    return render(request,'math_quiz.html')

def puzzle_solving(request):
    return render(request,'puzzle_solving.html')

def aptitude_challenge(request):
    return render(request,'aptitude_challenge.html')

def physics_events(request):
    return render(request,'physics_events.html')

def science_quiz(request):
    return render(request,'science_quiz.html')

def project_expo(request):
    return render(request,'project_expo.html')

def innovation_challenge(request):
    return render(request,'innovation_challenge.html')

def college_day(request):
    return render(request, 'college_day.html')

def check_status(request):

    status = None

    if request.method == "POST":

        email = request.POST['email']

        try:
            student = Registration.objects.get(email=email)
            status = student.status

        except:
            status = "No Registration Found"

    return render(request,'status.html',
                  {'status':status})

def cricket(request):
    return render(request, 'cricket.html')

def football(request):
    return render(request, 'football.html') 

def volleyball(request):
    return render(request, 'volleyball.html')                 

def kabaddi(request):
    return render(request, 'kabaddi.html')

def athletics(request):
    return render(request, 'athletics.html')

def chess(request):
    return render(request, 'chess.html')

def badminton(request):
    return render(request, 'badminton.html') 

def solo_dance(request):
    return render(request, 'solo_dance.html')   

def group_dance(request):
    return render(request, 'group_dance.html')   

def singing(request):
    return render(request, 'singing.html')

def mime(request):
    return render(request, 'mime.html')    

def photography(request):
    return render(request, 'photography.html')       

def short_film(request):
    return render(request, 'short_film.html')  

def drama(request):
    return render(request, 'drama.html')  

def contact(request):
    return render(request, 'contact.html')  

from .models import Registration

from .models import Registration

def dashboard(request):

    total = Registration.objects.count()
    approved = Registration.objects.filter(status="Approved").count()
    pending = Registration.objects.filter(status="Pending").count()
    rejected = Registration.objects.filter(status="Rejected").count()

    sports = Registration.objects.filter(department="Sports").count()
    symposium = Registration.objects.filter(department="Computer Science").count() + \
                 Registration.objects.filter(department="Commerce").count() + \
                 Registration.objects.filter(department="Mathematics").count() + \
                 Registration.objects.filter(department="Physics").count()

    cultural = Registration.objects.filter(department="Cultural").count()
    college_day = Registration.objects.filter(department="College Day").count()
    recent = Registration.objects.all().order_by('-id')[:5]

    context = {
        'total': total,
        'approved': approved,
        'pending': pending,
        'rejected': rejected,
        'sports': sports,
        'symposium': symposium,
        'cultural': cultural,
        'college_day': college_day,
        'recent' : recent,
    }

    return render(request, 'dashboard.html', context)
