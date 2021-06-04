import logging
import re

async def EVAL_ooga(self, ctx):
    if re.search(r'(ooga)\b', ctx.content.lower()):
        await ctx.channel.send("booga")
        logging.info("EVAL_ooga() did trigger")
        return True
    else:
        return False