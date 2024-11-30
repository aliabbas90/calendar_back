from flask import jsonify
from .user_service import (
    calculate_user_days,
    determine_user_name,
    determine_user_rewards,
    update_user_day,
    create_user_service
)

def get_user_days(id):
    days = calculate_user_days(id)
    return jsonify(days)

def get_user_name_from_id(id):
    name = determine_user_name(id)
    return jsonify(name)

def get_user_rewards(id):
    reward,reward_day = determine_user_rewards(id)
    return jsonify({"reward":reward,"reward_day_":reward_day})

def modify_user_day(id, day_index, new_day_value):
    result = update_user_day(id, day_index, new_day_value)
    return jsonify(result)

def create_new_user(id,user_name,reward,reward_day):
    result = create_user_service(id,user_name,reward,reward_day)
    return jsonify(result)
