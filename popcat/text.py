"""
Text Utilities Module

This module provides functions for manipulating and transforming text.
All functions return processed strings.

Available Functions:
    - translate(text, to): Translate text to another language
    - reverse(text): Reverse the order of characters in text
    - mock(text): Convert text to mocking SpongeBob format
    - doublestruck(text): Convert text to mathematical double-struck format
    - texttomorse(text): Convert text to Morse code
    - encode(text): Encode text to binary format
    - decode(binary): Decode binary to readable text
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

def _make_request(endpoint: str, params: dict) -> str:
    """Make a request to the API and return the text result."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        
        # Try to parse as JSON first, then fall back to text
        try:
            data = response.json()
            # Different endpoints return data in different formats
            if 'translated' in data:
                return data['translated']
            elif 'text' in data:
                return data['text']
            elif 'morse' in data:
                return data['morse']
            elif 'binary' in data:
                return data['binary']
            elif 'decoded' in data:
                return data['decoded']
            else:
                # If we have a simple response, return the first string value
                for value in data.values():
                    if isinstance(value, str):
                        return value
                return str(data)
        except ValueError:
            # If not JSON, return as text
            return response.text
            
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def translate(text: str, to: str) -> str:
    """
    Translate text to another language.
    
    Args:
        text (str): Text to translate
        to (str): Target language code (e.g., "es", "fr", "de", "ja", "zh")
        
    Returns:
        str: Translated text
        
    Raises:
        ValueError: If text or language code is invalid
        Exception: If API request fails
        
    Example:
        >>> translated = translate("Hello world", "es")
        >>> print(translated)
        Hola mundo
        
        >>> translated = translate("Good morning", "fr")
        >>> print(translated)
        Bonjour
    """
    _validate_text(text)
    _validate_text(to)
    
    return _make_request("/translate", {"text": text, "to": to})

def reverse(text: str) -> str:
    """
    Reverse the order of characters in text.
    
    Args:
        text (str): Text to reverse
        
    Returns:
        str: Reversed text
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> reversed_text = reverse("Hello World")
        >>> print(reversed_text)
        dlroW olleH
        
        >>> reversed_text = reverse("Python")
        >>> print(reversed_text)
        nohtyP
    """
    _validate_text(text)
    return _make_request("/reverse", {"text": text})

def mock(text: str) -> str:
    """
    Convert text to mocking SpongeBob format (aLtErNaTiNg CaPiTaLs).
    
    Args:
        text (str): Text to mock
        
    Returns:
        str: Mocking text with alternating capitals
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> mocked = mock("This is a test")
        >>> print(mocked)
        tHiS iS a TeSt
        
        >>> mocked = mock("Python is awesome")
        >>> print(mocked)
        pYtHoN iS aWeSoMe
    """
    _validate_text(text)
    return _make_request("/mock", {"text": text})

def doublestruck(text: str) -> str:
    """
    Convert text to mathematical double-struck format.
    
    Args:
        text (str): Text to convert
        
    Returns:
        str: Double-struck text using Unicode mathematical characters
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> ds_text = doublestruck("Hello")
        >>> print(ds_text)
        ℍ𝕖𝕝𝕝𝕠
        
        >>> ds_text = doublestruck("Python")
        >>> print(ds_text)
        ℙ𝕪𝕥𝕙𝕠𝕟
    """
    _validate_text(text)
    return _make_request("/doublestruck", {"text": text})

def texttomorse(text: str) -> str:
    """
    Convert text to Morse code.
    
    Args:
        text (str): Text to convert to Morse code
        
    Returns:
        str: Morse code representation using dots and dashes
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> morse = texttomorse("SOS")
        >>> print(morse)
        ... --- ...
        
        >>> morse = texttomorse("Hello")
        >>> print(morse)
        .... . .-.. .-.. ---
    """
    _validate_text(text)
    return _make_request("/texttomorse", {"text": text})

def encode(text: str) -> str:
    """
    Encode text to binary format.
    
    Args:
        text (str): Text to encode
        
    Returns:
        str: Binary representation of the text
        
    Raises:
        ValueError: If text is invalid
        Exception: If API request fails
        
    Example:
        >>> binary = encode("Hi")
        >>> print(binary)
        01001000 01101001
        
        >>> binary = encode("A")
        >>> print(binary)
        01000001
    """
    _validate_text(text)
    return _make_request("/encode", {"text": text})

def decode(binary: str) -> str:
    """
    Decode binary to readable text.
    
    Args:
        binary (str): Binary string to decode (space-separated 8-bit chunks)
        
    Returns:
        str: Decoded text
        
    Raises:
        ValueError: If binary string is invalid
        Exception: If API request fails
        
    Example:
        >>> decoded = decode("01001000 01101001")
        >>> print(decoded)
        Hi
        
        >>> decoded = decode("01000001")
        >>> print(decoded)
        A
    """
    _validate_text(binary)
    # Basic validation for binary format
    binary_clean = binary.replace(' ', '')
    if not all(c in '01' for c in binary_clean):
        raise ValueError("Binary string must contain only 0s and 1s")
    
    return _make_request("/decode", {"binary": binary})

# Export all functions
__all__ = [
    'translate', 'reverse', 'mock', 'doublestruck', 
    'texttomorse', 'encode', 'decode'
]