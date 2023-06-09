from homepage.models import PageSettings

def page_settings(request):
    try:
        page_settings = PageSettings.objects.get(pk=1)
        return {
            'page_name': page_settings.name,
            'page_footer': page_settings.footer_text,
            'page_settings': page_settings
            }
    except:
        return {
            'page_footer': 'Created by Balázs Nagy - 2023 - All rights reserved',
            }