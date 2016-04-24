from logging import StreamHandler

from .signals import book_manipulation
from .models import RequestRecord


class LoggingBooksManipulationsMiddleware(StreamHandler):
    def emit(self, record):
        msg = record.msg
        if (msg.find('book_store_book') != -1 and
                msg.find('INSERT') != -1 or msg.find('UPDATE') != -1 or msg.find('DELETE') != -1):
            book_manipulation.send(sender=self.__class__, msg=msg)


class RequestKeeperMiddleware:
    def process_view(self, request, view, args, kwargs):
        record = RequestRecord(path=request.path)
        record.save()