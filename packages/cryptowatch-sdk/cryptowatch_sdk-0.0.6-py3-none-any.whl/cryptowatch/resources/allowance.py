from marshmallow import Schema, fields, post_load


class AllowanceSchema(Schema):
    cost = fields.Integer()
    remaining = fields.Integer()
    remainingPaid = fields.Integer()
    upgrade = fields.Str()

    @post_load
    def make_allowance(self, data, **kwargs):
        return AllowanceResource(**data)


class AllowanceResource:
    def __init__(self, cost, remaining, remainingPaid, upgrade):
        self.cost = cost
        self.remaining = remaining
        self.remaining_paid = remainingPaid
        self.upgrade = upgrade

    def __repr__(self):
        return "<Allowance({self.remaining})>".format(self=self)
