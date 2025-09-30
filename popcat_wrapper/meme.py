"""
Meme Generation Module

This module provides functions for creating popular meme formats with custom text and images.
Most functions return image URLs as strings.

Available Functions:
    - drake(text1, text2): Generate Drake pointing meme format
    - pooh(text1, text2): Generate Winnie the Pooh meme format
    - ship(image1, image2): Generate ship compatibility meme with percentage
    - supreme(text): Generate Supreme-style logo with custom text
    - oogway(text): Generate Master Oogway wisdom quote meme
    - biden(text): Generate Biden tweet-style meme
    - pikachu(text): Generate surprised Pikachu meme
    - sadcat(text): Generate sad cat meme with custom text
    - opinion(image, text): Generate "opinion" meme format
    - discord_message(username, content, avatar=None, color=None, timestamp=None): Generate Discord message screenshot
    - quote(image, text, name): Generate inspirational quote image
    - happysad(text1, text2): Generate happy vs sad comparison meme
    - unforgivable(text): Generate "unforgivable" curse meme
    - couldread(text): Generate "could you please read" meme
    - lulcat(text): Generate lulcat/lolcat meme
    - facts(text): Generate "facts" meme with custom text
    - alert(text): Generate warning alert sign
    - caution(text): Generate caution warning sign
"""

import requests
from typing import Optional, Dict, Any
from urllib.parse import quote

# Base URL for the Popcat API
BASE_URL = "https://api.popcat.xyz"

def _validate_text(text: str, max_length: Optional[int] = None) -> None:
    """Validate that the provided text is valid."""
    if not text or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string")
    if max_length and len(text) > max_length:
        raise ValueError(f"Text must be {max_length} characters or less")

def _validate_image_url(image_url: str) -> None:
    """Validate that the provided string is a valid image URL."""
    if not image_url or not isinstance(image_url, str):
        raise ValueError("Image URL must be a non-empty string")
    if not (image_url.startswith('http://') or image_url.startswith('https://')):
        raise ValueError("Image URL must start with http:// or https://")

def _make_request(endpoint: str, params: dict) -> str:
    """Make a request to the API and return the image URL."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        return response.url
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def _make_json_request(endpoint: str, params: dict) -> Dict[str, Any]:
    """Make a request to the API and return JSON data."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def drake(text1: str, text2: str) -> str:
    """
    Generate Drake pointing meme format.
    
    Args:
        text1 (str): Text for the "rejection" panel (Drake looking away)
        text2 (str): Text for the "approval" panel (Drake pointing)
        
    Returns:
        str: URL of the Drake meme
        
    Raises:
        ValueError: If text parameters are invalid
        Exception: If API request fails
        
    Example:
        >>> drake_meme = drake("Using other APIs", "Using Popcat API")
        >>> print(drake_meme)
        https://api.popcat.xyz/drake?text1=...&text2=...
    """
    _validate_text(text1)
    _validate_text(text2)
    return _make_request("/drake", {"text1": text1, "text2": text2})

def pooh(text1: str, text2: str) -> str:
    """
    Generate Winnie the Pooh meme format.
    
    Args:
        text1 (str): Text for regular Pooh (normal behavior)
        text2 (str): Text for fancy Pooh (sophisticated behavior)
        
    Returns:
        str: URL of the Pooh meme
        
    Raises:
        ValueError: If text parameters are invalid
        Exception: If API request fails
        
    Example:
        >>> pooh_meme = pooh("Eating honey", "Consuming apiary nectar")
        >>> print(pooh_meme)
        https://api.popcat.xyz/pooh?text1=...&text2=...
    """
    _validate_text(text1)
    _validate_text(text2)
    return _make_request("/pooh", {"text1": text1, "text2": text2})

def ship(image1: str, image2: str) -> str:
    """
    Generate ship compatibility meme with percentage.
    
    Args:
        image1 (str): URL of first person's image
        image2 (str): URL of second person's image
        
    Returns:
        str: URL of the ship compatibility meme
        
    Raises:
        ValueError: If image URLs are invalid
        Exception: If API request fails
        
    Example:
        >>> ship_meme = ship("https://example.com/person1.jpg", "https://example.com/person2.jpg")
        >>> print(ship_meme)
        https://api.popcat.xyz/ship?user1=...&user2=...
    """
    _validate_image_url(image1)
    _validate_image_url(image2)
    return _make_request("/ship", {"user1": image1, "user2": image2})

