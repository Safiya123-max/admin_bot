from aiogram import Router
from aiogram.filters import ChatMemberUpdatedFilter, LEAVE_TRANSITION, JOIN_TRANSITION
from aiogram.types import ChatMemberUpdated

router = Router()

@router.chat_member(ChatMemberUpdatedFilter(LEAVE_TRANSITION))
async def on_user_leave(event: ChatMemberUpdated): 
    await event.answer(f"😔 Good bye, {event.new_chat_member.user.first_name}...")


@router.chat_member(ChatMemberUpdatedFilter(JOIN_TRANSITION))
async def on_user_add(event: ChatMemberUpdated):
    await event.answer(f"👋 Hello, {event.new_chat_member.user.first_name}!")    
