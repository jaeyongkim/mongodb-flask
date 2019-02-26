from ..models import db
from ..models.user import User, Test

def get_user():
    print('here')
    t = db.Test()
    print(db.registered_documents)
    t.email = 'test123'
    t.is_test = True
    t.save()

def create_new_member():
    pass
    # user = User()
    # user.email = 'helloworld'
    # user.save()