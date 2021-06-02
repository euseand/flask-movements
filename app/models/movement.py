import datetime

from app import db


class MoneyMovementModel(db.Model):

    __tablename__ = 'money_movement'

    movement_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modified_date = db.Column(db.Date, default=datetime.datetime.today)
    amount = db.Column(db.String(50))
    originator_person = db.Column(db.String(100))
    receiver_person = db.Column(db.String(100))
    note = db.Column(db.String(100), nullable=True)

    def repr(self):
        return f'Money movement #{self.movement_id} from {self.originator_person} to {self.receiver_person} ' \
               f'with amount of {self.amount} made on {self.modified_date}'

