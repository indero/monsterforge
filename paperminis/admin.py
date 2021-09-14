from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User, Bestiary, Creature, CreatureQuantity


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


class BestiaryInline(admin.TabularInline):
    model = CreatureQuantity
    extra = 1
    exclude = ('owner',)

    def get_formset(self, request, obj=None, **kwargs):
        self.parent_obj = obj
        return super(BestiaryInline, self).get_formset(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        parent = self.parent_obj
        if db_field.name == "creature":
            kwargs["queryset"] = Creature.objects.filter(owner=parent.owner)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    list_display = ('owner', 'id', 'name', 'size', 'img_url')
    list_filter = ['size']
    fields = ['owner', 'name', 'img_url', 'size']


@admin.register(Bestiary)
class CreatureAdmin(admin.ModelAdmin):
    list_display = ('owner', 'id', 'name')
    fields = ['owner', 'name']
    inlines = [BestiaryInline]


@admin.register(CreatureQuantity)
class CreatureQuantityAdmin(admin.ModelAdmin):
    list_display = ('owner', 'id', 'creature', 'bestiary')
