from django.db import models

# Create your models here.

class BookShelf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def get_books(self):
        result = self.books_set.all()
        return result

    def __str__(self):
        return self.name

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    book_shelf = models.ForeignKey(BookShelf, null=True, on_delete=models.SET_NULL) 

    def assign_to(self, shelf):
        book_shelf = BookShelf.objects.get(name=shelf)
        self.book_shelf = book_shelf
        self.save()
    
    def get_shelf(self):
        shelf = Books.objects.get(pk=self.id)
        result = shelf.book_shelf if shelf != None else 'None'
        return result
    
    def delete(self):
        self.delete()

    def __str__(self):
        return self.title