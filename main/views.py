
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .EmailForm import EmailForm

BRANCH_EMAILS = {
    'CSE': 'csehod@gmail.com',
    'IT': 'ithod@gmail.com',
    'ECE': 'ecehod@gmail.com',
    'EEE': 'eeehod@gmail.com',
    'CIVIL': 'civilhod@gmail.com',
    'MECH': 'mechod@gmail.com'
}

def home(request):
    return render(request, 'home.html')

def colleges(request):
    colleges_list = ['SVEW', 'VIT', 'BVRICE']
    return render(request, 'colleges.html', {'colleges': colleges_list})

def students(request):
    students_list = [
        {'sno': 1, 'name': 'Kavya', 'branch': 'CSE', 'age': 20},
        {'sno': 2, 'name': 'Ravi', 'branch': 'ECE', 'age': 17},
        {'sno': 3, 'name': 'Anu', 'branch': 'IT', 'age': 18},
    ]
    return render(request, 'students.html', {'students': students_list})

def email(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            branch = form.cleaned_data['branch']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            to_email = BRANCH_EMAILS.get(branch)

            full_message = f"Message from: {name}\nBranch: {branch}\n\n{message}"

            send_mail(
                subject,
                full_message,
                'pranaviganta18@gmail.com',
                [to_email],
                fail_silently=False,
            )

            return HttpResponse(f"<h2>Email sent to {branch} department successfully!</h2>")
    else:
        form = EmailForm()

    return render(request, "mail_form.html", {"form": form})
    
