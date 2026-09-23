from aiogram import Router
from aiogram.filters import ChatMemberUpdatedFilter, PROMOTED_TRANSITION
from aiogram.types import ChatMemberUpdated

router = Router()


@router.chat_member(ChatMemberUpdatedFilter(PROMOTED_TRANSITION))
async def on_promoted(event: ChatMemberUpdated):
    user_name = event.new_chat_member.user.first_name
    await event.answer(f"Congratulations {user_name} on your appointment as administrator!")


@router.chat_member(ChatMemberUpdatedFilter(~PROMOTED_TRANSITION))
async def on_demoted(event: ChatMemberUpdated):
    user_name = event.new_chat_member.user.first_name
    await event.answer(f"{user_name} you've been demoted...")    
    