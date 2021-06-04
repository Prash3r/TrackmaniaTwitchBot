import logging
import re

async def EVAL_ping(self, ctx) -> bool:
    # This eval function checks every message
    # for the occurance of the word ping
    # and answeres with the word pong
    if re.search(r'(ping)\b', ctx.content.lower()):
        await ctx.channel.send("pong")
        logging.info("EVAL_ping() did trigger")
        return True
    else:
        return False