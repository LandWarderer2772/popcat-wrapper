"""
Popcat API Python Wrapper

A comprehensive Python wrapper for the Popcat API (https://popcat.xyz/api).
Provides access to over 60 endpoints including image manipulation, meme generation,
data retrieval, text utilities, and more.

Example:
    import popcat_wrapper as popcat
    
    # Generate a meme
    drake_meme = popcat.drake("Regular APIs", "Popcat API")
    
    # Get weather data  
    weather = popcat.weather("London")
    
    # Apply image filter
    jail_image = popcat.jail("https://example.com/image.png")

Modules:
    - image: Image manipulation and filters
    - meme: Meme generators and templates
    - data: Real-world data and information APIs
    - text: Text transformation utilities
    - random: Random content generators
    - utilities: General utility functions
    - classes: Specialized service classes (CodeClient, Shortener)
"""

__version__ = "1.0.0"
__author__ = "land_lmao"
__email__ = "mh3as81gb@mozmail.com"
__description__ = "A comprehensive Python wrapper for the Popcat API"
__url__ = "https://github.com/LandWarderer2772/popcat-wrapper"

# Import all modules for easy access
from .image import *
from .meme import *
from .data import *
from .text import *
from .random import *
from .utilities import *
from .classes import *

# Define what gets imported with "from popcat_wrapper import *"
__all__ = [
    # Image manipulation functions
    'jail', 'blur', 'invert', 'greyscale', 'drip', 'clown', 'colorify', 
    'wanted', 'gun', 'ad', 'uncover', 'communism', 'jokeoverhead', 'mnm',
    
    # Meme generation functions
    'drake', 'pooh', 'ship', 'supreme', 'oogway', 'biden', 'pikachu', 
    'sadcat', 'opinion', 'discord_message', 'quote', 'happysad', 
    'unforgivable', 'couldread', 'lulcat', 'facts', 'alert', 'caution',
    
    # Data API functions
    'weather', 'github', 'npm', 'steam', 'imdb', 'country', 'periodic_table',
    'colorinfo', 'randomcolor', 'subreddit', 'itunes',
    
    # Text utility functions
    'translate', 'reverse', 'mock', 'doublestruck', 'texttomorse', 'encode', 'decode',
    
    # Random content functions
    'joke', 'fact', 'randommeme', 'car', 'showerthought', 'wouldyourather', 
    'eightball', '_8ball',
    
    # Utility functions
    'lyrics', 'screenshot', 'chatbot', 'welcomecard',
    
    # Specialized classes
    'CodeClient', 'Shortener'
]