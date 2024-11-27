from config import database
from utils.data_gathering import *

def calculate_user_days(id):
    daylist = get_all_days_from_user(id)
    return daylist

def determine_user_name(id):
    username = get_user_name_by_id(id)
    return {"name":username}

def determine_user_rewards(id):
    rewardlist = get_all_rewards_from_user(id)
    return rewardlist

def update_user_day(id, day_index, new_day_value):
    user_ref = database.db.collection('users').where('identifier', '==', id).get()
    if user_ref:
        doc_ref = user_ref[0].reference
        doc_data = doc_ref.get().to_dict()
        days = doc_data.get("days", [])
        
        if 0 <= day_index < len(days):
            days[day_index] = new_day_value
            doc_ref.update({"days": days})
            return {"message": "Day updated successfully."}
        else:
            return {"error": "Index out of range."}
    else:
        return {"error": "User not found."}


def create_user_service(id,user_name):
    user_ref = database.db.collection('users').where('identifier', '==', id).get()
    if user_ref:
        return {"error": "User already exists."}

    # Create a new user
    user_data = {
        "id": id,
        "name": user_name,
        "days": ["ready_to_open"] * 24
    }
    database.db.collection('users').add(user_data)
    return {"message": "User created successfully."}