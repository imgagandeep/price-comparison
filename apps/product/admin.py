# Related third-party imports
from django.apps import apps
from django.contrib import admin

# Retrieve all models from the "product" app
product_models = apps.get_app_config("product").get_models()

# Loop through each model in the "product" app and
# Register each model with Django's admin interface
for model in product_models:
    admin.site.register(model)
