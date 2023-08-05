from . import rule
from .field import Field, FloatField, DateField


class DataObject(Field):
    def __init__(self):
        """
        Actual data is the "date" and "number" Fields
        """
        super().__init__()
        self.name = "data"
        self.value = []
        self.date = DateField("date")
        self.number = FloatField("value")
        self.rules = [
            rule.len_eq(2),
        ]
        self.fields = [self.date, self.number]

    def set(self, value):
        self.value = value
        self.run_rules()
        if self.errors:
            return
        self.set_field(self.date, self.value[0])
        self.set_field(self.number, self.value[1])
        return self.errors
