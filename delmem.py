from telethon import TelegramClient 
import os 
bit_tokken= "5232848304:AAFyoNZigpThyz-FVMs9f2_NQulsuu9cmtQ" 
api_id=17299114

api_hash="653741f09cbd2a8839c21cdf5fe46217" 
kanal = "@kulgu_vaqti_uz"
Bot = TelegramClient('MemeberRomover',api_id,api_hash).start(bot_token=bit_tokken) 
Target = kanal
RemoveCount = input('6500') 
async def Main() : 
    MeID = await Bot.get_me().id 
    i = 0 
    while i < int(RemoveCount) : 
        for User in await Bot.iter_participants(entity=Target) : 
            if i >= int(RemoveCount) : 
                break 
            try : 
                if int(MeID) != int(User.id) : 
                    await Bot.kick_participant(Target,int(User.id)) 
                    i = i + 1 
            except : 
                pass 
    print(f'[!] Deleted {i} User From {Target} !') 
with Bot : 
    Bot.loop.run_until_complete(Main()) 
os.remove('MemeberRomover.session')
