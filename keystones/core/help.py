from discord.ext import commands


class HelpCog:
    @commands.group(pass_context=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('''
Keystones is a bot that helps track mythic keystones.
**Available commands:**
`!help <command>` - shows a help message for that command.
`!add <character> <dungeon> <level>` - adds a keystone for the specified 
dungeon and level for your character with the given name.
`!keys` - gets all of your keystones. You can check someone else's keys by 
mentioning them.
`!dungeons` - lists all dungeons and some accepted alternative names.
                           ''')

    @help.command(aliases=['dungeon'],
                  pass_context=True)
    async def dungeons(self, ctx):
        await ctx.send('''
`!dungeons` - Lists all dungeons and some of their accepted alternative names.
                       ''')

    @help.command(name='add',
                  pass_context=True)
    async def add_key(self, ctx):
        await ctx.send('''
`!add <character> <dungeon> <level>` - adds a keystone for the specified 
dungeon and level for your character with the given name. This will overwrite 
any existing 
                       ''')

    @help.command(name='get',
                  aliases=['keys', 'key', 'keystones', 'keystone'],
                  pass_context=True)
    async def get_keys(self, ctx):
        await ctx.send('''
`!keys` - gets all of the caller's keystones.
`!keys @role` - gets all keystones for users with the mentioned role.
`!keys @user` - gets all keystones for the mentioned user.
`!keys @everyone` - gets all keystones for everyone in the server. 
Alternatively, you can use `!keys everyone` or `!keys all`.
!keys @here` - gets all keystones for online members in the server. 
Alternatively, you can use `!keys here` or `!keys online`.
You can also combine multiple mentions in one command.
                       ''')
