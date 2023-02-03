from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Couple, WeddingImage
from .forms import CoupleForm, WeddingImagesForm

def home(request):
    couples = Couple.objects.all()
    weddingImages = WeddingImage.objects.all()
    return render(request, 'willyou/home.html', {'couples': couples, 'weddingImages': weddingImages})

def create(request):
    ImageFormSet = modelformset_factory(WeddingImage, form=WeddingImagesForm, extra=5)
    if request.method == 'POST':
        coupleForm = CoupleForm(request.POST)
        print(f'request.FILES : {request.FILES}')
        weddingImagesFormSet = ImageFormSet(request.POST, request.FILES, queryset=WeddingImage.objects.none())
        # print(f'******* {weddingImagesFormSet}')
        if coupleForm.is_valid() and weddingImagesFormSet.is_valid():
            couple = coupleForm.save()
            print(f'weddingImagesFormSet : {weddingImagesFormSet}')
            for form in weddingImagesFormSet.cleaned_data:
                print(f'form : {form}')
                if form:
                    print(f'entered if form')
                    weddingImage = form['image']
                    weddingPhoto = WeddingImage(couple=couple, image=weddingImage)
                    print(f'weddingPhoto : {weddingPhoto}')
                    weddingPhoto.save()
            return redirect('home')
    else:
        coupleForm = CoupleForm()
        weddingImagesFormSet = ImageFormSet(queryset=WeddingImage.objects.none())

    return render(request, 'willyou/create.html', {'coupleForm': coupleForm, 'weddingImagesFormSet': weddingImagesFormSet})