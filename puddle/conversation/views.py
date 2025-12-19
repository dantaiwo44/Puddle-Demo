from django.shortcuts import render

from items.models import Item
from django.shortcuts import redirect
from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations= Conversation.objects.filter(
        item=item,
        members__in=[request.user.id]
    )
    if conversations.exists():
        return redirect('conversation:conversation_detail',
                        primary_key= conversations.first().id)
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('items:item_detail',
                            primary_key=item.id)

    else:
        form = ConversationMessageForm()    

    return render(request, 'conversation/new_conversation.html',
                  {'form': form})

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(
        members__in=[request.user.id]
    )
    return render(request, 'conversation/inbox.html',
                  {'conversations': conversations})

@login_required
def conversation_detail(request, primary_key):
    conversation = Conversation.objects.filter(
        members__in=[request.user.id]).get(pk=primary_key)
    
    if request.method == 'POST':
        form= ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message= form.save(commit=False)
            conversation_message.conversation= conversation
            conversation_message.created_by= request.user
            conversation_message.save()
            conversation.save()

            return redirect('conversation:conversation_detail',
                            primary_key=primary_key)
    else:
        form= ConversationMessageForm()

    return render(request, 'conversation/detail.html',
                  {'conversation': conversation,
                   'form': form})