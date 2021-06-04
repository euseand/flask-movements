from marshmallow import fields, Schema


class UserSchema(Schema):
    """User schema class made for serializing/deserializing database model"""
    user_id = fields.UUID(data_key='userId', dump_only=True)
    username = fields.String(data_key='username', required=True)
    email = fields.String(data_key='email', required=True)
    password = fields.String(data_key='password', required=True, load_only=True)
    date_joined = fields.Date(data_key='dateJoined', dump_only=True)

    class Meta:
        fields = ('user_id', 'username', 'email', 'password', 'date_joined',)


class UserSingleOutputSchema(Schema):
    """Single User object output class made for enveloping response"""
    user = fields.Nested(UserSchema)

    class Meta:
        fields = ('user',)


class UserListOutputSchema(Schema):
    """List of Money Movement objects class made for enveloping response"""
    users = fields.List(fields.Nested(UserSchema))

    class Meta:
        fields = ('users',)
