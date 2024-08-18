import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is online and ready to manage tickets!')

@bot.command()
async def ticket(ctx):
    """Creates a new support ticket for the user."""
    # Create a new channel for the ticket
    guild = ctx.guild
    category = discord.utils.get(guild.categories, name='Tickets')
    
    if not category:
        category = await guild.create_category('Tickets')

    ticket_channel = await category.create_text_channel(f'ticket-{ctx.author.name}')
    await ticket_channel.set_permissions(guild.default_role, read_messages=False)
    await ticket_channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
    
    await ticket_channel.send(f'{ctx.author.mention} This is your support ticket channel. Please describe your issue here.')
    
    # Notify the user
    await ctx.send(f'Ticket created! {ticket_channel.mention}')

@bot.command()
@commands.has_permissions(administrator=True)
async def close(ctx):
    """Closes a support ticket."""
    if ctx.channel.category and ctx.channel.category.name == 'Tickets':
        await ctx.channel.send('Closing the ticket...')
        await asyncio.sleep(5)  # Wait for 5 seconds before deleting the channel
        await ctx.channel.delete()
    else:
        await ctx.send("You can only use this command in a ticket channel.")

# Replace 'YOUR_BOT_TOKEN' with your Discord bot token
bot.run('YOUR_BOT_TOKEN')
