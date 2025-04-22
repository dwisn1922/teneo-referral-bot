import random
import logging
from datetime import datetime

def setup_logger():
    logging.basicConfig(
        filename='logs/referral.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()

def get_random_user_agent():
    with open('config/user_agents.txt', 'r') as f:
        agents = [line.strip() for line in f if line.strip()]
    return random.choice(agents)

def get_random_delay():
    from config import settings
    return random.randint(settings.MIN_DELAY, settings.MAX_DELAY)