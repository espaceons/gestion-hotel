from django.shortcuts import redirect, render
from room.models import Room
from room.forms import RoomForm
# create your views here


def index(request):
    room = Room.objects.all()
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Room:index')
    context = {
        'room': room,
        'form': form,
    }
    return render(request, 'room/index.html', context)


def update(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('Room:index')
    context = {
        'room': room,
        'form': form,
    }
    return render(request, 'room/update.html', context)
