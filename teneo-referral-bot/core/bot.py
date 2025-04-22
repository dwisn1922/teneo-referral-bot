import requests
import time
from config import settings
from .utilities import get_random_user_agent, setup_logger

logger = setup_logger()

class TeneoReferralBot:
    def __init__(self):
        self.referral_link = settings.REFERRAL_LINK
        self.session = requests.Session()
        
    def simulate_visit(self):
        headers = {
            'User-Agent': get_random_user_agent(),
            'Referer': 'https://www.google.com/',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        
        try:
            response = self.session.get(
                self.referral_link,
                headers=headers,
                timeout=10
            )
            
            logger.info(f"Visit simulated - Status: {response.status_code}")
            return True
            
        except Exception as e:
            logger.error(f"Error during visit: {str(e)}")
            return False
    
    def run(self):
        from core.utilities import get_random_delay
        while True:
            success = self.simulate_visit()
            delay = get_random_delay()
            logger.info(f"Next attempt in {delay//60} minutes")
            time.sleep(delay)