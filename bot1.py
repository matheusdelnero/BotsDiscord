import discord
import os 

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'regras':  # se alguem digitar esse comando será exibida e seguinte mensagem:
            await message.channel.send(f'{message.author.name} as regras desse grupo são:{os.linesep} 1 - Respeitar os Amigos.{os.linesep} 2 - Dar Bença pro Teus{os.linesep} 3 - Falar Italiani')
        elif message.content == 'ajuda':
            await message.author.send('Deus Ajuda Quem Cedo Madruga!')
        elif message.content == 'botmaluco':
            await message.channel.send(f'Para Usar o Bot Digite:{os.linesep} "Regras" = Regras do Grupo.{os.linesep} "ajuda" = Mensagem Motivacional.{os.linesep} "botmaluco" = Comandos do Bot.')

    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} Acabou de Entrar No {guild.name}, Sinto Muito!'
            await guild.system_channel.send(mensagem)

intents = discord.Intents.default()
intents.members = True

        

client = MyClient()
client.run('OTYyNTAzNzAwMDIxMTI5MjM3.YlIfbA.QG8s2NmGhK9fDq_WjoFRMOQjhm0')