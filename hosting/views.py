from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader, Context
from django.http import HttpResponse
from .models import ActivityInfo, ActivityPicture
from .forms import ActivityForm, Host4AcivityForm, Host4ActivityPicture, Host4HashTagForm

# Create your views here.
def main_content(request) :
    contents = ActivityInfo.objects.all();
    pictures = ActivityPicture.objects.all();
    return render(request, 'hosting/content.html', {'contents' : contents, 'pictures' : pictures})

def detail(request, pk) :
    activity = get_object_or_404(Activity, pk=pk)
    picture = ActivityPicture.objects.filter(activityIndex=pk)
    schedule = ActivitySchedule.objects.filter(activityIndex=pk)
    hash_tag = HashTag.objects.filter(activityIndex=pk)
    review = ActivityReview.objects.filter(activityIndex=pk)
    host = get_object_or_404(Host, user_id = activity.user_id)
    context = { "detail" : activity, "picture" : picture, "hashtags" : hash_tag, "reviews" : review, "host" : host, "schedules" : schedule}
    return render(request, 'hosting/activity_detail.html', context)

def host(request) :
    return render(request, 'hosting/startHosting.html', {})

def host0(request) :
    return render(request, 'hosting/host0.html', {})

def host1(request):
    return render(request,'hosting/host1.html',{})

def host2(request):
    if request.method=="POST":
        form=ActivityForm(request.POST)
        if form.is_valid():
            new_activity=form.save(commit=False)
            new_activity.save()
            return redirect('host4', pk=new_activity.pk)
    else:
        form=ActivityForm()
    return render(request,'hosting/host2.html',{'form':form})

def host4(request, pk) :
    activity = get_object_or_404(ActivityInfo, pk=pk)
    if request.method=="POST" :
        #needed forms : Host4AcivityForm Host4HashTagForm Host4ActivityPicture
        form = Host4AcivityForm(request.POST, instance=activity)
        hash_tag = Host4HashTagForm(request.POST)
        pictures = Host4ActivityPicture(request.POST)
        if form.is_valid() :
            #form save
            activity = form.save(commit = False)
            new_hash = hash_tag.save(commit = False)
            new_picture = pictures.save(commit = False)
            activity.save()
            new_hash.save()
            new_picture.save()
            return redirect('host5', pk=activity.pk)
    else :
        #needed forms
        form = Host4AcivityForm(instance = activity)
        hash_tag = Host4HashTagForm()
        pictures = Host4ActivityPicture()
    return render(request, 'hosting/host4.html', {'activity' : activity, 'hash_tag' : hash_tag, 'pictures' : pictures})

def host8(request,pk):
    activity=get_object_or_404(ActivityInfo,pk=pk)
    context={"new_activity":activity}
    return render(request,'hosting/host8.html',context)