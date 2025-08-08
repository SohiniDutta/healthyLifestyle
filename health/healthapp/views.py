from django.shortcuts import render
from healthapp.models import contactModel,userModel
from healthapp.forms import registerForm,promptForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.hashers import make_password
from healthapp.utils import ques_answer,generate_text

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
   
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        


        try:
            validate_email(email)


            contactModel.objects.create(
                name = name,
                email = email,
                message= message
            
                )

            subject   = 'Healthy Lifestyle - Contact Form'
            message   = 'Thank You For Contacting'
            from_mail = settings.EMAIL_HOST_USER
            to        = [email]
            template  ='<p>Your Details Are Saved. We will get back to you shortly</p><p>Thanks & Regards</p><p>Healthy Lifestyle</p>'

            msg = EmailMultiAlternatives(subject=subject,body=message,from_email=from_mail,to=to)
            msg.attach_alternative(template,'text/html')
            msg.send()
            error = 'Form Submitted'

        
        except ValidationError:
            error = 'Invalid Email'
          
        return render(request,'index.html',{'error':error})

    else:
        return render(request,'index.html')

def login(request):

    if request.method == 'POST':

     
        email    = request.POST.get('email')
        password = request.POST.get('password')
        #user     = userModel.objects.get(email=email)
        #the above will throw an exception if not exists so try except has to be used except User.DoesNotExist:
        user     = userModel.objects.filter(email=email).first()
        if user:
            error='Logged In Successfully'
            request.session['username'] = user.first_name+' '+user.last_name
            request.session['id']       = user.id
            return render(request,'index.html',{'error':error})
        else:

            error='Not Registered'
            return render(request,'login.html',{'error':error})

    else:
        return render(request,'login.html')


def logout(request):
    del  request.session['username']
    del  request.session['id']
    #request.session.flush()   ---------deletes all session--  ------------------
    return render(request,'index.html')

def register(request):
    
    if request.method == 'POST':

        form = registerForm(request.POST)
        if form.is_valid():
            userform = form.save(commit=False)
            password = form.cleaned_data['password']
            userform.password = make_password(password)
            userform.save()
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'form':form,'error':'Data is not valid'})
      
    else:
        form = registerForm()
        return render(request,'register.html',{'form':form})

def bmi(request):

    return render(request,'bmi.html')

def message(request):
    form = promptForm()
    if request.method=='POST':
        form = promptForm(request.POST)
        if form.is_valid():
           
            generated = generate_text(form.cleaned_data['prompt'])
            

           # generated = ques_answer({'question':form.cleaned_data['prompt'],'context':form.cleaned_data['context']})
            return render(request,'chat.html',{'form':form,'generated':generated})
        else:

            return render(request,'chat.html',{'form':form})
    else:
         return render(request,'chat.html',{'form':form})

