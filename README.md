># `Toggle Button`
>
>      zip -r toggle.zip .
>
>[![image](https://github.com/user-attachments/assets/ae7b952f-4fe2-48c4-8a6c-1834d567a18b)](https://toggle.pythonanywhere.com/)
>[![image](https://github.com/user-attachments/assets/70fc62a8-f6a3-4a8b-b89c-ca394f598c2a)](https://toggle.pythonanywhere.com/admin/toggle_app/toggleitem/)
>
># **Material Admin**
>Material Admin is based on Google’s Material Design and supports the latest Django versions.

#### **Installation**:
1. Install Material Admin:
   ```bash
   pip install django-material-admin
   ```

2. Add `material` to `INSTALLED_APPS` in `settings.py` **before** `django.contrib.admin`:
   ```python
   INSTALLED_APPS = [
       'material',
       'django.contrib.admin',
       # other apps
   ]
   ```

3. Start the development server and check the admin interface.

---

```
TemplateSyntaxError at /admin/toggle_app/toggleitem/6/change/
Invalid filter: 'length_is'
```

### **1. Create Your Custom Filter**
1. **Define the Filter**
   Create a `templatetags` folder (if it doesn’t already exist) in your app, and include an `__init__.py` file inside it. Add a `custom_filters.py` file.

   Folder structure:
   ```
   toggle_app/
   ├── templatetags/
   │   ├── __init__.py
   │   ├── custom_filters.py
   ```

   In `custom_filters.py`, define the `length_is` filter:
   ```python
   from django import template

   register = template.Library()

   @register.filter
   def length_is(value, length):
       """Check if the length of the value is equal to the given length."""
       try:
           return len(value) == int(length)
       except (ValueError, TypeError):
           return False
   ```

---

### **2. Add to `builtins` in `settings.py`**
To make the custom filter globally available without needing to `{% load custom_filters %}` in each template, register it as a built-in template tag library.

1. In your `settings.py`, add:
   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
               "builtins": ["toggle_app.templatetags.custom_filters"],  # Add your custom filters here
           },
       },
   ]
   ```

---

### **3. Restart Your Development Server**
After making these changes, restart your Django development server to ensure the changes take effect:
```bash
python manage.py collectstatic
python manage.py runserver
```
