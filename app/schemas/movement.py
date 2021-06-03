from marshmallow import fields, Schema


class MoneyMovementSchema(Schema):

    movementId = fields.UUID(attribute='movement_id', dump_only=True)
    modifiedDate = fields.Date(attribute='modified_date', dump_only=True)
    amount = fields.String(attribute='amount', required=True)
    originatorPerson = fields.String(attribute='originator_person', required=True)
    receiverPerson = fields.String(attribute='receiver_person', required=True)
    note = fields.String(attribute='note')

    class Meta:
        ordered = True
        fields = ('movementId', 'modifiedDate', 'amount', 'originatorPerson', 'receiverPerson', 'note')
