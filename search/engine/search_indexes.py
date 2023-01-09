from haystack import indexes
from book.models import Book
class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/book_text.txt")
    title = indexes.CharField(model_attr='title')
    authors = indexes.CharField()
    def get_model(self):
        return Book
    # def prepare_title(self, obj):
    #     return [ a.title for a in Book.objects.all()]
    def index_queryset(self, using=None):
        return self.get_model().objects.all()