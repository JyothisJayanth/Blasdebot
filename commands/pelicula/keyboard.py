from functools import lru_cache

from telegram import InlineKeyboardMarkup, InlineKeyboardButton as Button

from commands.pelicula.constants import IMDB, YOUTUBE, TORRENT, SINOPSIS


@lru_cache(1)
def pelis_keyboard(include_desc=False):
    buttons = [
        [
            Button('🎟️ IMDB', callback_data=IMDB),
            Button('🎬️ Trailer', callback_data=YOUTUBE),
        ],
        [
            Button('🍿 Download', callback_data=TORRENT),
        ],
    ]
    if include_desc:
        sinospsis_row = [Button('📖️ Plot', callback_data=SINOPSIS)]
        buttons.insert(0, sinospsis_row)

    return InlineKeyboardMarkup(buttons)
