from django.contrib import admin

# Register your models here.
from .models import AdNetwork, Post, Advert, Country, AffiliateNetwork, Offer, CustomUser


class PostOpts(admin.ModelAdmin):
    list_filter = (
        'ad_networks__name',
        'countries__name',
        'affiliate_networks__name',
        'offers__name',
        'user__forum_name',
    )
    list_display = ('details', 'show_post_url')

    def show_post_url(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (obj.url, obj.url)
    show_post_url.allow_tags = True

# class CustomUserOpts(admin.ModelAdmin):


admin.site.register(AdNetwork)
admin.site.register(CustomUser)
admin.site.register(AffiliateNetwork)
admin.site.register(Offer)
# admin.site.register(Advert)
admin.site.register(Post, PostOpts)
admin.site.register(Country)