import os
from django.conf import settings
from django.db.models import NOT_PROVIDED
from pyforms_web.controls.control_base import ControlBase
import simplejson

class ControlFileUpload(ControlBase):

	def init_form(self):
		return "new ControlFileUpload('{0}', {1})".format( self._name, simplejson.dumps(self.serialize()) )

	@property
	def filepath(self):
		if self.value:
			return os.path.join( settings.MEDIA_ROOT, self.value[len(settings.MEDIA_URL):] )
		else:
			return None

	def serialize(self):
		data = super(ControlFileUpload, self).serialize()

		if self.value and self.value!=NOT_PROVIDED:
			try:
				file_data = {
					'name': os.path.basename(self.value),
					'size': os.path.getsize(self.filepath),
					'file': self.value,
					 'url': self.value
				}
				data.update({ 'file_data':file_data })
			except OSError:
				pass

		return data