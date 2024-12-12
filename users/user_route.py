from flask import Blueprint,request,jsonify
from .user_controller import (
    get_user_days,
    get_user_name_from_id,
    get_user_rewards,
    modify_user_day,
    create_new_user
)

users_bp = Blueprint('users', __name__)



@users_bp.route('/users/days', methods=['GET'])
def days_of_user():
    user = request.args.get('id')
    return get_user_days(user)

@users_bp.route('/users/id-to-name', methods=['GET'])
def name_of_user():
    id = request.args.get('id')
    captcha_token = request.args.get('captchaToken')
    print("dans user_route:",captcha_token)
    if not captcha_token:
        return jsonify({"error": "Token reCAPTCHA manquant"}), 400

    return get_user_name_from_id(id, captcha_token)


@users_bp.route('/users/rewards', methods=['GET'])
def rewards_of_user():
    user = request.args.get('id')
    return get_user_rewards(user)

@users_bp.route('/users/update-day', methods=['PUT'])
def update_day_of_user():
    data = request.get_json()
    user_id = data.get('id')
    day_index = data.get('day_index')
    new_day_value = data.get('new_day_value')
    return modify_user_day(user_id, day_index, new_day_value)


@users_bp.route('/users/create', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('id')
    user_name = data.get('name')
    reward = data.get('reward')
    reward_day = data.get('reward_day')
    print(user_name)
    return create_new_user(user_id,user_name,reward,reward_day)

