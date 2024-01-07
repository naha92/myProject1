from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('allMembers.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def team(request):
  template = loader.get_template('team.html')
  return HttpResponse(template.render())

def projects(request):
  template = loader.get_template('projects.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())