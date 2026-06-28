"""
URL configuration for college_events project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('sports/', views.sports, name='sports'),
    path('cultural/', views.cultural, name='cultural'),
    path('symposium/', views.symposium),
    path('cs_events/', views.cs_events),
    path('paper-presentation/', views.paper_presentation),
    path('web-designing/', views.web_designing),
    path('debugging/', views.debugging),
    path('coding-contest/', views.coding_contest),
    path('technical-quiz/', views.technical_quiz),
    path('commerce-events/', views.commerce_events),
    path('business-quiz/', views.business_quiz),
    path('marketing-challenge/', views.marketing_challenge),
    path('startup-pitching/', views.startup_pitching),
    path('maths-events/', views.maths_events),
    path('math-quiz/', views.math_quiz),
    path('puzzle-solving/', views.puzzle_solving),
    path('aptitude-challenge/', views.aptitude_challenge),
    path('physics-events/', views.physics_events),
    path('science-quiz/', views.science_quiz),
    path('project-expo/', views.project_expo),
    path('innovation-challenge/', views.innovation_challenge),
    path('college-day/', views.college_day, name='college_day'),
    path('status/', views.check_status),
    path('cricket/', views.cricket, name='cricket'),
    path('football/', views.football, name='football'),
    path('volleyball/', views.volleyball, name='volleyball'),
    path('kabaddi/', views.kabaddi, name='kabaddi'),
    path('athletics/', views.athletics, name='athletics'),
    path('chess/', views.chess, name='chess'),
    path('badminton/', views.badminton, name='badminton'),
    path('solo_dance/', views.solo_dance, name='solo_dance'),
    path('group_dance/', views.group_dance, name='group_dance'),
    path('singing/', views.singing, name='singing'),
    path('mime/', views.mime, name='mime'),
    path('drama/', views.drama, name='drama'),
    path('photography/', views.photography, name='photography'),
    path('short_film/', views.short_film, name='short_film'),
    path('dashboard/', views.dashboard, name='dashboard'),
    ]
