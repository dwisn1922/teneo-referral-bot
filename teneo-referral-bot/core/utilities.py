import random
import logging
import os
from pathlib import Path

def setup_logger():
    logging.basicConfig(
        filename='logs/referral.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()

def get_random_user_agent():
    # Dapatkan path absolut ke file user_agents.txt
    current_dir = Path(__file__).parent
    agents_file = current_dir.parent / 'config' / 'user_agents.txt'
    
    with open(agents_file, 'r') as f:
        agents = [line.strip() for line in f if line.strip()]
    return random.choice(agents)

def get_random_delay():
    from config.settings import MIN_DELAY, MAX_DELAY
    return random.randint(MIN_DELAY, MAX_DELAY)
