from django.contrib import admin

from APP.models import *


class productdetails(admin.ModelAdmin):
    list_display = ("product_id","catagory_name","product_name","product_price","product_image")
    class Meta:
        model=product
admin.site.register(product,productdetails)
admin.site.register(categeroy)
admin.site.register(signupImage)
admin.site.register(LoginImage)
