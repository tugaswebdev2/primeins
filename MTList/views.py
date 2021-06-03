from django.shortcuts import render, redirect
#from django.http import HttpResponse
from MTList.models import CompanyProfile, CompanyEmployee, MedicalOffers, MedicalHistoryRecord, Appointment
import git
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("test.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
        
def home_page(request):
    companyemployee = CompanyEmployee.objects.all()
    return render(request, 'homepage.html',{'companyemployee' : companyemployee})

def view_list(request, companyprofile_id):
    companyprofile_ = CompanyProfile.objects.get(id=companyprofile_id)
    return render(request, 'form.html', {'companyprofile': companyprofile_})

def create_list(request):
    companyprofile_ = CompanyProfile.objects.create()  
    CompanyProfile.objects.create()
    return redirect(f'/MTList/{companyprofile_.id}/')

def new_item(request,companyprofile_id):
    companyprofile_ = CompanyProfile.objects.get(id=companyprofile_id)
    CompanyEmployee.objects.create()
    return redirect(f'/MTList/{companyprofile_.id}/')
'''firstmodel'''

def CEmployeedata(request):
    companyp = CompanyProfile(CName="The Hunger Games Company", CAddress="blk 123 lot 456 Sta.Lucia", TNumber="4598562388", Emailemp="hunger@gmail.com")
    companyp.save()

    companyp = CompanyProfile.objects.all()
    result = 'Printing all CompanyProfile : <br>'
    for x in companyp:
    	res += x.CName+"<br>"

    ccompanyp = CompanyProfile.objects.get(id="1")
    res += 'Printing One Entry <br>'
    res += ccompanyp.CAddress

    res += '<br> Deleting an entry <br>'
    ccompanyp.delete()

    companyp = CompanyProfile(CName="The Hunger Games Company", CAddress="blk 123 lot 456 Sta.Lucia", TNumber="4598562388", Emailemp="hunger@gmail.com")
    companyp.save()
    res += 'Updating entry <br>'

    companyp = CompanyProfile.objects.get(CName="The Hunger Games Company")
    companyp.TNumber = "4598562388"
    companyp.save()
    res = ""

    cqs = CompanyEmployee.objects.filter(CName="The Hunger Games Company")
    res += "Found : %s results<br>"%len(cqs)

    cps = CompanyProfile.objects.order_by(CAddress)
    for x in cps:
    	res += x.CName + x.CAddress +'<br>'