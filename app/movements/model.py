import uuid
import datetime

from sqlalchemy.dialects.postgresql import UUID

from app.common import db


class MoneyMovementModel(db.Model):
    """Money Movement model class made for storing objects in database"""
    __tablename__ = 'movements'

    movement_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    modified_date = db.Column(db.Date, default=datetime.datetime.today)
    amount = db.Column(db.String(length=50))
    originator_person = db.Column(db.String(length=100))
    receiver_person = db.Column(db.String(length=100))
    note = db.Column(db.String(length=100), nullable=True)

    def __repr__(self):
        return f'Money movement #{self.movement_id} from {self.originator_person} to {self.receiver_person} ' \
               f'with amount of {self.amount} made on {self.modified_date}'

