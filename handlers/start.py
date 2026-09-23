from aiogram import Router
from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.types import ChatMemberUpdated

router = Router()


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def bot_joined_chat(event: ChatMemberUpdated):
    await event.bot.send_message(
        chat_id=event.chat.id,
        text=(
            "👋 <b>Hello everyone! I'm a bot moderator.</b>\n"
            "Thank you for adding me to the chat.\n\n"
            "⚠️ <b>Important:</b> Please grant me administrator rights (blocking, limiting members)"
            "so I can work properly and issue mutes/bans/warns"
        ),
        parse_mode="HTML"
    )