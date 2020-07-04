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
`!affix <affix_name>` - gets information about the specified affix.
`!affixes <offset>` - lists information about affixes for <offset> weeks into the future. The offset defaults to 0 and only supports integer offsets of 0-11.
`!timer <dungeon>` - gets information about keystone timers for the specified dungeon.
                           ''')

    @help.command(aliases=['dungeon'],
                  pass_context=True)
    async def dungeons(self, ctx):
        await ctx.send(f'''
`!{ctx.subcommand_passed}` - lists all dungeons and some of their accepted alternative names.
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
`!affixes <offset>` - lists information about affixes for <offset> weeks into the future. Only supports integer offsets of 0-11.
                       ''')

    @help.command(name='timer',
                  aliases=['timers'],
                  pass_context=True)
    async def get_dungeon_timers(self, ctx):
        await ctx.send(f'''
`!{ctx.subcommand_passed} <dungeon>` - gets information about how quickly you must complete the specified dungeon for a +1, +2, or +3 upgrade.
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
        await ctx.send(f'''
`!{ctx.subcommand_passed}` - gets all of the caller's keystones.
`!{ctx.subcommand_passed} @role` - gets all keystones for users with the mentioned role.
`!{ctx.subcommand_passed} @user` - gets all keystones for the mentioned user.
`!{ctx.subcommand_passed} @everyone` - gets all keystones for everyone in the server.
Alternatively, you can use `!{ctx.subcommand_passed} everyone` or `!{ctx.subcommand_passed} all`.
`!{ctx.subcommand_passed} @here` - gets all keystones for online members in the server.
Alternatively, you can use `!{ctx.subcommand_passed} here` or `!{ctx.subcommand_passed} online`.
You can also combine multiple mentions in one command.
                       ''')
