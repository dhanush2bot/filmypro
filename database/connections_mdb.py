import pymongo
from info import DATABASE_URL, DATABASE_NAME
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

myclient = pymongo.MongoClient(DATABASE_URL)
mydb = myclient[DATABASE_NAME]
mycol = mydb['Connections']   

async def add_connection(group_id, user_id, premium=False):
    user = mycol.find_one({'id': user_id})
    if user:
        if group_id not in user["ids"]:
            mycol.update_one({'id': user_id}, {"$push": {"ids": group_id}})
    else:
        mycol.insert_one({'id': user_id, 'ids': [group_id], 'premium': premium})

async def all_connections(user_id):
    user = mycol.find_one({'id': user_id})
    if user:
        return user["ids"]
    else:
        return []

async def delete_connections(group_id):
    mycol.update_many({"ids": group_id}, {"$pull": {"ids": group_id}})

async def set_premium_status(user_id, premium=True):
    user = mycol.find_one({'id': user_id})
    if user:
        mycol.update_one({'id': user_id}, {"$set": {"premium": premium}})
    else:
        logger.error(f"User {user_id} not found in the database.")

async def get_premium_status(user_id):
    user = mycol.find_one({'id': user_id})
    return user.get("premium", False) if user else False
