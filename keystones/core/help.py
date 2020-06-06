from discord.ext import commands


class HelpCog(commands.Cog):
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

    @help.command(name='affix',
                 pass_context=True)
    async def get_affix_details(self, ctx):
        await ctx.send('''
`!affix <affix_name>` - gets information about the specified affix.
                       ''')

    @help.command(name='affixes',
                 pass_context=True)
    async def get_period_affixes(self, ctx):
        await ctx.send('''
`!affixes` - lists information about affixes for this week.
`!affixes <offset>` - lists information about affixes for <offset> weeks into the future. Only supports an integer offset of 0-12.
                       ''')

    @help.command(name='timer',
                 aliases=['timers'],
                 pass_context=True)
    async def get_dungeon_timers(self, ctx):
        await ctx.send(f'''
`!{ctx.subcommand_passed} <dungeon>` - gets information about keystone timers for the specified dungeon.
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
`!keys @here` - gets all keystones for online members in the server.
Alternatively, you can use `!keys here` or `!keys online`.
You can also combine multiple mentions in one command.
                       ''')
