# Django Tree Menu

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-3.2+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

Django Tree Menu - это reusable приложение для создания и отображения древовидных меню в Django проектах. Позволяет создавать многоуровневые меню, которые можно редактировать через стандартную админку Django.

## Особенности

- 🏷️ Поддержка нескольких независимых меню на одном сайте
- 🌳 Древовидная структура с неограниченной вложенностью
- 🔗 Поддержка как прямых URL, так и именованных URL (named URLs)
- 🎯 Автоматическое определение активного пункта по текущему URL
- ⚡ Всего 1 запрос к БД для отрисовки меню
- 💻 Удобное управление через стандартную админку Django
- � Гибкая система CSS-классов для стилизации

## Установка

1. Копируйте приложение в проект:

2. Добавьте приложение в `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'tree_menu',
    ...
]
```

3. Выполните миграции:

```bash
python manage.py migrate
```

## Использование

1. Создайте меню через админку Django (`/admin/tree_menu/menu/`)
2. Добавьте пункты меню с указанием родительских элементов
3. В шаблоне используйте template tag для отображения меню:

```html
{% load tree_menu_tags %}

<!-- Основное меню -->
<nav>{% draw_menu 'main_menu' %}</nav>

<!-- Боковое меню -->
<aside>{% draw_menu 'sidebar_menu' %}</aside>
```

## Пример структуры меню

```
Основное меню (main_menu)
├── Главная (/)
├── О компании
│   ├── История (/about/history/)
│   └── Команда (/about/team/)
└── Услуги
    ├── Разработка (/services/development/)
    └── Дизайн (/services/design/)

Боковое меню (sidebar_menu)
├── Блог (blog)
└── Контакты (/contacts/)
```

## Настройка отображения

Приложение добавляет следующие CSS-классы для стилизации:

- `.menu` - основной контейнер меню
- `.menu-item` - пункт меню
- `.active` - активный пункт меню
- `.has-active-child` - пункт, содержащий активный дочерний элемент
- `.submenu` - контейнер подменю
- `.submenu-item` - пункт подменю

Пример CSS:

```css
.menu {
    list-style: none;
    padding: 0;
}

.menu-item a {
    display: block;
    padding: 8px 12px;
    text-decoration: none;
    color: #333;
}

.menu-item.active > a,
.submenu-item.active > a {
    font-weight: bold;
    color: #0066cc;
}

.submenu {
    padding-left: 20px;
    list-style: none;
}
```

## Логика отображения

1. Все родительские пункты активного элемента развернуты
2. Непосредственные дети активного пункта развернуты
3. Остальные ветви свернуты

## Тестирование

Для запуска тестов:

```bash
python manage.py test tree_menu
```

## Лицензия

MIT License. Смотрите файл [LICENSE](LICENSE) для подробной информации.

---

Разработано с ❤️ для Django сообщества. Pull requests приветствуются!