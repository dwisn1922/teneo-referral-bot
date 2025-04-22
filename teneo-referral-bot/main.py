import sys
import os
from core.bot import TeneoReferralBot

# Tambahkan path root project ke Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    print("Starting Teneo.Pro Referral Bot...")
    bot = TeneoReferralBot()
    bot.run()
