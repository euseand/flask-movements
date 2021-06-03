from app import db
from app.models.movement import MoneyMovementModel
from app.exceptions.movement import MovementObjectNotFound


class MoneyMovementService:

    @staticmethod
    def get_all():
        movement_list = MoneyMovementModel.query.all()
        return movement_list

    @staticmethod
    def get_by_id(movement_id):
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            return movement
        else:
            raise MovementObjectNotFound

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
        else:
            raise MovementObjectNotFound

    @staticmethod
    def delete(movement_id):
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            db.session.delete(movement)
            db.session.commit()
        else:
            raise MovementObjectNotFound
