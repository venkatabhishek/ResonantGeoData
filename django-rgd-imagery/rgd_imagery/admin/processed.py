from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from rgd.admin.mixins import MODIFIABLE_FILTERS, TASK_EVENT_FILTERS, TASK_EVENT_READONLY, reprocess
from rgd_imagery.models import ConvertedImageFile, SubsampledImage


@admin.register(ConvertedImageFile)
class ConvertedImageFileAdmin(OSMGeoAdmin):
    list_display = (
        'id',
        'source_image',
        'status',
        'modified',
        'created',
    )
    readonly_fields = ('converted_file',) + TASK_EVENT_READONLY
    actions = (reprocess,)
    list_filter = MODIFIABLE_FILTERS + TASK_EVENT_FILTERS


@admin.register(SubsampledImage)
class SubsampledImageAdmin(OSMGeoAdmin):
    list_display = (
        'id',
        'source_image',
        'sample_type',
        'status',
        'modified',
        'created',
    )
    readonly_fields = ('data',) + TASK_EVENT_READONLY
    actions = (reprocess,)
    list_filter = MODIFIABLE_FILTERS + TASK_EVENT_FILTERS