def supreme(text: str) -> str:
    """
    Generate Supreme-style logo with custom text.
    
    Args:
        text (str): Custom text for the logo
        
    Returns:
        str: URL of the Supreme logo image
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> supreme_logo = supreme("POPCAT")
        >>> print(supreme_logo)
        https://api.popcat.xyz/supreme?text=POPCAT
    """
    _validate_text(text)
    return _make_request("/supreme", {"text": text})

def oogway(text: str) -> str:
    """
    Generate Master Oogway wisdom quote meme.
    
    Args:
        text (str): Quote text
        
    Returns:
        str: URL of the Oogway meme
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> wisdom = oogway("There are no accidents")
        >>> print(wisdom)
        https://api.popcat.xyz/oogway?text=...
    """
    _validate_text(text)
    return _make_request("/oogway", {"text": text})

def biden(text: str) -> str:
    """
    Generate Biden tweet-style meme.
    
    Args:
        text (str): Tweet content
        
    Returns:
        str: URL of the Biden tweet meme
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> biden_tweet = biden("Listen, Jack...")
        >>> print(biden_tweet)
        https://api.popcat.xyz/biden?text=...
    """
    _validate_text(text)
    return _make_request("/biden", {"text": text})

def pikachu(text: str) -> str:
    """
    Generate surprised Pikachu meme.
    
    Args:
        text (str): Text for the meme
        
    Returns:
        str: URL of the Pikachu meme
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> pikachu_meme = pikachu("When you realize it's Monday")
        >>> print(pikachu_meme)
        https://api.popcat.xyz/pikachu?text=...
    """
    _validate_text(text)
    return _make_request("/pikachu", {"text": text})

def sadcat(text: str) -> str:
    """
    Generate sad cat meme with custom text.
    
    Args:
        text (str): Text for the sad cat
        
    Returns:
        str: URL of the sad cat meme
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> sad_meme = sadcat("No more treats")
        >>> print(sad_meme)
        https://api.popcat.xyz/sadcat?text=...
    """
    _validate_text(text)
    return _make_request("/sadcat", {"text": text})

def opinion(image: str, text: str) -> str:
    """
    Generate "opinion" meme format.
    
    Args:
        image (str): URL of the person's image
        text (str): Opinion text
        
    Returns:
        str: URL of the opinion meme
        
    Raises:
        ValueError: If image URL or text is invalid
        Exception: If API request fails
        
    Example:
        >>> opinion_meme = opinion("https://example.com/person.jpg", "Pineapple belongs on pizza")
        >>> print(opinion_meme)
        https://api.popcat.xyz/opinion?image=...&text=...
    """
    _validate_image_url(image)
    _validate_text(text)
    return _make_request("/opinion", {"image": image, "text": text})

def discord_message(username: str, content: str, avatar: Optional[str] = None, 
                   color: Optional[str] = None, timestamp: Optional[str] = None) -> str:
    """
    Generate Discord message screenshot.
    
    Args:
        username (str): Discord username
        content (str): Message content
        avatar (str, optional): Avatar image URL
        color (str, optional): User role color (hex code)
        timestamp (str, optional): Message timestamp
        
    Returns:
        str: URL of the Discord message image
        
    Raises:
        ValueError: If required parameters are invalid
        Exception: If API request fails
        
    Example:
        >>> discord_msg = discord_message("CoolUser", "Hello everyone!")
        >>> discord_msg_custom = discord_message("Dev", "New feature deployed!", 
        ...                                      avatar="https://example.com/avatar.png",
        ...                                      color="#FF5733")
        >>> print(discord_msg)
        https://api.popcat.xyz/discord?username=...&content=...
    """
    _validate_text(username)
    _validate_text(content)
    
    params = {"username": username, "content": content}
    if avatar:
        _validate_image_url(avatar)
        params["avatar"] = avatar
    if color:
        params["color"] = color
    if timestamp:
        params["timestamp"] = timestamp
        
    return _make_request("/discord", params)

