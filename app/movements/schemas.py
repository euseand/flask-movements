from marshmallow import fields, Schema


class MoneyMovementSchema(Schema):
    """Money Movement schema class made for serializing/deserializing database model"""
    movement_id = fields.UUID(data_key='movementId', dump_only=True)
    modified_date = fields.Date(data_key='modifiedDate', dump_only=True)
    amount = fields.String(data_key='amount', required=True)
    originator_person = fields.String(data_key='originatorPerson', required=True)
    receiver_person = fields.String(data_key='receiverPerson', required=True)
    note = fields.String(data_key='note')

    class Meta:
        fields = ('movement_id', 'modified_date', 'amount', 'originator_person', 'receiver_person', 'note',)


class MoneyMovementInputSchema(MoneyMovementSchema):
    """Money Movement schema class made for filling new object fields"""

    class Meta:
        fields = ('amount', 'originator_person', 'receiver_person', 'note',)


class MoneyMovementSingleOutputSchema(Schema):
    """Single Money Movement object output class made for enveloping response"""
    movement = fields.Nested(MoneyMovementSchema)

    class Meta:
        fields = ('movement',)


class MoneyMovementListOutputSchema(Schema):
    """List of Money Movement objects class made for enveloping response"""
    movements = fields.List(fields.Nested(MoneyMovementSchema))

    class Meta:
        fields = ('movements',)
