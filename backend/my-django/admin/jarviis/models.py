from django.db import models

# Create your models here.
from admin.common.models import ValueObject, Reader, Printer


class Jarviis(object):
    vo = ValueObject()
    reader = Reader()
    printer = Printer()

    def create_jarviis_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/jarviis/data/'
        vo.fname = 'jangmessage'
        jarviis_file_name = reader.new_file(vo)
        jarviis_model = reader.csv(jarviis_file_name, 0, ['count','body','readable_date'])
        printer.dframe(jarviis_model)
        jarviis_model.to_csv(self.vo.context + 'new_data/message_final2.csv')
        return jarviis_model

    def create_message_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/jarviis/data/new_data/'
        vo.fname = 'message_final'
        jarviis_file_name = reader.new_file(vo)
        jarviis_model = reader.csv(jarviis_file_name, 0, ('count','body','readable_date'))
        jarviis_model[["body"].str.startswith("KB")].head()
        jarviis_model.to_csv(self.vo.context + 'new_data/message_final03.csv')
        return jarviis_model

    def pratice(self):
        pass