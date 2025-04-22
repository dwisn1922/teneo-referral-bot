import sys
import os

# Pastikan path benar
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from core.bot import TeneoReferralBot

if __name__ == "__main__":
    print("Starting bot...")
    bot = TeneoReferralBot()
    bot.run()
