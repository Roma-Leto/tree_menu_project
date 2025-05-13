from django import template
from django.urls import resolve, reverse
from django.core.exceptions import ObjectDoesNotExist
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info

    try:
        menu = Menu.objects.prefetch_related('items').get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu': None}

    menu_items = menu.items.all()

    # Определяем активный пункт меню
    active_item = None
    for item in menu_items:
        if item.get_url() == current_url:
            active_item = item
            break

    # Собираем дерево меню
    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_tree(items, item)
                tree.append({
                    'item': item,
                    'children': children,
                    'is_active': active_item == item or any(
                        child['is_active'] for child in children
                    ),
                    'has_active_child': any(
                        child['is_active'] or child['has_active_child'] for
                        child in children
                    )
                })
        return tree

    menu_tree = build_tree(menu_items)

    return {
        'menu': menu,
        'menu_tree': menu_tree,
        'current_url': current_url,
    }