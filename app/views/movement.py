import datetime

from flask import request
from flask_restx import fields, Namespace, Resource

# from app.models.movement import MoneyMovementRequestModel
from app.schemas.movement import MoneyMovementSchema
from app.services.movement import MoneyMovementService

movement_ns = Namespace('movement', 'Money movement operations')
movement_dao = MoneyMovementService()
movement_schema = MoneyMovementSchema()
movement_list_schema = MoneyMovementSchema(many=True)
movement_swagger_schema = movement_ns.model('Movement', {
    'movementId': fields.Integer(
        attribute='movement_id', readonly=True, description='Money movement unique identifier'),
    'modifiedDate': fields.String(
        attribute='modified_date', readonly=True, description='Money movement modified date in format YYYY-MM-DD'),
    'amount': fields.String(
        attribute='amount', required=True, description='Money movement amount with currency'),
    'originatorPerson': fields.String(
        attribute='originator_person', required=True, description='Money movement originator person'),
    'receiverPerson': fields.String(
        attribute='2receiver_person', required=True, description='Money movement receiver person'),
    'note': fields.String(
        attribute='note', required=False, description='Money movement additional note'),
})


@movement_ns.route('/<int:movement_id>')


@movement_ns.response(404, 'Money movement not found')
@movement_ns.param('movement_id', 'Money movement identifier')


class Movement(Resource):

    @staticmethod
    @movement_ns.doc('get_movement', model=movement_swagger_schema)
    # @movement_ns.marshal_with(movement_swagger_schema, envelope='movement')
    def get(movement_id):
        movement = movement_dao.get_by_id(movement_id)
        # return movement
        return {'movement': movement_schema.dump(movement)}

    @staticmethod
    @movement_ns.doc('delete_movement')
    def delete(movement_id):
        movement = movement_dao.get_by_id(movement_id)
        if movement:
            movement_dao.delete(movement_id)
            return {'message': 'Movement deleted successfully'}, 200

    @staticmethod
    @movement_ns.doc('put_movement')
    # @movement_ns.expect(movement_description)
    # @movement_ns.marshal_with(movement_description)
    def put(movement_id):
        movement = movement_dao.get_by_id(movement_id)
        data = request.get_json()
        movement_data = movement_schema.load(data)
        if movement:
            movement = movement_dao.update(movement_id, movement_data)
            return {'movement': movement_schema.dump(movement)}, 200


@movement_ns.route('/')
class MovementList(Resource):

    @staticmethod
    @movement_ns.doc('list_movements')
    # @movement_ns.expect(movement_description)
    def get():
        movements = movement_dao.get_all()
        return {'movements': movement_list_schema.dump(movements)}, 200

    @staticmethod
    @movement_ns.doc('post_movement', model=movement_swagger_schema, envelope='movement')
    @movement_ns.expect(movement_swagger_schema)
    # @movement_ns.marshal_with(movement_schema, envelope='movement')
    def post():
        data = request.get_json()
        movement_data = movement_schema.load(data)
        movement = movement_dao.create(movement_data)
        #return movement
        return {'movement': movement_schema.dump(movement)}, 201
