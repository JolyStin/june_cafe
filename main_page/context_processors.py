from .models import MainMenuItem


def main_menu_items(request):
    items = MainMenuItem.objects.filter(is_visible=True)
    return {'main_menu_items': items}
