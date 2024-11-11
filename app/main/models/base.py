from sqlalchemy import Column,DateTime,event
from datetime import datetime
from sqlalchemy import event

from sqlalchemy.ext.declarative import declared_attr

class TimestampMixin:
    @declared_attr
    def date_added(cls):
        return Column(DateTime, default=datetime.now())

    @declared_attr
    def date_modified(cls):
        return Column(DateTime, onupdate=datetime.now())


@event.listens_for(TimestampMixin, 'before_insert', propagate=True)
def update_created_modified_on_create_listener(mapper, connection, target):
    target.date_added = datetime.now()
    target.date_modified = datetime.now()

@event.listens_for(TimestampMixin, 'before_update', propagate=True)
def update_modified_on_update_listener(mapper, connection, target):
    target.date_modified = datetime.now()


