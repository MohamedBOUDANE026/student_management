from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Staff, Staff_Notification, Staff_Leave


def HOME(request):
    return render(request, 'Staff/home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id=staff_id)

        context = {
            "notification": notification
        }
    return render(request, 'Staff/notification.html', context)


@login_required(login_url='/')
def NOT_MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notifications')


@login_required(login_url='/')
def APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)

        context = {
            'staff_leave_history' : staff_leave_history
        }
    return render(request, 'Staff/apply_leave.html', context)


@login_required(login_url='/')
def APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Staff.objects.get(admin = request.user.id)

        leave = Staff_Leave(
            staff_id = staff,
            data = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request, 'Successfully Sent')
    return redirect('apply_leave')

