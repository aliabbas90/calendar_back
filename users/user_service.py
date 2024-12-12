from config import database
from utils.data_gathering import *
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def calculate_user_days(id):
    daylist = get_all_days_from_user(id)
    return daylist

def determine_user_name(id):
    username = get_user_name_by_id(id)
    return {"name":username}

def determine_user_rewards(id):
    reward,reward_day = get_all_rewards_from_user(id)
    return reward,reward_day

def update_user_day(id, day_index, new_day_value):
    user_ref = database.db.collection('users').where('id', '==', id).get()
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


def create_user_service(id,user_name,reward,reward_day):
    user_ref = database.db.collection('users').where('id', '==', id).get()
    if user_ref:
        return {"error": "User already exists."}

    # Create a new user
    user_data = {
        "id": id,
        "name": user_name,
        "days": ["ready_to_open"] * 24,
        "reward" : reward,
        "reward_day" : reward_day
    }
    database.db.collection('users').add(user_data)
    return {"message": "User created successfully."}

def validate_recaptcha(token):
    print("Début de la validation reCAPTCHA...")
    api_key = os.getenv("CAPTCHA_API_KEY")
    site_key = os.getenv("CAPTCHA_SITE_KEY")
    url = f"https://recaptchaenterprise.googleapis.com/v1/projects/tipii-calendar-659cf/assessments?key={api_key}"

    request_body = {
        "event": {
            "token": token,
            "expectedAction": "LOGIN",
            "siteKey": site_key,
        }
    }

    try:
        print(f"Envoi de la requête POST à l'URL : {url}")
        response = requests.post(url, json=request_body)
        print(f"Statut HTTP de la réponse : {response.status_code}")
        result = response.json()
        print("Réponse reCAPTCHA :", result)

        valid = result.get("tokenProperties", {}).get("valid", False)
        score = result.get("riskAnalysis", {}).get("score", 0)

        print(f"Validité : {valid}, Score : {score}")
        return valid, score
    except Exception as e:
        print(f"Erreur lors de la validation reCAPTCHA : {e}")
        return False, 0


