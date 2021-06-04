import logging
import re

async def EVAL_luckerscounter(self, ctx) -> bool:
    # This evaluation checks if LuckersTurbo was called Luckers
    # in every message and counts occurences persistently in the Database
    if re.search(r'(luckers)\b', ctx.content.lower()):
        oldval = self.DB_GetPV('luckerscounter')
        newval = oldval + 1
        await ctx.channel.send(f"Turbo was called Luckers for {newval} times ... please just dont, @{ctx.author.name}!")
        self.DB_WritePV('luckerscounter', str(newval), str(oldval))
        logging.info("EVAL_luckerscounter() did trigger")
        return True
    else:
        return False