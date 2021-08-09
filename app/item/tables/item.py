import django_tables2 as tables

from ..models.item import *


class ItemTable(tables.Table):
    thumbnail_url = tables.TemplateColumn(
        """
        <div><img src="{{ record.thumbnail_url }}"></div>        
        """)
    review = tables.TemplateColumn(
        """
        <!-- カルーセル矢印の装飾 -->
        <style>
        .carousel-control-prev-icon {
            background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23f00' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
        }
        .carousel-control-next-icon {
            background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23f00' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
        }
        </style>

        <!-- カルーセル実装 -->
        <div id="carouselExampleControls" class="carousel slide" data-ride="false" data-touch='true'>
            <div class="carousel-inner">
                {% for review in record.review.all %}
                    {% if forloop.first %}
                        <div class="carousel-item active">
                            <div> ★{{ review.star }}  </div>
                            <div>{{ review.title }}</div>
                            <div>{{ review.content }}</div>
                        </div>
                    {% else %}
                        <div class="carousel-item px-5">
                            <div>★{{ review.star }}</div>
                            <div>{{ review.title }}</div>
                            <div>{{ review.content }}</div>
                        </div>
                    {% endif %}
                {% endfor %}
            </div>

            <!-- カルーセル矢印 -->
            <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>
        """)
    favorite_button = tables.TemplateColumn(
    """
    <form action="{% url 'item:favorite' record.pk %}" method="get">
        <button type="submit" name="button" class='text-white bg-primary rounded-pill border-primary py-1 px-2 small'>★</button>
        {% csrf_token %}
    </form>        
    """,verbose_name='お気に入り')

    class Meta:
        model = ItemModel
        template_name = 'django_tables2/bootstrap4.html'
        orderable = False

        fields = ('thumbnail_url','name', 'yahoo_price','rakuten_price','amazon_price','yahoo_review_count','yahoo_star_average','review','favorite_button')  


class FavoriteTable(tables.Table):
    thumbnail_url = tables.TemplateColumn(
        """
        <div><img src="{{ record.thumbnail_url }}"></div>        
        """)
    review = tables.TemplateColumn(
        """
        <!-- カルーセル矢印の装飾 -->
        <style>
        .carousel-control-prev-icon {
            background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23f00' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
        }
        .carousel-control-next-icon {
            background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23f00' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
        }
        </style>

        <!-- カルーセル実装 -->
        <div id="carouselExampleControls" class="carousel slide" data-ride="false" data-touch='true'>
            <div class="carousel-inner">
                {% for review in record.review.all %}
                    {% if forloop.first %}
                        <div class="carousel-item active">
                            <div> ★{{ review.star }}  </div>
                            <div>{{ review.title }}</div>
                            <div>{{ review.content }}</div>
                        </div>
                    {% else %}
                        <div class="carousel-item px-5">
                            <div>★{{ review.star }}</div>
                            <div>{{ review.title }}</div>
                            <div>{{ review.content }}</div>
                        </div>
                    {% endif %}
                {% endfor %}
            </div>

            <!-- カルーセル矢印 -->
            <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>
        """)
    delete_favorite_button = tables.TemplateColumn(
    """
    <form action="{% url 'item:delete-favorite' record.pk %}" method="get">
        <button type="submit" name="button" class='text-white bg-danger rounded-pill border-danger px-2 small'>-</button>
        {% csrf_token %}
    </form>        
    """,verbose_name='お気に入り削除')
    class Meta:
        model = ItemModel
        template_name = 'django_tables2/bootstrap4.html'
        orderable = False

        fields = ('thumbnail_url','name', 'yahoo_price','rakuten_price','amazon_price','yahoo_review_count','yahoo_star_average','review') 