from datetime import datetime

from django.dispatch import receiver
from django.dispatch import Signal

book_manipulation = Signal(providing_args=["msg"])

@receiver(book_manipulation, dispatch_uid="my_unique_identifier")
def log_book_manipulation(sender, **kwargs):
    print kwargs['msg']
    f = open("book_store/book_manipulation.log", 'a')
    time = datetime.now().strftime('[%d/%b/%Y %H:%M:%S]')
    f.write ("%s - %s \n" % (time, kwargs['msg']) )
    f.close()
