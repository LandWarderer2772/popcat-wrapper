"""
Specialized Classes Module

This module provides specialized service classes for advanced Popcat API functionality.
Contains CodeClient for code paste creation and Shortener for URL shortening.

Available Classes:
    - CodeClient: Create and manage syntax-highlighted code pastes on https://code.popcat.xyz
    - Shortener: URL shortening service with custom extensions
"""

import requests
from typing import Dict, Any, Optional, List

# Base URL for the Popcat API
BASE_URL = "https://api.popcat.xyz"

class CodeClient:
    """
    A client for creating and managing code pastes on https://code.popcat.xyz.
    
    This class provides functionality to create syntax-highlighted code pastes
    with various themes and language support.
    
    Attributes:
        api_key (str): API key for authentication
        
    Example:
        >>> client = CodeClient("your-api-key")
        >>> paste = client.create_bin("Test Code", "A simple example", "print('Hello, World!')", 
        ...                          theme="GitHub Dark", language="Python")
        >>> print(paste['url'])
        https://code.popcat.xyz/ABC123
    """
    
    # Available syntax highlighting themes
    THEMES = [
        "Active4D", "All Hallows Eve", "Amy", "Birds of Paradise", "Blackboard",
        "Brilliance Black", "Brilliance Dull", "Chrome DevTools", "Clouds Midnight",
        "Clouds", "Cobalt", "Cobalt2", "Dawn", "Dominion Day", "Dracula", "Dreamweaver",
        "Eiffel", "Espresso Libre", "GitHub Dark", "GitHub Light", "GitHub", "IDLE",
        "idleFingers", "iPlastic", "Katzenmilch", "krTheme", "Kuroir Theme", "LAZY",
        "Merbivore Soft", "Merbivore", "monoindustrial", "Monokai Bright", "Monokai",
        "Night Owl", "Nord", "Oceanic Next", "Pastels on Dark", "Slush and Poppies",
        "SpaceCadet", "Sunburst", "Tomorrow", "Twilight", "Upstream Sunburst",
        "Vibrant Ink", "Xcode_default", "Zenburnesque"
    ]
    
    # Supported programming languages
    LANGUAGES = [
        "JavaScript", "JSON", "HTML", "CSS", "Markdown", "PlainText", "Python",
        "Java", "C++", "C", "C#", "TypeScript", "PHP", "Ruby", "Go", "Rust",
        "Swift", "Kotlin", "Dart", "Scala", "R", "MATLAB", "SQL", "Shell",
        "PowerShell", "Bash", "Perl", "Lua", "Haskell", "Erlang", "Elixir",
        "F#", "OCaml", "Clojure", "Lisp", "Scheme", "Prolog", "VHDL", "Verilog",
        "Assembly", "Fortran", "COBOL", "Ada", "Pascal", "Delphi", "VB.NET",
        "VBA", "ActionScript", "CoffeeScript", "LiveScript", "PureScript",
        "Elm", "ReasonML", "Crystal", "Nim", "Zig", "V", "Dlang"
    ]
    
    def __init__(self, api_key: str):
        """
        Initialize the CodeClient with an API key.
        
        Args:
            api_key (str): API key for authentication
            
        Raises:
            ValueError: If api_key is invalid
        """
        if not api_key or not isinstance(api_key, str):
            raise ValueError("API key must be a non-empty string")
        self.api_key = api_key
    
    def create_bin(self, title: str, description: str, code: str, 
                   theme: str = "GitHub Dark", language: str = "PlainText") -> Dict[str, Any]:
        """
        Create a new code paste.
        
        Args:
            title (str): Title of the code paste
            description (str): Description of the paste
            code (str): The actual code content
            theme (str, optional): Syntax highlighting theme. Defaults to "GitHub Dark"
            language (str, optional): Programming language. Defaults to "PlainText"
            
        Returns:
            Dict[str, Any]: Paste URL and metadata
            
        Raises:
            ValueError: If any parameter is invalid
            Exception: If API request fails
            
        Example:
            >>> client = CodeClient("your-api-key")
            >>> paste = client.create_bin(
            ...     "Hello World", 
            ...     "A simple Python example",
            ...     "print('Hello, World!')",
            ...     theme="Monokai",
            ...     language="Python"
            ... )
            >>> print(paste)
            {
                'url': 'https://code.popcat.xyz/ABC123',
                'id': 'ABC123',
                'title': 'Hello World',
                'description': 'A simple Python example',
                'theme': 'Monokai',
                'language': 'Python',
                'created_at': '2023-01-15T10:30:00Z',
                ...
            }
        """
        # Validate parameters
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")
        if not description or not isinstance(description, str):
            raise ValueError("Description must be a non-empty string")
        if not code or not isinstance(code, str):
            raise ValueError("Code must be a non-empty string")
        
        # Validate theme
        if theme not in self.THEMES:
            raise ValueError(f"Theme must be one of: {', '.join(self.THEMES)}")
        
        # Validate language (case-insensitive)
        language_normalized = None
        for lang in self.LANGUAGES:
            if lang.lower() == language.lower():
                language_normalized = lang
                break
        
        if language_normalized is None:
            raise ValueError(f"Language must be one of: {', '.join(self.LANGUAGES)}")
        
        # Make API request
        try:
            response = requests.post(f"{BASE_URL}/code", json={
                "title": title,
                "description": description,
                "code": code,
                "theme": theme,
                "language": language_normalized
            }, headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            })
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    @classmethod
    def get_available_themes(cls) -> List[str]:
        """
        Get list of available syntax highlighting themes.
        
        Returns:
            List[str]: List of available theme names
            
        Example:
            >>> themes = CodeClient.get_available_themes()
            >>> print(themes[:5])
            ['Active4D', 'All Hallows Eve', 'Amy', 'Birds of Paradise', 'Blackboard']
        """
        return cls.THEMES.copy()
    
    @classmethod
    def get_available_languages(cls) -> List[str]:
        """
        Get list of supported programming languages.
        
        Returns:
            List[str]: List of supported language names
            
        Example:
            >>> languages = CodeClient.get_available_languages()
            >>> print(languages[:5])
            ['JavaScript', 'JSON', 'HTML', 'CSS', 'Markdown']
        """
        return cls.LANGUAGES.copy()


