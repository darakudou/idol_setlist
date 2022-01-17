from django.contrib import admin

from core.models import Idol, Live, LiveAppearance, Setlist, Sound, Place


class IdolAdmin(admin.ModelAdmin):
    list_display = ("name", "display_name")


admin.site.register(Idol, IdolAdmin)


class SoundAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "remark")


admin.site.register(Sound, SoundAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Place, PlaceAdmin)


class LiveAdmin(admin.ModelAdmin):
    list_display = ("id", "place", "start", "end", "is_online_only")


admin.site.register(Live, LiveAdmin)


class LiveAppearanceAdmin(admin.ModelAdmin):
    list_display = ("id", "live", "idol", "stage", "start", "end")


admin.site.register(LiveAppearance, LiveAppearanceAdmin)


class SetlistAdmin(admin.ModelAdmin):
    list_display = ("id", "live_apparance", "sound", "is_mc", "order")


admin.site.register(Setlist, SetlistAdmin)
