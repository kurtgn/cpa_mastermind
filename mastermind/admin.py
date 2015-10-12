from django.contrib import admin

# Register your models here.
from .models import AdNetwork, Post, Country, AffiliateNetwork, Offer, CustomUser


class PostOpts(admin.ModelAdmin):
    list_filter = (
        'ad_networks__name',
        'countries__name',
        'affiliate_networks__name',
        'offers__name',
        'user__forum_name',
    )
    list_display = (
        'user',
        'created_at',
        'details',
        'all_countries',
        'all_offers',
        'aff_networks',
        'all_ad_networks',
        'show_post_url',
    )

    def show_post_url(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (obj.url, obj.url)

    def all_countries(self, obj):
        return ', '.join(map(lambda c: c.name, obj.countries.all()))

    def all_offers(self, obj):
        return ', '.join(map(lambda c: c.name, obj.offers.all()))

    def aff_networks(self, obj):
        return ', '.join(map(lambda c: c.name, obj.affiliate_networks.all()))

    def all_ad_networks(self, obj):
        return ', '.join(map(lambda c: c.name, obj.ad_networks.all()))

    filter_horizontal = ('countries', 'affiliate_networks', 'offers', 'ad_networks')
    show_post_url.allow_tags = True
    all_countries.short_description = 'Гео'
    show_post_url.short_description = 'Ссылка'
    all_offers.short_description = 'Офферы'
    aff_networks.short_description = 'Источники'
    all_ad_networks.short_description = 'Офф.сети'
    # created_at.short_description = 'Создано'

# class CustomUserOpts(admin.ModelAdmin):


admin.site.register(AdNetwork)
admin.site.register(CustomUser)
admin.site.register(AffiliateNetwork)
admin.site.register(Offer)
# admin.site.register(Advert)
admin.site.register(Post, PostOpts)
admin.site.register(Country)