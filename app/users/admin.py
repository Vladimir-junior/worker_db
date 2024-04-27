from django.contrib import admin

from users.models import User, Payouts, Position, Bonus, WorkingHours, Department


class PositionAdmin(admin.ModelAdmin):
    list_display = ["name", "employees_count"]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "manager"]

    search_fields = ["name"]


class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ["user_full_name", "date", "hours", "description"]

    search_fields = ["user__first_name", "user__last_name"]

    @admin.display(empty_value="-")
    def user_full_name(self, obj: User):
        return f'{obj.user.last_name} {obj.user.first_name}'


class UserAdmin(admin.ModelAdmin):
    list_display = ["user_full_name", "department", "position", "rate"]

    search_fields = ["first_name", "last_name"]

    @admin.display(empty_value="-")
    def user_full_name(self, obj: User):
        return f'{obj.last_name} {obj.first_name}'


class PayoutsAdmin(admin.ModelAdmin):
    list_display = ["user", "begin_date_interval", "end_date_interval", "amount", "status"]

    search_fields = ["user__first_name", "user__last_name"]

    readonly_fields = ['total_amount']




class BonusAdmin(admin.ModelAdmin):
    list_display = ["payout", "amount", "description"]



admin.site.register(Payouts, PayoutsAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(WorkingHours, WorkingHoursAdmin)
admin.site.register(User, UserAdmin)
