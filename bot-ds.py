import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'Привет всем':
            await message.channel.send('Привет')

        if message.content == 'Всем привет':
            await message.channel.send('Привет')

        if message.content == 'всем привет':
            await message.channel.send('Привет')

        if message.content == 'я ебал твою мать':
            await message.channel.send('Мою :(')

        if message.content == '300':
            await message.channel.send('Отсоси у тракториста')

        if message.content == '150+150':
            await message.channel.send('Отсоси у поросят')

        if message.content == 'Эдик':
            await message.channel.send('Педик')

        if message.content == 'Алекс любит...':
            await message.channel.send('Какишь')

        if message.content == 'Иди нахуй':
            await message.channel.send('СИРЕНА ВИУ ВИУ ВИУ ВИУ:loudspeaker:')

        if message.content == 'Я чмо':
            await message.channel.send('ок.')

        if message.content == 'купить премиум':
            await message.channel.send('чтобы купить премиум отпишите создателю Traf#5647')

        if message.content == 'Купить премиум':
            await message.channel.send('чтобы купить премиум отпишите создателю Traf#5647')

        if message.content == 'Ты ботяра':
            await message.channel.send('Опхуел сам такой')

        if message.content == 'Мать ебал':
            await message.channel.send('Охуел щяс забаню')

        if message.content == 'Ты бот':
            await message.channel.send('Я знаю и что')

        if message.content == 'я твою мать ебал':
            await message.channel.send('Мою :(')

        if message.content == 'Я твою мать ебал':
            await message.channel.send('Мою :(')

        if message.content == 'Мать в канаве':
            await message.channel.send('Охуела дочь шлюхи щяс в бан отлетишь')

        if message.content == 'мать в канаве':
            await message.channel.send('Охуела дочь шлюхи щяс в бан отлетишь')

        if message.content == 'Пошел нахуй бот ебаный':
            await message.channel.send('Охуела дочь окушерки, щяс в бан отлетишь шпрот ходячий')

        if message.content == 'Безмамный':
            await message.channel.send('СИРЕНА ВИУ ВИУ ВИУ ВИУ ВИУ ВИУ ВИУ')

        if message.content == 'серв хуйня':
            await message.channel.send('Охуел!??!?! если тут есть я,значит серв идеальный! :heart:')

        if message.content == 'создатель':
            await message.channel.send('Создатель прекраного бота Traf#5647')

        if message.content == 'Cоздатель':
            await message.channel.send('Создатель прекраного бота Traf#5647')

        if message.content == 'я твою маму ебал':
            await message.channel.send('слыш безмамное существо ебало офни')

        if message.content == 'Вчера я прилетел в узбекистан и там были арабы в моем шкафу и начинают раздевать меня':
            await message.channel.send(' А потом тебя трахает мшк фреде и 283838 арабов и поют песню у меня нет проблем кроме моей бошки 1000-7 я умер прости ')

        if message.content == 'бот':
            await message.channel.send('Я знаю и что')

        if message.content == 'Я люблю когда...':
            await message.channel.send('Я люблю когда волосатые мужики обмазываються маслом')

        if message.content == 'Бот':
            await message.channel.send('Я знаю и что')

        if message.content == 'Ботик':
            await message.channel.send('Я знаю и что')

        if message.content == 'ботик':
            await message.channel.send('Я знаю и что')
client = MyClient()
client.run('OTQwNjk1NDk2OTEyMTY3MDIy.YgLI8w.ZMlKTbC3L9FejNK5QpYYzedToEU')