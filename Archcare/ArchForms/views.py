from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse,HttpRequest
from django.template import Template, loader, context, RequestContext
from ArchForms.models import *
from ArchForms.forms import *
from django.forms import modelform_factory,DateField,formset_factory
# Create your views here.

def index(request):
    #template = loader.get_template("index.html")
    #c = context.Context({"title":"Archcare Intranet Portal"}
    return render(request,template_name="ArchForms/index.html",context={"title":"Archcare Intranet Portal","article":"welcome to the staff portal","brand":"Portal Home"})

def weekly_progress_report(request):
    if request.method == "POST":
        service_user_list = ServiceUser.objects.get(pk=request.POST["form-0-service_user"])
        new_weekly_report = WeeklyReport(service_user=service_user_list,date=request.POST["form-0-date"],morning=request.POST["form-0-morning"],evening=request.POST["form-0-evening"],week_number=request.POST["form-0-week_number"],daily_total_one_to_one_support_hours_provided=request.POST["form-0-daily_total_one_to_one_support_hours_provided"],)
        new_weekly_report.save()
    weekly_form = formset_factory(add_weekly_report)
    context_var = RequestContext(request,{"title":"Weekly Progress Report","form":weekly_form,"brand":"Weekly Report"})
    return render_to_response(template_name="ArchForms/weekform.html",context=context_var)

def daily_progress_report(request):
    # add post logic here
    if request.method == "POST":
        new_progress_report = ProgressReport(date=request.POST["form-0-date"],content_of_one_to_one_support=request.POST["form-0-content_of_one_to_one_support"],evaluation_and_comments=request.POST["form-0-evaluation_and_comments"])
        new_progress_report.save()
    daily_form = formset_factory(add_daily_report,)
    context_var = RequestContext(request,{"title":"Weekly Progress Report","brand":"Log Daily Progress","form":daily_form})
    return render_to_response(template_name="ArchForms/dayform.html",context=context_var)

def add_service_user(request):
    service_user = modelform_factory(ServiceUser, fields=("title","first_name","second_name","full_name","contact_phone",),)
    context_var = RequestContext(request,{"title":"Weekly Progress Report","brand":"Add Service User","form":service_user})
    return render_to_response(template_name="ArchForms/addserviceuser.html",context=context_var)

def add_staff_member(request):
    staff_member = modelform_factory(StaffMember, fields=("title","first_name","second_name","full_name","contact_phone",),)
    context_var = RequestContext(request,{"title":"Weekly Progress Report","brand":"Add Staff Member","form":staff_member})
    return render_to_response(template_name="ArchForms/addstaffmember.html",context=context_var)

def add_house(request):
    house = modelform_factory(House, fields=("address",),)
    context_var = RequestContext(request,{"title":"Weekly Progress Report","brand":"Add House","form":house})
    return render_to_response(template_name="ArchForms/addhouse.html",context=context_var)

def specify_week(request):
    week_form = formset_factory(show_weekly_report,)
    context_var = RequestContext(request,{"title":"Weekly Progress Report","brand":"Show Week Reports","getform":week_form})
    return render_to_response(template_name="Archforms/weekquery.html",context=context_var)

def show_weeks(request):
    first_date = request.GET["form-0-date_start"]
    last_date = request.GET["form-0-date_end"]
    service_user_list = ServiceUser.objects.get(pk=request.GET["form-0-user"])
    service_user_name = str(service_user_list.full_name[0])
    report_table = get_list_or_404(WeeklyReport,date__range=[first_date, last_date],service_user=request.GET["form-0-user"])
    # filtered_objects = report_table.
    context_var = RequestContext(request,{"title":"Weekly Progress Report","brand":"Show Week Reports","article":report_table})
    return render_to_response(template_name="Archforms/weekshow.html",context=context_var)

def specify_days(request):
    day_form = formset_factory(show_daily_report,)
    context_var = RequestContext(request,{"title":"Daily Progress Report","brand":"Show Day Reports","getform":day_form})
    return render_to_response(template_name="Archforms/dayquery.html",context=context_var)

def show_days(request):
    first_date = request.GET["form-0-date_start"]
    last_date = request.GET["form-0-date_end"]
    print(first_date)
    print(last_date)
    report_table = get_list_or_404(ProgressReport,date__range=[first_date, last_date])
    # filtered_objects = report_table.objects.filter(created_at__range=(first_date["form-0-date_start"], last_date["form-0-date_end"]))
    context_var = RequestContext(request,{"title":"Daily Progress Report Results","brand":"Daily Reports Results","article":report_table})
    return render_to_response(template_name="Archforms/dayshow.html",context=context_var)