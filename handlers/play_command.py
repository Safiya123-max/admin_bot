from aiogram import Router, F
from aiogram.types import Message
from filters.filter import Reply, BotIsAdmin

router = Router()


@router.message(
        F.text.lower().in_({"!hit", "hit"}), 
        Reply(), BotIsAdmin()
        )
async def hit_command(message: Message):
    target_user = message.reply_to_message.from_user
    user = message.from_user

    user_mention = f'<a href="tg://user?id={user.id}">{user.full_name}</a>'
    target_user_mention = f'<a href="tg://user?id={target_user.id}">{target_user.full_name}</a>'
    
    await message.reply(
        f"👊 | {user_mention} hit {target_user_mention}",
        parse_mode="HTML")  


@router.message(
        F.text.lower().in_({"!kiss", "kiss"}), 
        Reply(), BotIsAdmin()
        )
async def kiss_command(message: Message):
    target_user = message.reply_to_message.from_user
    user = message.from_user

    user_mention = f'<a href="tg://user?id={user.id}">{user.full_name}</a>'
    target_user_mention = f'<a href="tg://user?id={target_user.id}">{target_user.full_name}</a>'
    
    await message.reply(
        f"💋 | {user_mention} kissed {target_user_mention}",
        parse_mode="HTML")   


@router.message(
        F.text.lower().in_({"!hugg", "hugg"}), 
        Reply(), BotIsAdmin()
        )
async def hugg_command(message: Message):
    target_user = message.reply_to_message.from_user
    user = message.from_user

    user_mention = f'<a href="tg://user?id={user.id}">{user.full_name}</a>'
    target_user_mention = f'<a href="tg://user?id={target_user.id}">{target_user.full_name}</a>'
    
    await message.reply(
        f"🫂 | {user_mention} hugged {target_user_mention}",
        parse_mode="HTML")
