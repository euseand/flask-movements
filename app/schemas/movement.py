from marshmallow import fields, Schema


class MoneyMovementInputSchema(Schema):

    movementId = fields.UUID(dump_only=True)
    modifiedDate = fields.Date(dump_only=True)
    amount = fields.String(attribute='amount', required=True)
    originatorPerson = fields.String(required=True)
    receiverPerson = fields.String(required=True)
    note = fields.String(attribute='note')

    class Meta:
        ordered = True
        fields = ('movementId', 'modifiedDate', 'amount', 'originatorPerson', 'receiverPerson', 'note')


class MoneyMovementOutputSchema(Schema):

    movement_id = fields.String(data_key='movementId')
    modified_date = fields.String(data_key='modifiedDate')
    amount = fields.String()
    originator_person = fields.String(data_key='originatorPerson')
    receiver_person = fields.String(data_key='receiverPerson')
    note = fields.String(attribute='note')

    class Meta:
        ordered = True
        fields = ('movement_id', 'modified_date', 'amount', 'originator_person', 'receiver_person', 'note')


class SingleResponseSchema(Schema):

    type = fields.String(required=True)
    data = fields.Nested(MoneyMovementOutputSchema, required=True)

    class Meta:
        ordered = True
        fields = ('type', 'data')


class ListResponseSchema(Schema):

    type = fields.String(required=True)
    data = fields.List(fields.Nested(MoneyMovementOutputSchema), required=True)

    class Meta:
        ordered = True
        fields = ('type', 'data')
