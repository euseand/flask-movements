from marshmallow import fields, Schema


class MoneyMovementSchema(Schema):

    movementId = fields.Integer(attribute='movement_id', dump_only=True)
    modifiedDate = fields.Date(attribute='modified_date', dump_only=True)
    amount = fields.String(attribute='amount')
    originatorPerson = fields.String(attribute='originator_person')
    receiverPerson = fields.String(attribute='receiver_person')
    note = fields.String(attribute='note')

    class Meta:
        fields = ('movementId', 'modifiedDate', 'amount', 'originatorPerson', 'receiverPerson', 'note')
