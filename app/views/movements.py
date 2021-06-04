from flask import jsonify
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from app.schemas.movements import MoneyMovementSchema, MoneyMovementSingleOutputSchema, MoneyMovementListOutputSchema
from app.services.movements import MoneyMovementsService
from app.exceptions.movements import MovementObjectNotFound


movement_blp = Blueprint('movement', __name__, url_prefix='/movements',
                         description='All operations for a single money movement object')
movements_blp = Blueprint('movements', __name__, url_prefix='/movements',
                          description='All operations for a list of money movement objects')

movement_dao = MoneyMovementsService()

movement_schema = MoneyMovementSchema()
movements_schema = MoneyMovementSchema(many=True)


@movement_blp.route('/<movement_id>')
class Movement(MethodView):
    """Api view class for single Money Movement object operations"""
    @staticmethod
    @movement_blp.response(200, MoneyMovementSingleOutputSchema)
    def get(movement_id):
        """Read a single movement

        Return single money movements object.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)
            movement_json = movement_schema.dump(movement)
            return jsonify({'movement': movement_json}), 200
        except MovementObjectNotFound:
            abort(404, message='Movement not found.')

    @staticmethod
    @movement_blp.arguments(MoneyMovementSchema)
    @movement_blp.response(200, MoneyMovementSingleOutputSchema)
    def put(movement_id, movement_data):
        """Update an existing movement

        Update money movement with sent data.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)
            movement_dao.update(movement_id, movement_data)
            movement_json = movement_schema.dump(movement)
            return jsonify({'movement': movement_json}), 200
        except MovementObjectNotFound:
            abort(404, message='Movement not found.')

    @staticmethod
    @movement_blp.response(200)
    def delete(movement_id):
        """Delete an existing movement

        Delete money movement object.
        """
        try:
            movement = movement_dao.get_by_id(movement_id)            
            movement_dao.delete(movement_id)
            return {'message': 'Movement deleted successfully'}, 200
        except MovementObjectNotFound:
            abort(404, message='Movement not found')


@movements_blp.route('/')
class MovementsList(MethodView):
    """Api view class for a list of Money Movement objects operations"""
    @staticmethod
    @movements_blp.response(200, MoneyMovementListOutputSchema)
    def get():
        """Read all movements

        Return all money movements objects.
        """
        movements = movement_dao.get_all()
        movements_json = movements_schema.dump(movements)
        return jsonify({'movements': movements_json}), 200

    @staticmethod
    @movements_blp.arguments(MoneyMovementSchema)
    @movements_blp.response(201, MoneyMovementSingleOutputSchema)
    def post(movement_data):
        """Create a new movement

        Add a new money movement object.
        """
        movement = movement_dao.create(movement_data)
        movement_json = movement_schema.dump(movement)
        return jsonify({'movement': movement_json}), 201
