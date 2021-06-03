from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app.schemas.movement import MoneyMovementSchema
from app.services.movement import MoneyMovementService
from app.exceptions import MovementObjectNotFound


movement_blp = Blueprint('movement', 'Money movement operations')
movement_dao = MoneyMovementService()


@movement_blp.route('/movement/')
class MovementList(MethodView):

    @staticmethod
    @movement_blp.response(200, MoneyMovementSchema(many=True))
    def get():
        """Get movements

        Return all money movements objects.
        """
        movements = movement_dao.get_all()
        return movements

    @staticmethod
    @movement_blp.arguments(MoneyMovementSchema)
    @movement_blp.response(201, MoneyMovementSchema)
    def post(movement_data):
        """Post movement

        Add a new money movement object.
        """
        movement = movement_dao.create(movement_data)
        return movement


@movement_blp.route('/movement/<movement_id>')
class Movement(MethodView):

    @staticmethod
    @movement_blp.response(200, MoneyMovementSchema)
    def get(movement_id):
        """Get movement

        Return single money movements object.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)
        except MovementObjectNotFound:
            abort(404, message='Movement not found.')
        return movement

    @staticmethod
    @movement_blp.arguments(MoneyMovementSchema)
    @movement_blp.response(200, MoneyMovementSchema)
    def put(movement_id, movement_data):
        """Put movement

        Update money movement with sent data.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)
        except MovementObjectNotFound:
            abort(404, message='Movement not found.')
        movement_dao.update(movement_id, movement_data)
        return movement

    @staticmethod
    @movement_blp.response(204)
    def delete(movement_id):
        """Delete movement

        Delete money movement object.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)
        except MovementObjectNotFound:
            abort(404, message='Movement not found')
        movement_dao.delete(movement_id)
        return {'message': 'Movement deleted successfully'}, 200
