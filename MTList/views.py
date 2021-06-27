from django.shortcuts import render, redirect
from MTList.models import CompanyProfile, Companyemployee, MedicalOffers, MedicalHistoryRecord, Appointment
#import git
from django.views.decorators.csrf import csrf_exempt

def home_page(request):
    companyprofiles = CompanyProfile.objects.all()
    return render(request, 'form.html',{'companyprofiles' : companyprofiles})

def new_item(request):
    companyprofiled_ = CompanyProfile.objects.create(CName=request.POST['CNamed'],CAddress=request.POST['CAddressd'],Nemp=request.POST['Nempd'],Emailemp=request.POST['Emailempd'],TNumber=request.POST['TNumberd'],)
    return redirect(f'/{companyprofiled_.id}/view_list')

def view_list(request, companyprofile_id):
    companyprofile_ = CompanyProfile.objects.get(id=companyprofile_id)
    return render(request, 'employees.html', {'companyprofile': companyprofile_})

def create_list(request, companyprofile_id):
    companyprofile_ = CompanyProfile.objects.get(id=companyprofile_id)
    Companyemployee.objects.create(NPatient=request.POST['NPatientd'],EIdnumber=request.POST['EIdnumberd'],Phealth=request.POST['Phealthd'], companyp=companyprofile_)
    return redirect(f'/{companyprofile_.id}/view_list')

def edit(request, id):
    companyprofiles = CompanyProfile.objects.get(id=id)
    context = {'companyprofiles': companyprofiles}
    return render(request, 'new.html', context)

def update(request,id):
    companyprofile = CompanyProfile.objects.get(id=id)
    companyprofile.CName = request.POST['CCName']
    companyprofile.CAddress = request.POST['CCAddress']
    companyprofile.Nemp = request.POST['CNEmployee']
    companyprofile.Emailemp = request.POST['CEmail']
    companyprofile.TNumber = request.POST['CPhone']
    companyprofile.save()
    return redirect('/')

def delete(request, id):
    companyprofile = CompanyProfile.objects.get(id=id)
    companyprofile.delete()
    return redirect ('/')


'''firstmodel'''
def employed(request):
    #companyemployee = CompanyEmployee.objects.all()
    return render(request, 'employees.html')

def appointed(request):
    #companyemployee = CompanyEmployee.objects.all()
    return render(request, 'appointment.html')

def abouts(request):
    #companyemployee = CompanyEmployee.objects.all()
    return render(request, 'about.html')

def formed(request):
    #companyemployee = CompanyEmployee.objects.all()
    return render(request, 'form.html')

'''def CEmployeedata(request):
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
'''

'''@csrf_exempt
def update(request):
    if request.method == "POST":
  
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
       
        repo = git.Repo("test.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
'''  