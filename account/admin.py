from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


# Register your models here.
class AccountAdmin(UserAdmin,admin.OSMGeoAdmin):
    list_display = ('email','username','phone','address','geom','date_joined','last_login','is_staff','is_admin','products','area')
    search_fields = ('email','username','phone')
    readonly_fields = ('id','date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)