"""
Image Manipulation Module

This module provides functions for applying various filters and effects to images.
All functions return image URLs as strings.

Available Functions:
    - jail(image_url): Apply jail filter overlay to an image
    - blur(image): Apply blur filter to an image  
    - invert(image): Invert all colors in the image
    - greyscale(image): Convert image to greyscale/black and white
    - drip(image): Apply drip effect filter to an image
    - clown(image): Apply clown makeup filter to an image
    - colorify(image, color): Apply color filter/tint to an image
    - wanted(image): Generate a "WANTED" poster with the provided image
    - gun(image, text=None): Generate gun meme with image
    - ad(image): Generate advertisement-style meme
    - uncover(image): Apply uncover filter effect
    - communism(image_url): Apply communism filter with red overlay and symbols
    - jokeoverhead(image): Generate "joke over head" meme format
    - mnm(image): Generate M&M-style meme with the image
"""

import requests
from typing import Optional
from urllib.parse import quote

# Base URL for the Popcat API
BASE_URL = "https://api.popcat.xyz"

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
        return response.url  # Return the final URL which points to the generated image
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def jail(image_url: str) -> str:
    """
    Apply jail filter overlay to an image.
    
    Args:
        image_url (str): URL of the image to process
        
    Returns:
        str: URL of the processed image with jail overlay
        
    Raises:
        ValueError: If image_url is invalid
        Exception: If API request fails
        
    Example:
        >>> jail_image = jail("https://example.com/image.png")
        >>> print(jail_image)
        https://api.popcat.xyz/jail?image=...
    """
    _validate_image_url(image_url)
    return _make_request("/jail", {"image": image_url})

def blur(image: str) -> str:
    """
    Apply blur filter to an image.
    
    Args:
        image (str): URL of the image to blur
        
    Returns:
        str: URL of the blurred image
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> blurred = blur("https://example.com/photo.jpg")
        >>> print(blurred)
        https://api.popcat.xyz/blur?image=...
    """
    _validate_image_url(image)
    return _make_request("/blur", {"image": image})

def invert(image: str) -> str:
    """
    Invert all colors in the image.
    
    Args:
        image (str): URL of the image to invert
        
    Returns:
        str: URL of the inverted image
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> inverted = invert("https://example.com/image.png")
        >>> print(inverted)
        https://api.popcat.xyz/invert?image=...
    """
    _validate_image_url(image)
    return _make_request("/invert", {"image": image})

def greyscale(image: str) -> str:
    """
    Convert image to greyscale/black and white.
    
    Args:
        image (str): URL of the image to convert
        
    Returns:
        str: URL of the greyscale image
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> grey_image = greyscale("https://example.com/colorful.jpg")
        >>> print(grey_image)
        https://api.popcat.xyz/greyscale?image=...
    """
    _validate_image_url(image)
    return _make_request("/greyscale", {"image": image})

def drip(image: str) -> str:
    """
    Apply drip effect filter to an image.
    
    Args:
        image (str): URL of the image
        
    Returns:
        str: URL of the processed image with drip effect
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> drip_image = drip("https://example.com/image.png")
        >>> print(drip_image)
        https://api.popcat.xyz/drip?image=...
    """
    _validate_image_url(image)
    return _make_request("/drip", {"image": image})

def clown(image: str) -> str:
    """
    Apply clown makeup filter to an image.
    
    Args:
        image (str): URL of the image
        
    Returns:
        str: URL of the processed image with clown makeup
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> clown_image = clown("https://example.com/face.jpg")
        >>> print(clown_image)
        https://api.popcat.xyz/clown?image=...
    """
    _validate_image_url(image)
    return _make_request("/clown", {"image": image})

