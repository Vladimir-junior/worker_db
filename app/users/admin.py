from django import forms
from django.contrib import admin
from django.db.models import Count, Sum
from django.contrib.auth.models import Group

from users.models import (
    User,
    Bonus,
    Payouts,
    Position,
    Department,
    WorkingHours,
)


class PositionAdmin(admin.ModelAdmin):
    list_display = ["name", "num_users"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(num_users=Count('users'))
        # print(qs.query)
        return qs

    @admin.display(empty_value="-")
    def num_users(self, obj: Position):
        return obj.num_users


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "manager", "num_users"]
    search_fields = ["name"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(num_users=Count('users'))
        # print(qs.query)
        return qs

    @admin.display(empty_value="-")
    def num_users(self, obj: Department):
        return obj.num_users


class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ["user_full_name", "date", "hours", "description"]
    search_fields = ["user__first_name", "user__last_name"]

    @admin.display(empty_value="-")
    def user_full_name(self, obj: User):
        return f'{obj.user.last_name} {obj.user.first_name}'


class UserAdmin(admin.ModelAdmin):
    list_display = ["user_full_name", "department", "position", "rate", "employee_code"]

    search_fields = ["first_name", "last_name"]

    fields = [
        "first_name",
        "last_name",
        "email",
        "position",
        "rate",
        "department",
        "employee_code",
    ]

    @admin.display(empty_value="-")
    def user_full_name(self, obj: User):
        return f'{obj.last_name} {obj.first_name}'


class BonusAdmin(admin.ModelAdmin):
    list_display = ["payout", "amount", "description"]


class BonusInlineForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

class BonusInline(admin.TabularInline):
    model = Bonus
    extra = 1
    form = BonusInlineForm

class PayoutsAdmin(admin.ModelAdmin):
    inlines = [BonusInline]
    list_display = ["user", "begin_date_interval", "end_date_interval", "total_amount", "status"]
    search_fields = ["user__first_name", "user__last_name"]
    readonly_fields = ['total_amount']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(bonuses_amount=Sum('bonuses__amount'))
        return qs



admin.site.register(Payouts, PayoutsAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(WorkingHours, WorkingHoursAdmin)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)