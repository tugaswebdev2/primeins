from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from MTList.views import home_page
from django.template.loader import render_to_string
from MTList.models import CompanyProfile, CompanyEmployee, MedicalOffers, MedicalHistoryRecord, Appointment

class MyMainPage(TestCase):
    
   def test_root_url_resolves_to_mainpage_view(self):
      found = resolve('/')
      self.assertEqual(found.func, home_page)
      
   
   
   def test_necessary_items_to_save(self): 
      self.client.get('/')        
      self.assertEqual(CompanyEmployee.objects.count(), 0)
      
class ViewListings(TestCase):
 
   def test_using_list_template(self):
      companyprofile_ = CompanyProfile.objects.create()        
      response = self.client.get(f'/MTList/{companyprofile_.id}/')
      self.assertTemplateUsed(response, 'form.html')
     
   
   def test_all_displaying_the_items(self):        
       companyprofile_ = CompanyProfile.objects.create()        
       #CompanyEmployee.objects.create(Phealth='Micah', companyprofile=companyprofile_)        
       #CompanyEmployee.objects.create(Phealth='Tugas', companyprofile=companyprofile_)
   
   def test_is_correct_then_passed_list_to_template(self):       
       other_companyprofile = CompanyProfile.objects.create()        
       correct_companyprofile = CompanyProfile.objects.create()        
       response = self.client.get(f'/MTList/{correct_companyprofile.id}/')
       self.assertEqual(response.context['companyprofile'], correct_companyprofile)  
 
class TestGeneratedItem(TestCase):   

 
   def test_directing_after_POST(self):        
       response = self.client.post('/MTList/new', data={'fname':'Full Name', 'depname':'My Department','kaddress':'Home Address','Reason':'Purpose','info':'Contact Information','sdate':'New Date','sign1':'Symptoms'})                     
       new_companyprofile = CompanyProfile.objects.first()        
       self.assertRedirects(response, f'/MTList/{new_companyprofile.id}/')
           
'''class TestNewAddedItem(TestCase):

   def test_saving_a_POST_request_to_an_existing_list(self):       
      other_companyprofile = CompanyProfile.objects.create()        
      correct_companyprofile = CompanyProfile.objects.create()        
      
      self.client.post(            
          f'/MTList/{correct_companyprofile.id}/add_item',            
          data={'fname':'Full Name','depname':'My Department', 'kaddress':'Home Address','Reason':'Purpose','info':'Contact Information','sdate':'New Date','sign1':'Symptoms'})
      
      self.assertEqual(CompanyEmployee.objects.count(), 1)        
      new_companyemployee = CompanyEmployee.objects.first()        
      self.assertEqual(new_companyemployee.NPatient, '')       
      self.assertEqual(new_companyemployee.companyprofile, correct_companyprofile)
      
   def test_directing_to_a_list_view(self):        
      other_companyprofile = CompanyProfile.objects.create()        
      correct_companyprofile = CompanyProfile.objects.create()        
      response = self.client.post(            
          f'/MTList/{correct_companyprofile.id}/add_item',            
         data={'fname':'Full Name', 'depname':'My Department','kaddress':'Home Address','Reason':'Purpose','info':'Contact Information','sdate':'New Date','sign1':'Symptoms'}) 
      self.assertRedirects(response, f'/MTList/{correct_companyprofile.id}/')
 '''  
'''class MyMapping(TestCase):

   def test_saving_and_retrieving_items(self):
      companyprofile_ = CompanyProfile()        
      companyprofile_.save()
      
      first_companyemployee = CompanyEmployee()        
      first_companyemployee.NPatient = 'The first (ever) list item' 
      first_companyemployee.companyprofile = companyprofile_ 
      first_companyemployee.save()        
               
      second_companyemployee = CompanyEmployee()      
      second_companyemployee.NPatient = 'Item the second'
      second_companyemployee.companyprofile = companyprofile_         
      second_companyemployee.save()
       
       
      saved_companyprofile = CompanyProfile.objects.first()          
      self.assertEqual(saved_companyprofile, companyprofile_)
                 
      saved_companyemployees = CompanyEmployee.objects.all()
      self.assertEqual(saved_companyemployees.count(), 2)
       
      first_saved_companyemployee = saved_companyemployees[0]
      second_saved_companyemployee = saved_companyemployees[1]             
      self.assertEqual(first_saved_companyemployee.NPatient, 'The first (ever) list item')
      self.assertEqual(first_saved_companyemployee.companyprofile, companyprofile_)
      self.assertEqual(second_saved_companyemployee.NPatient, 'Item the second')
      self.assertEqual(second_saved_companyemployee.companyprofile, companyprofile_)
'''
'''    def test_home_page_return_correct_html(self):
    	 request = HttpRequest()
    	 response = HomePage(request)
    	 html = response.content.decode('utf8')
    	 expected_html = render_to_string('homepage.html')
    	 self.assertEqual(html,expected_html)
    def test_save_POST_request(self):
         response = self.client.post('/', data={'fname':'address'})
         self.assertIn('fname', response.content.decode())
    	 self.assertTrue(html.startswith('<html>'))
    	 self.assertIn('<title>ECT Application</title>', html)
    	 self.assertTrue(html.endswith('</html>'))
    	 self.assertTemplateUsed(response, 'homepage.html')'''

# Create your tests here.
