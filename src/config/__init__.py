import os
from dotenv import load_dotenv


def load_env_variables():
    """Load and validate environment variables from .env file."""
    load_dotenv()
    api_key = os.getenv("APCA_API_KEY_ID")
    api_secret = os.getenv("APCA_API_SECRET_KEY")
    base_url = "https://paper-api.alpaca.markets"  # Paper trading URL

    if not api_key or not api_secret:
        raise ValueError("API_KEY or API_SECRET not found in .env file")

    return {"api_key": api_key, "api_secret": api_secret, "base_url": base_url}
