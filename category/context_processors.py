
# Custom Imports : - 

from category.models import Category

# Main Code : -

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)