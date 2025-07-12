from RAJAmusic67.core.bot import SHUKLA
from RAJAmusic67.core.dir import dirr
from RAJAmusic67.core.git import git
from RAJAmusic67.core.userbot import Userbot
from RAJAmusic67.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SHUKLA()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
