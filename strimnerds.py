#! /usr/bin/env python3
"""
A python script for running the strimnerds Discord bot.
"""
import discord

__version__ = '1.0'

name = "name"  # STREAMER NAME REQUIRED
url = "https://twitch.tv/" + name
client = discord.Client(activity=discord.Streaming(
    platform="Twitch",
    name=name,
    url=url,
    twitch_name=name)
)


@client.event
async def on_member_update(before, after):
    if (
        before.guild.id != 987654321987654321 or  # GUILD ID REQUIRED
        before.id != 987654321987654321 or  # USER ID REQUIRED
        before.activity.type is None or
        before.activity.type == discord.Streaming.type or
        after.activity.type is None or
        after.activity.type != discord.Streaming.type
    ):
        return

    await client.get_channel(987654321987654321).send(  # CHANNEL ID REQUIRED
        "%s is streaming! %s %s" % (
            name, url, after.guild.get_role(987654321987654321).mention  # ROLE ID REQUIRED
        )
    )


def main():
    client.run('xxx')


if __name__ == '__main__':
    main()
