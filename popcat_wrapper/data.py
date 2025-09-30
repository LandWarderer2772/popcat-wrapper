"""
Data & Information APIs Module

This module provides functions for retrieving real-world data and information.
All functions return structured dictionaries with comprehensive information.

Available Functions:
    - weather(place): Get current weather information for any location
    - github(username): Get GitHub user information and statistics
    - npm(package): Get NPM package details and statistics
    - steam(name): Search for games on Steam platform
    - imdb(name): Search for movies and TV shows on IMDB
    - country(name): Get detailed information about any country
    - periodic_table(element): Get periodic table element information
    - colorinfo(color): Get detailed information about any color
    - randomcolor(): Generate a random color with all formats
    - subreddit(subreddit_name): Get Reddit subreddit information
    - itunes(song): Search for songs on iTunes
"""

import requests
from typing import Dict, Any
from urllib.parse import quote

# Base URL for the Popcat API
BASE_URL = "https://api.popcat.xyz"

def _validate_text(text: str) -> None:
    """Validate that the provided text is valid."""
    if not text or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string")

def _make_request(endpoint: str, params: dict = None) -> Dict[str, Any]:
    """Make a request to the API and return JSON data."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params or {})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def weather(place: str) -> Dict[str, Any]:
    """
    Get current weather information for any location.
    
    Args:
        place (str): City or location name
        
    Returns:
        Dict[str, Any]: Weather data including temperature, conditions, humidity, etc.
        
    Raises:
        ValueError: If place name is invalid
        Exception: If API request fails
        
    Example:
        >>> weather_data = weather("London")
        >>> print(weather_data)
        {
            'location': 'London, England',
            'temperature': '15°C',
            'condition': 'Partly Cloudy',
            'humidity': '65%',
            'wind': '10 km/h',
            ...
        }
    """
    _validate_text(place)
    return _make_request("/weather", {"q": place})

def github(username: str) -> Dict[str, Any]:
    """
    Get GitHub user information and statistics.
    
    Args:
        username (str): GitHub username
        
    Returns:
        Dict[str, Any]: User profile data, repos, stats, followers, etc.
        
    Raises:
        ValueError: If username is invalid
        Exception: If API request fails
        
    Example:
        >>> user_data = github("octocat")
        >>> print(user_data)
        {
            'username': 'octocat',
            'name': 'The Octocat',
            'bio': 'GitHub mascot',
            'public_repos': 8,
            'followers': 9001,
            'following': 9,
            ...
        }
    """
    _validate_text(username)
    return _make_request("/github", {"user": username})

def npm(package: str) -> Dict[str, Any]:
    """
    Get NPM package details and statistics.
    
    Args:
        package (str): NPM package name
        
    Returns:
        Dict[str, Any]: Package information, downloads, version, dependencies
        
    Raises:
        ValueError: If package name is invalid
        Exception: If API request fails
        
    Example:
        >>> package_data = npm("express")
        >>> print(package_data)
        {
            'name': 'express',
            'version': '4.18.2',
            'description': 'Fast, unopinionated, minimalist web framework',
            'downloads': 25000000,
            'author': 'TJ Holowaychuk',
            ...
        }
    """
    _validate_text(package)
    return _make_request("/npm", {"q": package})

def steam(name: str) -> Dict[str, Any]:
    """
    Search for games on Steam platform.
    
    Args:
        name (str): Game name to search
        
    Returns:
        Dict[str, Any]: Game information, price, reviews, screenshots
        
    Raises:
        ValueError: If game name is invalid
        Exception: If API request fails
        
    Example:
        >>> game_data = steam("Portal 2")
        >>> print(game_data)
        {
            'name': 'Portal 2',
            'price': '$9.99',
            'rating': '96% Positive',
            'release_date': 'Apr 18, 2011',
            'developer': 'Valve',
            ...
        }
    """
    _validate_text(name)
    return _make_request("/steam", {"q": name})

def imdb(name: str) -> Dict[str, Any]:
    """
    Search for movies and TV shows on IMDB.
    
    Args:
        name (str): Movie/TV show name
        
    Returns:
        Dict[str, Any]: Movie/show details, ratings, cast, plot
        
    Raises:
        ValueError: If movie/show name is invalid
        Exception: If API request fails
        
    Example:
        >>> movie_data = imdb("The Matrix")
        >>> print(movie_data)
        {
            'title': 'The Matrix',
            'year': '1999',
            'rating': '8.7/10',
            'genre': 'Action, Sci-Fi',
            'director': 'Lana Wachowski, Lilly Wachowski',
            'cast': ['Keanu Reeves', 'Laurence Fishburne', ...],
            ...
        }
    """
    _validate_text(name)
    return _make_request("/imdb", {"q": name})

def country(name: str) -> Dict[str, Any]:
    """
    Get detailed information about any country.
    
    Args:
        name (str): Country name
        
    Returns:
        Dict[str, Any]: Country data, population, capital, currency, flag, etc.
        
    Raises:
        ValueError: If country name is invalid
        Exception: If API request fails
        
    Example:
        >>> country_data = country("Japan")
        >>> print(country_data)
        {
            'name': 'Japan',
            'capital': 'Tokyo',
            'population': 125800000,
            'currency': 'Japanese Yen',
            'flag': 'https://...',
            'continent': 'Asia',
            ...
        }
    """
    _validate_text(name)
    return _make_request("/country", {"name": name})

def periodic_table(element: str) -> Dict[str, Any]:
    """
    Get periodic table element information.
    
    Args:
        element (str): Element name or symbol (e.g., "Hydrogen" or "H")
        
    Returns:
        Dict[str, Any]: Element properties, atomic data, discovery info
        
    Raises:
        ValueError: If element name/symbol is invalid
        Exception: If API request fails
        
    Example:
        >>> element_data = periodic_table("Carbon")
        >>> print(element_data)
        {
            'name': 'Carbon',
            'symbol': 'C',
            'atomic_number': 6,
            'atomic_mass': '12.011',
            'group': 14,
            'period': 2,
            'category': 'Nonmetal',
            ...
        }
    """
    _validate_text(element)
    return _make_request("/periodic_table", {"element": element})

def colorinfo(color: str) -> Dict[str, Any]:
    """
    Get detailed information about any color.
    
    Args:
        color (str): Hex color code (e.g., "#FF0000") or color name (e.g., "red")
        
    Returns:
        Dict[str, Any]: Color data, RGB, HSL, CMYK values, name
        
    Raises:
        ValueError: If color format is invalid
        Exception: If API request fails
        
    Example:
        >>> color_data = colorinfo("#FF0000")
        >>> print(color_data)
        {
            'hex': '#FF0000',
            'rgb': {'r': 255, 'g': 0, 'b': 0},
            'hsl': {'h': 0, 's': 100, 'l': 50},
            'cmyk': {'c': 0, 'm': 100, 'y': 100, 'k': 0},
            'name': 'Red',
            ...
        }
    """
    _validate_text(color)
    return _make_request("/colorinfo", {"color": color})

def randomcolor() -> Dict[str, Any]:
    """
    Generate a random color with all formats.
    
    Returns:
        Dict[str, Any]: Random color with hex, RGB, HSL values, and name
        
    Raises:
        Exception: If API request fails
        
    Example:
        >>> random_color = randomcolor()
        >>> print(random_color)
        {
            'hex': '#3A7BD5',
            'rgb': {'r': 58, 'g': 123, 'b': 213},
            'hsl': {'h': 215, 's': 65, 'l': 53},
            'name': 'Steel Blue',
            ...
        }
    """
    return _make_request("/randomcolor")

def subreddit(subreddit_name: str) -> Dict[str, Any]:
    """
    Get Reddit subreddit information.
    
    Args:
        subreddit_name (str): Subreddit name (without r/ prefix)
        
    Returns:
        Dict[str, Any]: Subreddit statistics and information
        
    Raises:
        ValueError: If subreddit name is invalid
        Exception: If API request fails
        
    Example:
        >>> subreddit_data = subreddit("python")
        >>> print(subreddit_data)
        {
            'name': 'python',
            'title': 'Python',
            'description': 'News about the programming language Python',
            'subscribers': 1200000,
            'created': '2008-01-25',
            'is_nsfw': False,
            ...
        }
    """
    _validate_text(subreddit_name)
    # Remove r/ prefix if present
    if subreddit_name.startswith('r/'):
        subreddit_name = subreddit_name[2:]
    return _make_request("/subreddit", {"subreddit": subreddit_name})

def itunes(song: str) -> Dict[str, Any]:
    """
    Search for songs on iTunes.
    
    Args:
        song (str): Song name to search
        
    Returns:
        Dict[str, Any]: Song details, artist, album, preview, artwork
        
    Raises:
        ValueError: If song name is invalid
        Exception: If API request fails
        
    Example:
        >>> song_data = itunes("Bohemian Rhapsody")
        >>> print(song_data)
        {
            'track_name': 'Bohemian Rhapsody',
            'artist': 'Queen',
            'album': 'A Night at the Opera',
            'genre': 'Rock',
            'release_date': '1975-10-31',
            'preview_url': 'https://...',
            'artwork': 'https://...',
            ...
        }
    """
    _validate_text(song)
    return _make_request("/itunes", {"q": song})

# Export all functions
__all__ = [
    'weather', 'github', 'npm', 'steam', 'imdb', 'country', 
    'periodic_table', 'colorinfo', 'randomcolor', 'subreddit', 'itunes'
]