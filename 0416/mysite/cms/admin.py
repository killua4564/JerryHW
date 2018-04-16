from django.contrib import admin

from .models import *

class FoodInline(admin.TabularInline):
	model = Food

class PersonAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'gender', 'hobby']}),
	]
	list_display = ('id', 'name', 'gender')
	list_filter = ['name', 'gender']
	search_fields = ['name', 'gender']

class RestaurantAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'phone_number', 'address']}),
	]
	inlines = [FoodInline]
	list_display = ('id', 'name')
	list_filter = ['name']
	search_fields = ['name']

class FoodAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['restaurant', 'name', 'price', 'comment', 'is_spicy']}),
	]
	list_display = ('id', 'restaurant', 'name', 'price', 'is_spicy')
	list_filter = ['restaurant', 'name', 'price', 'is_spicy']
	search_fields = ['restaurant', 'name', 'price', 'is_spicy']

admin.site.register(Person, PersonAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)

