from django import forms
from django.forms import ModelForm
from .models import ProgressReport, WeeklyReport, ServiceUser, House, StaffMember

class add_daily_report(ModelForm):
    class Meta:
        model = ProgressReport
        fields = ['date','content_of_one_to_one_support','evaluation_and_comments',]
        localized_fields = ('date',)

class add_weekly_report(ModelForm):
    class Meta:
        model = WeeklyReport
        fields = ['service_user', 'date', 'morning', 'evening','week_number','daily_total_one_to_one_support_hours_provided']
        localized_fields = ('date',)

class show_daily_report(forms.Form):
    date_start = forms.DateField()
    date_end = forms.DateField()

class show_weekly_report(forms.Form):
    user = forms.ModelChoiceField(queryset=ServiceUser.objects.all(),)
    date_start = forms.DateField()
    date_end = forms.DateField()