import motor.motor_asyncio
import time
from info import DATABASE_NAME, DATABASE_URL, IMDB_TEMPLATE, WELCOME_TEXT, AUTH_CHANNEL, LINK_MODE, TUTORIAL, SHORTLINK_URL, SHORTLINK_API, SHORTLINK, FILE_CAPTION, IMDB, WELCOME, SPELL_CHECK, PROTECT_CONTENT, AUTO_FILTER, AUTO_DELETE

class Database:
    default_setgs = {
        'auto_filter': AUTO_FILTER,
        'file_secure': PROTECT_CONTENT,
        'imdb': IMDB,
        'spell_check': SPELL_CHECK,
        'auto_delete': AUTO_DELETE,
        'welcome': WELCOME,
        'welcome_text': WELCOME_TEXT,
        'template': IMDB_TEMPLATE,
        'caption': FILE_CAPTION,
        'url': SHORTLINK_URL,
        'api': SHORTLINK_API,
        'shortlink': SHORTLINK,
        'tutorial': TUTORIAL,
        'links': LINK_MODE,
        'fsub': AUTH_CHANNEL
    }

    default_verify = {
        'is_verified': False,
        'verified_time': 0,
        'verify_token': "",
        'link': ""
    }
    
    def __init__(self):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
        self.db = self._client[DATABASE_NAME]
        self.col = self.db.Users
        self.grp = self.db.Groups


    def new_user(self, id, name, premium=False, premium_plan=None, premium_expiry=None):
        return dict(
            id=id,
            name=name,
            ban_status=dict(
                is_banned=False,
                ban_reason="",
            ),
            verify_status=dict(
                is_verified=not premium,
                verified_time="" if premium else time.time(),
                verify_token="",
                link=""
            ),
            premium=premium,
            premium_plan=premium_plan,
            premium_expiry=premium_expiry
        )

    def new_group(self, id, title, premium=False):
        return dict(
            id=id,
            title=title,
            chat_status=dict(
                is_disabled=False,
                reason="",
            ),
            settings=self.default_setgs,
            premium=premium
        )
    
    async def add_user(self, id, name, premium=False, premium_plan=None, premium_expiry=None):
        user = self.new_user(id, name, premium, premium_plan, premium_expiry)
        await self.col.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return bool(user)
    
    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count
    
    async def remove_ban(self, id):
        ban_status = dict(
            is_banned=False,
            ban_reason=''
        )
        await self.col.update_one({'id': id}, {'$set': {'ban_status': ban_status}})
    
    async def ban_user(self, user_id, ban_reason="No Reason"):
        ban_status = dict(
            is_banned=True,
            ban_reason=ban_reason
        )
        await self.col.update_one({'id': user_id}, {'$set': {'ban_status': ban_status}})

    async def get_ban_status(self, id):
        default = dict(
            is_banned=False,
            ban_reason=''
        )
        user = await self.col.find_one({'id': int(id)})
        if not user:
            return default
        return user.get('ban_status', default)

    async def get_all_users(self):
        return self.col.find({})
    
    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def delete_chat(self, grp_id):
        await self.grp.delete_many({'id': int(grp_id)})

    async def get_banned(self):
        users = self.col.find({'ban_status.is_banned': True})
        chats = self.grp.find({'chat_status.is_disabled': True})
        b_chats = [chat['id'] async for chat in chats]
        b_users = [user['id'] async for user in users]
        return b_users, b_chats

    async def add_chat(self, chat, title, premium=False):
        chat = self.new_group(chat, title, premium)
        await self.grp.insert_one(chat)

    async def get_chat(self, chat):
        chat = await self.grp.find_one({'id': int(chat)})
        return False if not chat else chat.get('chat_status')

    async def re_enable_chat(self, id):
        chat_status = dict(
            is_disabled=False,
            reason="",
        )
        await self.grp.update_one({'id': int(id)}, {'$set': {'chat_status': chat_status}})
        
    async def update_settings(self, id, settings):
        await self.grp.update_one({'id': int(id)}, {'$set': {'settings': settings}})
        
    async def get_settings(self, id):
        chat = await self.grp.find_one({'id': int(id)})
        if chat:
            return chat.get('settings', self.default_setgs)
        return self.default_setgs

    async def disable_chat(self, chat, reason="No Reason"):
        chat_status = dict(
            is_disabled=True,
            reason=reason,
        )
        await self.grp.update_one({'id': int(chat)}, {'$set': {'chat_status': chat_status}})

    async def get_verify_status(self, user_id, chat_id=None):
        user = await self.col.find_one({'id': int(user_id)})
        if user:
            if chat_id and user.get('premium', False):
                return self.default_verify
            return user.get('verify_status', self.default_verify)
        return self.default_verify

    async def update_verify_status(self, user_id, verify):
        await self.col.update_one({'id': int(user_id)}, {'$set': {'verify_status': verify}})

    async def total_chat_count(self):
        count = await self.grp.count_documents({})
        return count

    async def get_all_chats(self):
        return self.grp.find({})

    async def get_db_size(self):
        return (await self.db.command("dbstats"))['dataSize']
    
    async def update_premium_plan(self, user_id, premium_plan, premium_expiry):
        await self.col.update_one({'id': int(user_id)}, {'$set': {'premium_plan': premium_plan, 'premium_expiry': premium_expiry}})

    async def get_premium_plan(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        if user:
            return user.get('premium_plan'), user.get('premium_expiry')
        return None, None

    async def check_premium_expiry(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        if user and user.get('premium', False):
            current_time = time.time()
            expiry_time = user.get('premium_expiry', 0)
            if expiry_time > current_time:
                return True
            else:
                await self.col.update_one({'id': int(user_id)}, {'$set': {'premium': False, 'verify_status.is_verified': False}})
        return False

    async def buy_premium(self, user_id, premium_plan):
        current_time = time.time()
        if premium_plan == '7days':
            expiry_time = current_time + (7 * 24 * 60 * 60)  # 7 days
            cost = 12
        elif premium_plan == '30days':
            expiry_time = current_time + (30 * 24 * 60 * 60)  # 30 days
            cost = 30
        elif premium_plan == '120days':
            expiry_time = current_time + (120 * 24 * 60 * 60)  # 120 days
            cost = 60
        elif premium_plan == '365days':
            expiry_time = current_time + (365 * 24 * 60 * 60)  # 365 days
            cost = 120
        else:
            return None

        existing_plan, existing_expiry = await self.get_premium_plan(user_id)
        if existing_plan == premium_plan and existing_expiry > current_time:
            expiry_time += existing_expiry - current_time

        await self.update_premium_plan(user_id, premium_plan, expiry_time)
        return cost

db = Database()
