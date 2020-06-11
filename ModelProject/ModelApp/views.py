from django.shortcuts import render
from ModelApp.models import Job,Book

# Create your views here.
def job(request):
    job_rec = Job.objects.all()
    print("job_rec :- ")
    print(job_rec)
    print()
    print()
    job_dict = {"job_list":job_rec}
    print("job_dict :- ")
    print(job_dict)
    return render(request,"ModelApp_Template/job.html",context=job_dict)

def book(request):
    book_list = Book.objects.all()
    book_dict = {"book_list":book_list}
    return render(request,"ModelApp_Template/book.html",context=book_dict)
