from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
class CustomUserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = User
    list_display = ('username','address','email', 'is_staff', 'is_active',)
    list_filter = ('username','address','email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','address','email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
