import django_tables2 as tables

from ..models.item import *


class ItemTable(tables.Table):
    
    class Meta:
        model = ItemModel
        template_name = 'django_tables2/bootstrap4.html'
        orderable = False
        thumbnail_url = tables.TemplateColumn(
        """
        <div><img src="{{ record.thumbnail_url }}"></div>        
        """)
        review = tables.TemplateColumn(
        """
        {% for review i in record.review.all %}
            {% if i == 0 %}
                <div class="carousel-item active">
                    <div> {{ review.star }}  </div>
                    <div>{{ review.title }}</div>
                    <div>{{ review.content }}</div>
                </div>
            {% else %}
                <div class="carousel-item">
                    <div>{{ review.star }}</div>
                    <div>{{ review.title }}</div>
                    <div>{{ review.content }}</div>
                </div>
            {% endif %}
        {% endfor %}
        """)

        fields = ('name', 'thumbnail_url', 'review')  