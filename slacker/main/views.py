from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q

# Create your views here.


@login_required
def index(request):

	return render(request, 'index.html')

def group_chat(request, groupchat_id):
	gc = GroupChat.objects.filter(pk=groupchat_id).first()
	if gc != None:
		if request.method == 'GET':
			return render(request, 'group_chat.html', {'gc' : gc})
		group_message = GroupMessage(chat=gc, content=request.POST.get('content'), profile=request.user.profile)
		group_message.save()
		return redirect('group_chat', gc.id)
	#flash message chat not found 
	return redirect('index')

@login_required
def private_chat(request,profile_id):

	profile2 = Profile.objects.filter(pk=profile_id).first()
	chat = PrivateChat.objects.filter(profiles=request.user.profile).filter(profiles=profile2).distinct().first()
	print(chat)
	if chat == None:
		chat = PrivateChat()
		chat.save()
		chat.profiles.add(request.user.profile, profile2)
	if request.method == 'POST':
		message = PrivateMessage(chat=chat, content=request.POST.get('content'), profile=request.user.profile)
		message.save()
	return render(request, 'private_chat.html', {'chat' : chat, 'profile2' : profile2})

@login_required
def private_chat_by_id(request,privatechat_id):
	chat = PrivateChat.objects.filter(pk=privatechat_id).first()
	profile2 = chat.profiles.exclude(user=request.user).first()
	return redirect('private_chat', profile2.id )
