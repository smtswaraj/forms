from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from . forms import reviewForm
from . models import Review
from django.views import View
# Create your views here.

class review(View):
        def get(self,request):
            form = reviewForm()
            return render(request,'form_reviews/review.html',{'form':form})

        def post(self,request):
            form = reviewForm(request.POST)
            if form.is_valid():
                form.save()
                print(form.cleaned_data)
                return HttpResponseRedirect('thanks')
            return render(request,'form_reviews/review.html',{'form':form})


# def review(request):
#     if request.method == 'POST':
#     #     data = request.POST['Username']
#     #     if data == '':
#     #         return render(request,'form_reviews/review.html',{'error':True})
#     #     return HttpResponseRedirect('thanks')
        # form = reviewForm(request.POST)
        # if form.is_valid():
#             # print(form.cleaned_date)
            # data = Review(
            #     user_name = form.cleaned_data['user_name'],
            #     feedback = form.cleaned_data['feedback']
            # )
            # data.save()
            # form.save()
            # print(form.cleaned_data)
            
    #         return HttpResponseRedirect('thanks')
    # else:
 
    #         form = reviewForm()
    # return render(request,'form_reviews/review.html',{'form':form})
#     # return render(request,'form_reviews/review.html',{'error':False})


def thanks(request):
        # if request.method == 'POST':
        #     a = str(request.POST['nm'])
        #     if a != '':
        #         return render(request,'form_reviews/thanks.html')
        #     else:
        #         # return HttpResponse("<h1>Enter some value</h1>")
        return render(request,'form_reviews/thanks.html')