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
        return jarviis_model

    def create_message_model(self):
        reader = self.reader
        jarviis_model = reader.csv('admin/jarviis/data/message')
        jarbody = jarviis_model['body'].str.contains('KB국민체크', case=True, na=False)
        jarviis_model =jarviis_model.loc[jarbody, :]
        jarviis_model.to_csv('admin/jarviis/data/' + 'new_data/message_final06.csv')
        return jarviis_model

    def splite_string(self):
        pass



