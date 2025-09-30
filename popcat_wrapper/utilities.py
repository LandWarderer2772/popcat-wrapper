"""
Utilities Module

This module provides general utility functions for various purposes.
Functions return different types depending on their specific functionality.

Available Functions:
    - lyrics(song): Get lyrics for any song
    - screenshot(url): Take a screenshot of any website
    - chatbot(message, ownername, botname): Get AI chatbot response
    - welcomecard(background, avatar, text_1, text_2, text_3): Generate custom welcome card
"""

import requests
from typing import Dict, Any
from urllib.parse import quote, urlparse

# Base URL for the Popcat API
BASE_URL = "https://api.popcat.xyz"

def _validate_text(text: str) -> None:
    """Validate that the provided text is valid."""
    if not text or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string")

def _validate_url(url: str) -> None:
    """Validate that the provided string is a valid URL."""
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")
    
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError("URL must be a valid HTTP/HTTPS URL")
    
    if parsed.scheme not in ['http', 'https']:
        raise ValueError("URL must use HTTP or HTTPS protocol")

def _make_json_request(endpoint: str, params: dict) -> Dict[str, Any]:
    """Make a request to the API and return JSON data."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def _make_request(endpoint: str, params: dict) -> str:
    """Make a request to the API and return the response URL or content."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        return response.url
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def lyrics(song: str) -> Dict[str, Any]:
    """
    Get lyrics for any song.
    
    Args:
        song (str): Song name or "artist - song" format
        
    Returns:
        Dict[str, Any]: Song lyrics and metadata including title, artist, album
        
    Raises:
        ValueError: If song name is invalid
        Exception: If API request fails
        
    Example:
        >>> song_lyrics = lyrics("Bohemian Rhapsody Queen")
        >>> print(song_lyrics)
        {
            'title': 'Bohemian Rhapsody',
            'artist': 'Queen',
            'album': 'A Night at the Opera',
            'lyrics': 'Is this the real life? Is this just fantasy?...',
            'length': 355,
            'release_date': '1975-10-31',
            ...
        }
        
        >>> song_lyrics = lyrics("Taylor Swift - Shake It Off")
        >>> print(song_lyrics)
        {
            'title': 'Shake It Off',
            'artist': 'Taylor Swift',
            'album': '1989',
            'lyrics': 'I stay out too late, got nothing in my brain...',
            ...
        }
    """
    _validate_text(song)
    return _make_json_request("/lyrics", {"song": song})

def screenshot(url: str) -> str:
    """
    Take a screenshot of any website.
    
    Args:
        url (str): Valid website URL to screenshot
        
    Returns:
        str: URL of the screenshot image
        
    Raises:
        ValueError: If URL is invalid
        Exception: If API request fails
        
    Example:
        >>> screenshot_url = screenshot("https://github.com")
        >>> print(screenshot_url)
        https://api.popcat.xyz/screenshot?url=https%3A//github.com
        
        >>> screenshot_url = screenshot("https://stackoverflow.com")
        >>> print(screenshot_url)
        https://api.popcat.xyz/screenshot?url=https%3A//stackoverflow.com
    """
    _validate_url(url)
    return _make_request("/screenshot", {"url": url})

def chatbot(message: str, ownername: str, botname: str) -> Dict[str, Any]:
    """
    Get AI chatbot response.
    
    Args:
        message (str): Message to send to chatbot
        ownername (str): Name of the bot owner
        botname (str): Name of the bot
        
    Returns:
        Dict[str, Any]: Bot response and metadata
        
    Raises:
        ValueError: If any parameter is invalid
        Exception: If API request fails
        
    Example:
        >>> bot_response = chatbot("Hello there!", "John", "MyBot")
        >>> print(bot_response)
        {
            'response': 'Hello! How can I help you today?',
            'botname': 'MyBot',
            'ownername': 'John',
            'message': 'Hello there!',
            'timestamp': '2023-01-15T10:30:00Z',
            ...
        }
        
        >>> bot_response = chatbot("What's the weather like?", "Alice", "WeatherBot")
        >>> print(bot_response)
        {
            'response': 'I would need your location to tell you about the weather!',
            'botname': 'WeatherBot',
            'ownername': 'Alice',
            ...
        }
    """
    _validate_text(message)
    _validate_text(ownername)
    _validate_text(botname)
    
    return _make_json_request("/chatbot", {
        "msg": message,
        "owner": ownername,
        "botname": botname
    })

def welcomecard(background: str, avatar: str, text_1: str, text_2: str, text_3: str) -> str:
    """
    Generate custom welcome card for servers.
    
    Args:
        background (str): Background image URL (must be PNG, HTTPS)
        avatar (str): User avatar image URL
        text_1 (str): Welcome text line 1 (e.g., "Welcome")
        text_2 (str): Welcome text line 2 (e.g., username)
        text_3 (str): Welcome text line 3 (e.g., server info)
        
    Returns:
        str: URL of the welcome card image
        
    Raises:
        ValueError: If any parameter is invalid
        Exception: If API request fails
        
    Example:
        >>> welcome_img = welcomecard(
        ...     "https://example.com/bg.png",
        ...     "https://example.com/avatar.jpg", 
        ...     "Welcome",
        ...     "John Doe",
        ...     "to our awesome server!"
        ... )
        >>> print(welcome_img)
        https://api.popcat.xyz/welcomecard?background=...&avatar=...
        
        >>> welcome_img = welcomecard(
        ...     "https://example.com/space_bg.png",
        ...     "https://example.com/user_avatar.png",
        ...     "Welcome back",
        ...     "Alice",
        ...     "You are member #1337"
        ... )
    """
    _validate_url(background)
    _validate_url(avatar)
    _validate_text(text_1)
    _validate_text(text_2)
    _validate_text(text_3)
    
    # Additional validation for background image
    if not background.lower().endswith('.png'):
        raise ValueError("Background image must be a PNG file")
    if not background.startswith('https://'):
        raise ValueError("Background image URL must use HTTPS")
    
    return _make_request("/welcomecard", {
        "background": background,
        "avatar": avatar,
        "text1": text_1,
        "text2": text_2, 
        "text3": text_3
    })

# Export all functions
__all__ = [
    'lyrics', 'screenshot', 'chatbot', 'welcomecard'
]