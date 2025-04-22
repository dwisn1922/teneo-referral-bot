import sys
import os

# Tambahkan path root ke Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from core.bot import TeneoReferralBot

if __name__ == "__main__":
    print("Starting Teneo.Pro Referral Bot...")
    bot = TeneoReferralBot()
    bot.run()
