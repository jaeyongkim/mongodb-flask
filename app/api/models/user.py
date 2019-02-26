from datetime import datetime
from . import db, Document


@db.register
class User(Document):
    __collection__ = 'user'
    structure = {
        'email': str,
        'name': str,
        'created': datetime
    }
    required_fields = ['email']
    default_values = {'created': datetime.utcnow}
    use_dot_notation = True

@db.register
class Test(User):
    structure = {
        'is_test': bool
    }