from pyforms_web.controls.control_base import ControlBase
import simplejson

class ControlText(ControlBase):

    def __init__(self, *args, **kwargs):
        """
        :param function on_enter_event: Event called when the Enter key is pressed.
        """
        super().__init__(*args, **kwargs)
        self.on_enter_event = kwargs.get('on_enter_event', self.on_enter_event)


    def init_form(self):
        return """new ControlText('{0}', {1})""".format(
            self._name, 
            simplejson.dumps(self.serialize()) 
        )

    def on_enter_event(self):
        """
        Event called when the Enter key is pressed
        """
        pass

    def serialize(self):
        res = super(ControlText, self).serialize()
        if self.value is None: 
            res.update({'value':''})
        else:
            res.update({'value':str(self.value)})
        return res

    def deserialize(self, properties):
        super(ControlText, self).deserialize(properties)
        val = properties.get('value',None)
        if val=='': self._value = None