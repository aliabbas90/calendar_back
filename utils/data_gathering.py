from config import database

db = database.db


def get_all_days_from_user(id):
    users_ref = db.collection('users').where('id', '==', id)
    docs = users_ref.stream()
    pydocs = [doc.to_dict() for doc in docs]
    return pydocs[0]["days"]


def get_user_name_by_id(id):
    users_ref = db.collection('users').where('id', '==', id)
    docs = users_ref.stream()
    pydocs = [doc.to_dict() for doc in docs]
    return pydocs[0]["name"]


def get_all_rewards_from_user(id):

    users_ref = db.collection('users').where('id', '==', id)
    docs = users_ref.stream()
    pydocs = [doc.to_dict() for doc in docs]
    return pydocs[0]["reward"],pydocs[0]["reward_day"]
