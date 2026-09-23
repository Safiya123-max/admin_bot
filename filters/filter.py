from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.enums import ChatMemberStatus


class Admin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.chat.type == "private":
            return False

        member = await message.chat.get_member(message.from_user.id)
                
        if member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR):
            return True   
        else:
            await message.reply("You do not have administrator rights")
            return False


class Reply(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not message.reply_to_message:
            await message.reply("Need to reply to message")
            return False 
        
        return True


class BotIsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.chat.type == "private":
            return False

        bot_member = await message.chat.get_member(message.bot.id)
        is_admin = bot_member.status == ChatMemberStatus.ADMINISTRATOR
       
        if not is_admin:
            await message.reply("Give the bot administrator rights to execute this command!")

        return is_admin


class NotPrivat(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.chat.type == "private":
            return False
        
        return True   

