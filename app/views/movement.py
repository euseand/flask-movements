from pprint import pprint

from flask import jsonify
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from app.schemas.movement import MoneyMovementInputSchema, MoneyMovementOutputSchema, SingleResponseSchema, ListResponseSchema
from app.services.movement import MoneyMovementService
from app.exceptions.movement import MovementObjectNotFound


blp = Blueprint('movement', __name__, url_prefix='/movement', description='Money movements operations')
movement_dao = MoneyMovementService()


@blp.route('/')
class MovementList(MethodView):

    @staticmethod
    @blp.response(200, ListResponseSchema())
    def get():
        """Get movements

        Return all money movements objects.
        """
        movements = movement_dao.get_all()
        result = MoneyMovementOutputSchema(many=True).dump(movements, many=True)
        pprint(result)
        return {'type': 'success', 'data': result}

    @staticmethod
    @blp.arguments(MoneyMovementInputSchema)
    @blp.response(201, SingleResponseSchema)
    def post(movement_data):
        """Post movement

        Add a new money movement object.
        """
        movement = movement_dao.create(movement_data)
        result = MoneyMovementOutputSchema().dump(movement)
        return {'type': 'success', 'data': result}


@blp.route('/<movement_id>')
class Movement(MethodView):

    @staticmethod
    @blp.response(200, SingleResponseSchema)
    def get(movement_id):
        """Get movement

        Return single money movements object.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)
        except MovementObjectNotFound:
            abort(404, message='Movement not found.')
        result = MoneyMovementOutputSchema().dump(movement)
        return {'type': 'success', 'data': result}

    @staticmethod
    @blp.arguments(MoneyMovementInputSchema)
    @blp.response(200, SingleResponseSchema)
    def put(movement_id, movement_data):
        """Put movement

        Update money movement with sent data.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)
        except MovementObjectNotFound:
            abort(404, message='Movement not found.')
        movement_dao.update(movement_id, movement_data)
        result = MoneyMovementOutputSchema().dump(movement)
        return {'type': 'success', 'data': result}

    @staticmethod
    @blp.response(200)
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
