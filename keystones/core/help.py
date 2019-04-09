from discord.ext import commands


class HelpCog():
    @commands.command(pass_context=True)
    async def help(self, ctx, *args):
        await ctx.send('''
Keystones helps track your mythic keystones.
**Available commands:**
`!help <command>` - shows a help message for that 
command.
`!add <character> <dungeon> <level>` - adds a keystone 
for the specified dungeon and level for your 
character with the given name.
`!keys` - gets all of your keystones. You can check 
someone else's keys by mentioning them.
`!dungeons` - lists all dungeons and some accepted 
alternative names.
                       ''')
