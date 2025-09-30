"""
Random Content Module

This module provides functions for generating random entertainment content.
Functions return various types including strings and dictionaries.

Available Functions:
    - joke(): Get a random joke
    - fact(): Get a random interesting fact
    - randommeme(): Get a random meme from the internet
    - car(): Get information about a random car
    - showerthought(): Get a random shower thought from Reddit
    - wouldyourather(): Get a random "would you rather" question
    - eightball(): Get a magic 8-ball response
    - _8ball(): Alias for eightball() with alternative name
"""

import requests
from typing import Dict, Any, Union

# Base URL for the Popcat API
BASE_URL = "https://api.popcat.xyz"

def _make_request(endpoint: str) -> Union[str, Dict[str, Any]]:
    """Make a request to the API and return the result."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        
        # Try to parse as JSON first
        try:
            data = response.json()
            
            # For simple string responses, extract the main content
            if 'joke' in data and len(data) == 1:
                return data['joke']
            elif 'fact' in data and len(data) == 1:
                return data['fact']
            elif 'answer' in data and len(data) == 1:
                return data['answer']
            else:
                # Return full data for complex responses
                return data
                
        except ValueError:
            # If not JSON, return as text
            return response.text
            
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def joke() -> str:
    """
    Get a random joke.
    
    Returns:
        str: Random joke text
        
    Raises:
        Exception: If API request fails
        
    Example:
        >>> random_joke = joke()
        >>> print(random_joke)
        Why don't scientists trust atoms? Because they make up everything!
        
        >>> another_joke = joke()
        >>> print(another_joke)
        What do you call a fake noodle? An impasta!
    """
    return _make_request("/joke")

def fact() -> str:
    """
    Get a random interesting fact.
    
    Returns:
        str: Random fact text
        
    Raises:
        Exception: If API request fails
        
    Example:
        >>> random_fact = fact()
        >>> print(random_fact)
        Octopuses have three hearts and blue blood.
        
        >>> another_fact = fact()
        >>> print(another_fact)
        Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs.
    """
    return _make_request("/fact")

def randommeme() -> Dict[str, Any]:
    """
    Get a random meme from the internet.
    
    Returns:
        Dict[str, Any]: Random meme with image URL, title, and metadata
        
    Raises:
        Exception: If API request fails
        
    Example:
        >>> meme_data = randommeme()
        >>> print(meme_data)
        {
            'title': 'When you finally understand recursion',
            'image': 'https://i.redd.it/...',
            'author': 'u/programmer123',
            'subreddit': 'r/ProgrammerHumor',
            'ups': 5420,
            'awards': 3,
            ...
        }
    """
    return _make_request("/randommeme")

def car() -> Dict[str, Any]:
    """
    Get information about a random car.
    
    Returns:
        Dict[str, Any]: Random car information including make, model, year, specs
        
    Raises:
        Exception: If API request fails
        
    Example:
        >>> car_info = car()
        >>> print(car_info)
        {
            'make': 'Toyota',
            'model': 'Camry',
            'year': '2022',
            'type': 'Sedan',
            'fuel_type': 'Gasoline',
            'engine': '2.5L 4-Cylinder',
            'horsepower': '203 hp',
            'price': '$25,000',
            ...
        }
    """
    return _make_request("/car")

def showerthought() -> Dict[str, Any]:
    """
    Get a random shower thought from Reddit.
    
    Returns:
        Dict[str, Any]: Random shower thought with text and metadata
        
    Raises:
        Exception: If API request fails
        
    Example:
        >>> thought = showerthought()
        >>> print(thought)
        {
            'thought': 'The person who would proof read Hitler\'s speeches was literally a grammar Nazi.',
            'author': 'u/deepthoughts',
            'ups': 15420,
            'awards': 5,
            'date': '2023-01-15',
            ...
        }
    """
    return _make_request("/showerthought")

def wouldyourather() -> Dict[str, Any]:
    """
    Get a random "would you rather" question.
    
    Returns:
        Dict[str, Any]: Would you rather question with two options
        
    Raises:
        Exception: If API request fails
        
    Example:
        >>> wyr = wouldyourather()
        >>> print(wyr)
        {
            'question': 'Would you rather have the ability to fly or be invisible?',
            'option1': 'Have the ability to fly',
            'option2': 'Be invisible',
            'votes1': 60,
            'votes2': 40,
            ...
        }
    """
    return _make_request("/wouldyourather")

def eightball() -> str:
    """
    Get a magic 8-ball response.
    
    Returns:
        str: Magic 8-ball answer
        
    Raises:
        Exception: If API request fails
        
    Example:
        >>> answer = eightball()
        >>> print(answer)
        It is certain.
        
        >>> answer = eightball()
        >>> print(answer)
        Ask again later.
    """
    return _make_request("/8ball")

def _8ball() -> str:
    """
    Get a magic 8-ball response (alternative name).
    
    This is an alias for eightball() with an alternative naming convention
    that starts with an underscore to make it a valid Python identifier.
    
    Returns:
        str: Magic 8-ball answer
        
    Raises:
        Exception: If API request fails
        
    Example:
        >>> answer = _8ball()
        >>> print(answer)
        Signs point to yes.
        
        >>> answer = _8ball()
        >>> print(answer)
        Don't count on it.
    """
    return eightball()

# Export all functions
__all__ = [
    'joke', 'fact', 'randommeme', 'car', 'showerthought', 
    'wouldyourather', 'eightball', '_8ball'
]