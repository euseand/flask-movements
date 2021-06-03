from pprint import pprint

from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app.schemas.movement import MoneyMovementSchema, SingleOutputSchema, ListOutputSchema
from app.services.movement import MoneyMovementService
from app.exceptions import MovementObjectNotFound


movement_blp = Blueprint('movement', __name__, url_prefix='/movement',
                description='Single money movement operations')
movements_blp = Blueprint('movements', __name__, url_prefix='/movement',
                description='List of money movements operations')
movement_dao = MoneyMovementService()
movement_schema = MoneyMovementSchema()
movements_schema = MoneyMovementSchema(many=True)


@movements_blp.route('/')
class MovementList(MethodView):

    @staticmethod
    @movements_blp.response(200, ListOutputSchema)
    def get():
        """Get movements

        Return all money movements objects.
        """
        movements = movement_dao.get_all()
        movements_json = movements_schema.dump(movements)
        return jsonify({'movements': movements_json})

    @staticmethod
    @movements_blp.arguments(MoneyMovementSchema)
    @movements_blp.response(201, SingleOutputSchema)
    def post(movement_data):
        """Post movement

        Add a new money movement object.
        """
        movement = movement_dao.create(movement_data)
        movement_json = movement_schema.dump(movement)
        return jsonify({'movement': movement_json})


@movement_blp.route('/<movement_id>')
class Movement(MethodView):

    @staticmethod
    @movement_blp.response(200, SingleOutputSchema)
    def get(movement_id):
        """Get movement

        Return single money movements object.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)
            movement_json = movement_schema.dump(movement)
            return jsonify({'movement': movement_json})
        except MovementObjectNotFound:
            abort(404, message='Movement not found.')

    @staticmethod
    @movement_blp.arguments(MoneyMovementSchema)
    @movement_blp.response(200, SingleOutputSchema)
    def put(movement_id, movement_data):
        """Put movement

        Update money movement with sent data.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)
            movement_dao.update(movement_id, movement_data)
            movement_json = movement_schema.dump(movement)
            return jsonify({'movement': movement_json})
        except MovementObjectNotFound:
            abort(404, message='Movement not found.')

    @staticmethod
    @movement_blp.response(200)
    def delete(movement_id):
        """Delete movement

        Delete money movement object.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)            
            movement_dao.delete(movement_id)
            return {'message': 'Movement deleted successfully'}, 200
        except MovementObjectNotFound:
            abort(404, message='Movement not found')
