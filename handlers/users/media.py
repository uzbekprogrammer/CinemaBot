from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from data.config import ADMINS
from states import MediaId
from loader import dp, bot


@dp.message_handler(Command('post'), user_id=ADMINS)
async def posting(message: types.Message):
    await MediaId.video.set()
    await message.reply("Mediani yuborishingiz mumkin")



@dp.message_handler(content_types=types.ContentType.PHOTO, state=MediaId.video, user_id=ADMINS)
async def get_file_id_p(message: types.Message, state: FSMContext):
    video_id = message.photo[-1].file_id
    await message.reply(video_id)
    await state.update_data(
        {"video": video_id}
    )
    await message.answer(f"{video_id}")
    await message.answer('Tartib raqamini kiriting:')
    await MediaId.order.set()


@dp.message_handler(content_types=types.ContentType.VIDEO, state=MediaId.video, user_id=ADMINS)
async def get_file_id_v(message: types.Message, state: FSMContext):
    video_id = message.video.file_id
    await message.reply(video_id)
    await state.update_data(
        {'video': video_id}
    )
    await message.answer("Tartib raqamini kiriting:")
    await MediaId.order.set()


@dp.message_handler(state=MediaId.order, user_id=ADMINS)
async def get_file_order(message: types.Message, state: FSMContext):
    order = message.text
    await state.update_data(
        {'order': order}
    )

    data = await state.get_data()
    mediaId = data.get('video')
    order = data.get('order')

    await message.answer_video(mediaId, caption=f"{order} raqamli video tayyor")


@dp.message_handler(Command("kitob"), user_id=ADMINS)
async def send_book(message: types.Message):
    photo_id = "BAACAgIAAxkBAAMZZh4S1ZmkXdPizkTA-6v5nUyTQ24AAn48AAJqUWFLNWd9r1V8qwI0BA"

    await message.answer_video(
        photo_id, caption="Dasturlash asoslari kitobi. \n Narxi: 50000 so'm"
    )

