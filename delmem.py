from telethon import TelegramClient
import os
Bot = TelegramClient('MemeberRomover',int(input('17299114')),str(input('653741f09cbd2a8839c21cdf5fe46217'))).start(bot_token=str(input('5232848304:AAFyoNZigpThyz-FVMs9f2_NQulsuu9cmtQ')))
Target = input('@kulgu_vaqti_uz')
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
