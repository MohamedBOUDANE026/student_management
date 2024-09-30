from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import Student_views, views, Hod_views, Staff_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),


    # Login PATH
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # Profile Update
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # This is HOD Panel URL
    path('Hod/Home', Hod_views.HOME, name='hod_home'),
    path('Hod/Student/Add', Hod_views.ADD_STUDENT, name='add_student'),
    path('Hod/Student/View', Hod_views.VIEW_STUDENT, name='view_student'),
    path('Hod/Student/Edit/<str:id>', Hod_views.EDIT_STUDENT, name='edit_student'),
    path('Hod/Student/Update', Hod_views.UPDATE_STUDENT, name='update_student'),
    path('Hod/Student/Delete/<str:admin>', Hod_views.DELETE_STUDENT, name='delete_student'),

    # Staff
    path('Hod/Staff/Add', Hod_views.ADD_STAFF, name='add_staff'),
    path('Hod/Staff/View', Hod_views.VIEW_STAFF, name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_views.EDIT_STAFF, name='edit_staff'),
    path('Hod/Staff/Update', Hod_views.UPDATE_STAFF, name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>', Hod_views.DELETE_STAFF, name='delete_staff'),

    # Course
    path('Hod/Course/Add', Hod_views.ADD_COURSE, name='add_course'),
    path('Hod/Course/View', Hod_views.VIEW_COURSE, name='view_course'),
    path('Hod/Course/Edit/<str:id>', Hod_views.EDIT_COURSE, name='edit_course'),
    path('Hod/Course/Update', Hod_views.UPDATE_COURSE, name='update_course'),
    path('Hod/Course/Delete/<str:id>', Hod_views.DELETE_COURSE, name='delete_course'),

    # Subject
    path('Hod/Subject/Add', Hod_views.ADD_SUBJECT, name='add_subject'),
    path('Hod/Subject/View', Hod_views.VIEW_SUBJECT, name='view_subject'),
    path('Hod/Subject/Edit/<str:id>', Hod_views.EDIT_SUBJECT, name='edit_subject'),
    path('Hod/Subject/Update', Hod_views.UPDATE_SUBJECT, name='update_subject'),
    path('Hod/Subject/Delete/<str:id>', Hod_views.DELETE_SUBJECT, name='delete_subject'),

    # Session
    path('Hod/Session/Add', Hod_views.ADD_SESSION, name='add_session'),
    path('Hod/Session/View', Hod_views.VIEW_SESSION, name='view_session'),
    path('Hod/Session/Edit/<str:id>', Hod_views.EDIT_SESSION, name='edit_session'),
    path('Hod/Session/Update', Hod_views.UPDATE_SESSION, name='update_session'),
    path('Hod/Session/Delete/<str:id>', Hod_views.DELETE_SESSION, name='delete_session'),

    # Staff notification
    path('Hod/Staff/Send_Notification', Hod_views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),
    path('Hod/Staff/Save_Notification', Hod_views.STAFF_SAVE_NOTIFICATION, name='staff_save_notification'),

    path('Hod/Staff/Leave_view', Hod_views.STAFF_LEAVE_VIEW, name='staff_leave_view'),
    path('Hod/Staff/approve_view/<str:id>', Hod_views.STAFF_APPROVE_VIEW, name='staff_approve_view'),
    path('Hod/Staff/disapprove_view/<str:id>', Hod_views.STAFF_DISAPPROVE_VIEW, name='staff_disapprove_view'),


    # This is Staff URL
    path('Staff/Home', Staff_views.HOME, name='staff_home'),
    path('Staff/Notification', Staff_views.NOTIFICATIONS, name='notifications'),
    path('Staff/mark_as_done/<str:status>', Staff_views.NOT_MARK_AS_DONE, name='mark_as_done'),

    path('Staff/Apply_Leave',Staff_views.APPLY_LEAVE,name='apply_leave'),
    path('Staff/Apply_Leave_save',Staff_views.APPLY_LEAVE_SAVE,name='apply_leave_save'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
