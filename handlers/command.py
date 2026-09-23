from aiogram import Router, F
from aiogram import Bot
from filters.filter import Admin, Reply, BotIsAdmin
from datetime import timedelta
from aiogram.types import ChatPermissions
from aiogram.types import Message
from database.db import (
    get_warnings_count, get_warning, 
    get_warnings_for_user, delete_warning)

router = Router()


@router.message(
        F.text.lower().in_({"!pin", "pin"}),
        Reply(), Admin(), BotIsAdmin()
)
async def pin_command(message: Message):
    await message.bot.pin_chat_message(
        chat_id=message.chat.id,
        message_id=message.reply_to_message.message_id,
        disable_notification=False
    )
    await message.reply(f"✅ Message is pinned")


@router.message(
        F.text.lower().in_({"!unpin", "unpin"}),
        Reply(), Admin(), BotIsAdmin()
)
async def unpin_command(message: Message):
    await message.reply_to_message.unpin()
    await message.reply(f"✅ Message is unpinned")
  


@router.message(
        F.text.lower().in_({"!ban", "ban"}), 
        Reply(), Admin(), BotIsAdmin()
        )
async def ban_command(message: Message):
    target_user = message.reply_to_message.from_user
    await message.chat.ban(user_id=target_user.id)
    await message.reply(f"❌ User {target_user.first_name} banned")    


@router.message(
        F.text.lower().in_({"!unban", "unban"}), 
        Reply(), Admin(), BotIsAdmin()
        )
async def unban_command(message: Message):
    target_user = message.reply_to_message.from_user
    await message.chat.unban(user_id=target_user.id, only_if_banned=True)
    await message.reply(f"✅ User {target_user.first_name} unbanned!")



@router.message(
        F.text, F.text.lower().startswith(("!mut", "mut")), 
        Reply(), Admin(), BotIsAdmin()
        )
async def mute_command(message: Message):
    args = message.text.split(maxsplit=1)
    
    if len(args) < 2:
        return await message.reply("Specify the time of the mute!")

    time_str = args[1].strip().lower()
    
    unit = time_str[-1]
    value = time_str[:-1]

    if not value.isdigit():
        return await message.reply("Incorrect time format! Example: `15m`, `2h`, `1d`")

    duration = int(value)
    if duration <= 0:
        return await message.reply("Mute time must be greater than 0")

    if unit == "m":
        delta = timedelta(minutes=duration)
    elif unit == "h":
        delta = timedelta(hours=duration)
    elif unit == "d":
        delta = timedelta(days=duration)

    target_user = message.reply_to_message.from_user
    permissions = ChatPermissions(can_send_messages=False)

    try:
        await message.chat.restrict(
            user_id=target_user.id,
            permissions=permissions,
            until_date=delta
        )
        await message.reply(f"🔇 User {target_user.first_name} has been muted at {time_str}")
    except Exception as e:
        await message.reply(f"Failed to issue mute: {e}")



@router.message(
        F.text.lower().in_({"!unmut", "unmut",}), 
        Reply(), Admin(), BotIsAdmin()
        )
async def unmute_command(message: Message):
    target_user = message.reply_to_message.from_user

    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True
    )
    
    await message.chat.restrict(
        user_id=target_user.id,
        permissions=permissions
    )

    await message.reply(f"🔊 Restrictions have been lifted for user {target_user.first_name}")    


@router.message(
        F.text,
        F.text.lower().startswith(("!warn", "warn")), 
        Reply(), Admin(), BotIsAdmin()
        )
async def warn_command(message: Message):
    args = message.text.split(maxsplit=1)
         
    if len(args) < 2:
        return await message.reply("Write the reason for the warning")

    user_id = message.reply_to_message.from_user.id
    target_user = message.reply_to_message.from_user
    moderator_id = message.from_user.id
    chat_id = message.chat.id
    reason = args[1]

    await get_warning(chat_id, user_id, moderator_id, reason)

    await message.reply(
        f"⚠️ User {target_user.first_name} received a warning\n"
        f"Reason : {reason}\n"
        f"Total warnings: {await get_warnings_count(user_id)}")  


@router.message(
        F.text,
        F.text.lower().startswith(("!all_warns", "all_warns")), 
        Reply(), BotIsAdmin()
        )
async def warn_for_user_command(message: Message, bot: Bot):
    user_id = message.reply_to_message.from_user.id
    target_user = message.reply_to_message.from_user
    chat_id = message.chat.id

    warnings = await get_warnings_for_user(user_id, chat_id)  

    if not warnings:
        await message.reply(
            f"{target_user.full_name} has no warnings."
        )
        return

    text = f"⚠️ Warnings for {target_user.full_name}:\n"
    for warning in warnings:
        admin = await bot.get_chat(warning["moderator_id"])
        first_name = admin.first_name

        text += (
            f"ID: {warning['warning_id']}\n"
            f"Reason: {warning['reason']}\n"
            f"Admin: {first_name}\n"
            f"Date: {warning['created_at']:%d.%m.%Y %H:%M}\n\n"
        )

    await message.reply(text)


@router.message(
        F.text,
        F.text.lower().startswith(("!delete_warn", "delete_warn")), 
        Reply(), Admin(), BotIsAdmin()
        )
async def warn_command(message: Message):
    args = message.text.split(maxsplit=1)
         
    if len(args) < 2:
        return await message.reply("Write the warning ID")

    elif not args[1].isdigit():
        return await message.reply("Write the ID in numerical form")    

    target_user = message.reply_to_message.from_user.first_name
    warning_id = int(args[1])

    is_deleted = await delete_warning(warning_id)

    if not is_deleted:
        return await message.reply(f"There is no warning with this ID: {warning_id}")

    await message.reply(
        f"✅ You have removed the warning {warning_id} "
        f"from the {target_user}"
        )


  