def quote(image: str, text: str, name: str) -> str:
    """
    Generate inspirational quote image.
    
    Args:
        image (str): URL of the person's image
        text (str): Quote text (1-125 characters)
        name (str): Name of the person
        
    Returns:
        str: URL of the quote image
        
    Raises:
        ValueError: If parameters are invalid
        Exception: If API request fails
        
    Example:
        >>> quote_img = quote("https://example.com/einstein.jpg", 
        ...                   "Imagination is more important than knowledge", 
        ...                   "Albert Einstein")
        >>> print(quote_img)
        https://api.popcat.xyz/quote?image=...&text=...&name=...
    """
    _validate_image_url(image)
    _validate_text(text, max_length=125)
    _validate_text(name)
    
    return _make_request("/quote", {"image": image, "text": text, "name": name})

def happysad(text1: str, text2: str) -> str:
    """
    Generate happy vs sad comparison meme.
    
    Args:
        text1 (str): Text for happy side
        text2 (str): Text for sad side
        
    Returns:
        str: URL of the happy/sad meme
        
    Raises:
        ValueError: If text parameters are invalid
        Exception: If API request fails
        
    Example:
        >>> happysad_meme = happysad("Friday", "Monday")
        >>> print(happysad_meme)
        https://api.popcat.xyz/happysad?text1=...&text2=...
    """
    _validate_text(text1)
    _validate_text(text2)
    return _make_request("/happysad", {"text1": text1, "text2": text2})

def unforgivable(text: str) -> str:
    """
    Generate "unforgivable" curse meme.
    
    Args:
        text (str): Text for the meme
        
    Returns:
        str: URL of the unforgivable meme
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> unforgivable_meme = unforgivable("Using Internet Explorer")
        >>> print(unforgivable_meme)
        https://api.popcat.xyz/unforgivable?text=...
    """
    _validate_text(text)
    return _make_request("/unforgivable", {"text": text})

def couldread(text: str) -> str:
    """
    Generate "could you please read" meme.
    
    Args:
        text (str): Text for the meme
        
    Returns:
        str: URL of the meme
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> read_meme = couldread("the documentation")
        >>> print(read_meme)
        https://api.popcat.xyz/couldread?text=...
    """
    _validate_text(text)
    return _make_request("/couldread", {"text": text})

def lulcat(text: str) -> Dict[str, Any]:
    """
    Generate lulcat/lolcat meme.
    
    Args:
        text (str): Text for the meme
        
    Returns:
        Dict[str, Any]: Meme data with URL
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> lulcat_data = lulcat("I can haz cheezburger?")
        >>> print(lulcat_data)
        {'url': 'https://api.popcat.xyz/lulcat?text=...', ...}
    """
    _validate_text(text)
    return _make_json_request("/lulcat", {"text": text})

def facts(text: str) -> str:
    """
    Generate "facts" meme with custom text.
    
    Args:
        text (str): Fact text
        
    Returns:
        str: URL of the facts meme
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> facts_meme = facts("Python is awesome")
        >>> print(facts_meme)
        https://api.popcat.xyz/facts?text=...
    """
    _validate_text(text)
    return _make_request("/facts", {"text": text})

def alert(text: str) -> str:
    """
    Generate warning alert sign.
    
    Args:
        text (str): Alert message
        
    Returns:
        str: URL of the alert sign
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> alert_sign = alert("DANGER: High Voltage")
        >>> print(alert_sign)
        https://api.popcat.xyz/alert?text=...
    """
    _validate_text(text)
    return _make_request("/alert", {"text": text})

def caution(text: str) -> str:
    """
    Generate caution warning sign.
    
    Args:
        text (str): Caution message
        
    Returns:
        str: URL of the caution sign
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> caution_sign = caution("Wet Floor")
        >>> print(caution_sign)
        https://api.popcat.xyz/caution?text=...
    """
    _validate_text(text)
    return _make_request("/caution", {"text": text})

# Export all functions
__all__ = [
    'drake', 'pooh', 'ship', 'supreme', 'oogway', 'biden', 'pikachu', 
    'sadcat', 'opinion', 'discord_message', 'quote', 'happysad', 
    'unforgivable', 'couldread', 'lulcat', 'facts', 'alert', 'caution'
]