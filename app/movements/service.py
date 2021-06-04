from app.movements.model import db, MoneyMovementModel
from app.movements.exceptions import MovementObjectNotFound


class MoneyMovementsService:
    """Manager class for Money Movement objects"""
    @staticmethod
    def get_all():
        """Read all objects from database"""
        movement_list = MoneyMovementModel.query.all()
        return movement_list

    @staticmethod
    def get_by_id(movement_id):
        """Read a single objects from database by id"""
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            return movement
        else:
            raise MovementObjectNotFound

    @staticmethod
    def create(data):
        """Create a new object and save to database"""
        new_movement = MoneyMovementModel(**data)
        db.session.add(new_movement)
        db.session.commit()
        return new_movement

    @staticmethod
    def update(movement_id, data):
        """Update a single object fields and save to database"""
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            movement.update(data)
            db.session.commit()
        else:
            raise MovementObjectNotFound

    @staticmethod
    def delete(movement_id):
        """Delete a single object from database"""
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            db.session.delete(movement)
            db.session.commit()
        else:
            raise MovementObjectNotFound