def colorify(image: str, color: str) -> str:
    """
    Apply color filter/tint to an image.
    
    Args:
        image (str): URL of the image
        color (str): Color to apply (hex code like #FF0000 or color name like red)
        
    Returns:
        str: URL of the colorized image
        
    Raises:
        ValueError: If image URL or color is invalid
        Exception: If API request fails
        
    Example:
        >>> red_tinted = colorify("https://example.com/image.png", "#FF0000")
        >>> blue_tinted = colorify("https://example.com/image.png", "blue")
        >>> print(red_tinted)
        https://api.popcat.xyz/colorify?image=...&color=%23FF0000
    """
    _validate_image_url(image)
    if not color or not isinstance(color, str):
        raise ValueError("Color must be a non-empty string")
    
    return _make_request("/colorify", {"image": image, "color": color})

def wanted(image: str) -> str:
    """
    Generate a "WANTED" poster with the provided image.
    
    Args:
        image (str): URL of the image for the poster
        
    Returns:
        str: URL of the wanted poster
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> poster = wanted("https://example.com/criminal.jpg")
        >>> print(poster)
        https://api.popcat.xyz/wanted?image=...
    """
    _validate_image_url(image)
    return _make_request("/wanted", {"image": image})

def gun(image: str, text: Optional[str] = None) -> str:
    """
    Generate gun meme with image.
    
    Args:
        image (str): URL of the image
        text (str, optional): Text to add to the meme
        
    Returns:
        str: URL of the generated gun meme
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> gun_meme = gun("https://example.com/person.jpg")
        >>> gun_meme_text = gun("https://example.com/person.jpg", "Always has been")
        >>> print(gun_meme)
        https://api.popcat.xyz/gun?image=...
    """
    _validate_image_url(image)
    params = {"image": image}
    if text:
        params["text"] = text
    return _make_request("/gun", params)

def ad(image: str) -> str:
    """
    Generate advertisement-style meme.
    
    Args:
        image (str): URL of the image
        
    Returns:
        str: URL of the ad meme
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> ad_meme = ad("https://example.com/product.jpg")
        >>> print(ad_meme)
        https://api.popcat.xyz/ad?image=...
    """
    _validate_image_url(image)
    return _make_request("/ad", {"image": image})

def uncover(image: str) -> str:
    """
    Apply uncover filter effect.
    
    Args:
        image (str): URL of the image
        
    Returns:
        str: URL of the processed image
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> uncovered = uncover("https://example.com/hidden.jpg")
        >>> print(uncovered)
        https://api.popcat.xyz/uncover?image=...
    """
    _validate_image_url(image)
    return _make_request("/uncover", {"image": image})

def communism(image_url: str) -> str:
    """
    Apply communism filter with red overlay and symbols.
    
    Args:
        image_url (str): URL of the image
        
    Returns:
        str: URL of the processed image with communism filter
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> communist_image = communism("https://example.com/image.png")
        >>> print(communist_image)
        https://api.popcat.xyz/communism?image=...
    """
    _validate_image_url(image_url)
    return _make_request("/communism", {"image": image_url})

def jokeoverhead(image: str) -> str:
    """
    Generate "joke over head" meme format.
    
    Args:
        image (str): URL of the image
        
    Returns:
        str: URL of the joke over head meme
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> overhead_meme = jokeoverhead("https://example.com/confused.jpg")
        >>> print(overhead_meme)
        https://api.popcat.xyz/jokeoverhead?image=...
    """
    _validate_image_url(image)
    return _make_request("/jokeoverhead", {"image": image})

def mnm(image: str) -> str:
    """
    Generate M&M-style meme with the image.
    
    Args:
        image (str): URL of the image
        
    Returns:
        str: URL of the M&M meme
        
    Raises:
        ValueError: If image URL is invalid
        Exception: If API request fails
        
    Example:
        >>> mnm_meme = mnm("https://example.com/face.jpg")
        >>> print(mnm_meme)
        https://api.popcat.xyz/mnm?image=...
    """
    _validate_image_url(image)
    return _make_request("/mnm", {"image": image})

# Export all functions
__all__ = [
    'jail', 'blur', 'invert', 'greyscale', 'drip', 'clown', 'colorify',
    'wanted', 'gun', 'ad', 'uncover', 'communism', 'jokeoverhead', 'mnm'
]