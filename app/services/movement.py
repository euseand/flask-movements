from app import db
from app.models.movement import MoneyMovementModel


class MoneyMovementService:

    @staticmethod
    def get_all():
        movement_list = MoneyMovementModel.query.all()
        if movement_list:
            return movement_list
        else:
            raise Exception

    @staticmethod
    def get_by_id(movement_id):
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            return movement
        else:
            raise Exception

    @staticmethod
    def create(data):
        new_movement = MoneyMovementModel(**data)
        db.session.add(new_movement)
        db.session.commit()
        return new_movement

    @staticmethod
    def update(movement_id, data):
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            movement.update(data)
            db.session.commit()
            return movement
        else:
            raise Exception

    @staticmethod
    def delete(movement_id):
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            db.session.delete(movement)
            db.session.commit()
