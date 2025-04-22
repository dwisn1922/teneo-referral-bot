import sys
import os

# Tambahkan path root project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.bot import TeneoReferralBot

if __name__ == "__main__":
    print("Starting Teneo.Pro Referral Bot...")
    bot = TeneoReferralBot()
    bot.run()
