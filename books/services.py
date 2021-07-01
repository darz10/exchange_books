# logic for exchange books
from .models import Book


def getting_exchange_data(book_id, new_user):
    """Изменение владельца книги при обмене"""
    data = Book.objects.update(id=book_id, user=new_user)
    data.save()
    return data