class Shortener:
    """
    A static class for URL shortening services.
    
    This class provides functionality to create shortened URLs with custom extensions
    and retrieve information about existing shortened URLs.
    
    Example:
        >>> short_data = Shortener.shorten("https://github.com", "gh")
        >>> print(short_data['short_url'])
        https://popcat.xyz/gh
        
        >>> info = Shortener.get_info("gh")
        >>> print(info['original_url'])
        https://github.com
    """
    
    @staticmethod
    def shorten(url: str, extension: str) -> Dict[str, Any]:
        """
        Create a shortened URL with custom extension.
        
        Args:
            url (str): Full URL to shorten
            extension (str): Custom short extension (alphanumeric, 3-20 characters)
            
        Returns:
            Dict[str, Any]: Shortened URL and metadata
            
        Raises:
            ValueError: If parameters are invalid
            Exception: If API request fails
            
        Example:
            >>> short_data = Shortener.shorten("https://example.com", "example")
            >>> print(short_data)
            {
                'short_url': 'https://popcat.xyz/example',
                'original_url': 'https://example.com',
                'extension': 'example',
                'created_at': '2023-01-15T10:30:00Z',
                'clicks': 0,
                ...
            }
        """
        # Validate URL
        if not url or not isinstance(url, str):
            raise ValueError("URL must be a non-empty string")
        if not (url.startswith('http://') or url.startswith('https://')):
            raise ValueError("URL must start with http:// or https://")
        
        # Validate extension
        if not extension or not isinstance(extension, str):
            raise ValueError("Extension must be a non-empty string")
        if not extension.isalnum():
            raise ValueError("Extension must contain only alphanumeric characters")
        if not (3 <= len(extension) <= 20):
            raise ValueError("Extension must be between 3 and 20 characters")
        
        # Make API request
        try:
            response = requests.post(f"{BASE_URL}/shorten", json={
                "url": url,
                "extension": extension
            }, headers={
                "Content-Type": "application/json"
            })
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    @staticmethod
    def get_info(extension: str) -> Dict[str, Any]:
        """
        Get details about an existing shortened URL.
        
        Args:
            extension (str): Short URL extension
            
        Returns:
            Dict[str, Any]: Information about the shortened URL
            
        Raises:
            ValueError: If extension is invalid
            Exception: If API request fails or URL not found
            
        Example:
            >>> info = Shortener.get_info("example")
            >>> print(info)
            {
                'extension': 'example',
                'original_url': 'https://example.com',
                'short_url': 'https://popcat.xyz/example',
                'created_at': '2023-01-15T10:30:00Z',
                'clicks': 42,
                'last_accessed': '2023-01-20T15:45:00Z',
                ...
            }
        """
        # Validate extension
        if not extension or not isinstance(extension, str):
            raise ValueError("Extension must be a non-empty string")
        if not extension.isalnum():
            raise ValueError("Extension must contain only alphanumeric characters")
        
        # Make API request
        try:
            response = requests.get(f"{BASE_URL}/shorten/{extension}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            if hasattr(e.response, 'status_code') and e.response.status_code == 404:
                raise Exception(f"Shortened URL with extension '{extension}' not found")
            raise Exception(f"API request failed: {str(e)}")

# Export all classes
__all__ = ['CodeClient', 'Shortener']