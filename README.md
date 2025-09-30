# PopcatAPI Wrapper

[![PyPI version](https://badge.fury.io/py/popcatapi-wrapper.svg)](https://badge.fury.io/py/popcatapi-wrapper)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python wrapper for the [Popcat API](https://popcat.xyz/api) providing access to over 60 endpoints including image manipulation, meme generation, data retrieval, text utilities, and more.

## Quick Start

### Installation

```bash
pip install popcatapi-wrapper
```

### Basic Usage

```python
import popcatapi_wrapper as popcat

# Generate a meme
drake_meme = popcat.drake("Using other APIs", "Using Popcat API")
print(drake_meme)  # Returns image URL

# Get weather data  
weather = popcat.weather("London")
print(weather['temperature'])  # Current temperature

# Apply image filter
jail_image = popcat.jail("https://example.com/image.png")
print(jail_image)  # Returns processed image URL

# Get random content
joke = popcat.joke()
fact = popcat.fact()
print(f"Joke: {joke}")
print(f"Fact: {fact}")
```

## Features

- **Image Manipulation**: Apply filters and effects (jail, blur, colorify, etc.)
- **Meme Generation**: Create popular meme formats (Drake, Pooh, Supreme, etc.)
- **Data APIs**: Access real-world data (weather, GitHub, Steam, etc.)
- **Text Utilities**: Transform text (translate, morse code, reverse, etc.)
- **Random Content**: Get jokes, facts, shower thoughts, and more
- **Utilities**: Screenshots, lyrics, chatbot, welcome cards
- **Specialized Classes**: Code paste creation and URL shortening

## Complete Endpoint Reference

### Image Manipulation (14 functions)

Transform and apply effects to images. All functions return image URLs.

```python
# Basic filters
jail_img = popcat.jail("https://example.com/image.png")
blurred = popcat.blur("https://example.com/photo.jpg")
inverted = popcat.invert("https://example.com/image.png")
grey = popcat.greyscale("https://example.com/colorful.jpg")

# Effects
drip_effect = popcat.drip("https://example.com/image.png")
clown_filter = popcat.clown("https://example.com/face.jpg")
communist = popcat.communism("https://example.com/image.png")

# Color manipulation
red_tinted = popcat.colorify("https://example.com/image.png", "#FF0000")
blue_tinted = popcat.colorify("https://example.com/image.png", "blue")

# Meme-style effects
wanted_poster = popcat.wanted("https://example.com/criminal.jpg")
gun_meme = popcat.gun("https://example.com/person.jpg", "Always has been")
ad_style = popcat.ad("https://example.com/product.jpg")
uncover_effect = popcat.uncover("https://example.com/hidden.jpg")
overhead_joke = popcat.jokeoverhead("https://example.com/confused.jpg")
mnm_style = popcat.mnm("https://example.com/face.jpg")
```

**Available Functions:**
- `jail(image_url)` - Apply jail overlay
- `blur(image)` - Blur effect
- `invert(image)` - Invert colors
- `greyscale(image)` - Convert to greyscale
- `drip(image)` - Drip effect
- `clown(image)` - Clown makeup filter
- `colorify(image, color)` - Apply color tint
- `wanted(image)` - Generate wanted poster
- `gun(image, text=None)` - Gun meme format
- `ad(image)` - Advertisement style
- `uncover(image)` - Uncover effect
- `communism(image_url)` - Communist filter
- `jokeoverhead(image)` - Joke over head meme
- `mnm(image)` - M&M style meme

### Meme Generation (18 functions)

Create popular meme formats with custom text and images.

```python
# Comparison memes
drake_meme = popcat.drake("Regular APIs", "Popcat API")
pooh_meme = popcat.pooh("Eating honey", "Consuming apiary nectar")
happy_sad = popcat.happysad("Friday", "Monday")

# Text-based memes
supreme_logo = popcat.supreme("POPCAT")
wisdom = popcat.oogway("There are no accidents")
biden_tweet = popcat.biden("Listen, Jack...")
pikachu_meme = popcat.pikachu("When you realize it's Monday")
sad_cat = popcat.sadcat("No more treats")

# Interactive memes
ship_meme = popcat.ship("https://example.com/person1.jpg", "https://example.com/person2.jpg")
opinion_meme = popcat.opinion("https://example.com/person.jpg", "Pineapple belongs on pizza")

# Quote and message formats
quote_img = popcat.quote("https://example.com/einstein.jpg", 
                        "Imagination is more important than knowledge", 
                        "Albert Einstein")

discord_msg = popcat.discord_message("CoolUser", "Hello everyone!",
                                    avatar="https://example.com/avatar.png",
                                    color="#FF5733")

# Reaction memes
unforgivable_meme = popcat.unforgivable("Using Internet Explorer")
read_meme = popcat.couldread("the documentation")
lulcat_data = popcat.lulcat("I can haz cheezburger?")
facts_meme = popcat.facts("Python is awesome")

# Warning signs
alert_sign = popcat.alert("DANGER: High Voltage")
caution_sign = popcat.caution("Wet Floor")
```

**Available Functions:**
- `drake(text1, text2)` - Drake pointing meme
- `pooh(text1, text2)` - Winnie the Pooh meme
- `ship(image1, image2)` - Ship compatibility
- `supreme(text)` - Supreme logo style
- `oogway(text)` - Master Oogway wisdom
- `biden(text)` - Biden tweet style
- `pikachu(text)` - Surprised Pikachu
- `sadcat(text)` - Sad cat meme
- `opinion(image, text)` - Opinion meme format
- `discord_message(username, content, ...)` - Discord message
- `quote(image, text, name)` - Inspirational quote
- `happysad(text1, text2)` - Happy vs sad
- `unforgivable(text)` - Unforgivable curse
- `couldread(text)` - Could you please read
- `lulcat(text)` - Lulcat/lolcat meme
- `facts(text)` - Facts meme
- `alert(text)` - Warning alert sign
- `caution(text)` - Caution sign

### Data & Information APIs (11 functions)

Access real-world data and information. All functions return dictionaries.

```python
# Weather and location
weather_data = popcat.weather("London")
country_info = popcat.country("Japan")

# Social platforms
github_user = popcat.github("octocat")
subreddit_info = popcat.subreddit("python")

# Development and packages
npm_package = popcat.npm("express")
steam_game = popcat.steam("Portal 2")

# Entertainment
movie_data = popcat.imdb("The Matrix")
song_info = popcat.itunes("Bohemian Rhapsody")

# Science and colors
element_data = popcat.periodic_table("Carbon")
color_info = popcat.colorinfo("#FF0000")
random_color = popcat.randomcolor()
```

**Available Functions:**
- `weather(place)` - Weather information
- `github(username)` - GitHub user data
- `npm(package)` - NPM package details
- `steam(name)` - Steam game search
- `imdb(name)` - Movie/TV show data
- `country(name)` - Country information
- `periodic_table(element)` - Element data
- `colorinfo(color)` - Color information
- `randomcolor()` - Random color generator
- `subreddit(subreddit_name)` - Reddit subreddit data
- `itunes(song)` - iTunes song search

### Text Utilities (7 functions)

Transform and manipulate text in various ways.

```python
# Language and encoding
translated = popcat.translate("Hello world", "es")  # "Hola mundo"
morse_code = popcat.texttomorse("SOS")  # "... --- ..."
binary = popcat.encode("Hi")  # "01001000 01101001"
decoded = popcat.decode("01001000 01101001")  # "Hi"

# Text formatting
reversed_text = popcat.reverse("Hello World")  # "dlroW olleH"
mocked = popcat.mock("This is a test")  # "tHiS iS a TeSt"
double_struck = popcat.doublestruck("Hello")  # "ℍ𝕖𝕝𝕝𝕠"
```

**Available Functions:**
- `translate(text, to)` - Translate to another language
- `reverse(text)` - Reverse character order
- `mock(text)` - Mocking SpongeBob format
- `doublestruck(text)` - Mathematical double-struck
- `texttomorse(text)` - Convert to Morse code
- `encode(text)` - Encode to binary
- `decode(binary)` - Decode from binary

### Random Content (7 functions)

Get random entertainment content for fun and engagement.

```python
# Simple random content
random_joke = popcat.joke()
interesting_fact = popcat.fact()
magic_answer = popcat.eightball()  # or popcat._8ball()

# Complex random data
meme_data = popcat.randommeme()
car_info = popcat.car()
shower_thought = popcat.showerthought()
wyr_question = popcat.wouldyourather()

print(f"Joke: {random_joke}")
print(f"Fact: {interesting_fact}")
print(f"8-Ball says: {magic_answer}")
print(f"Random meme: {meme_data['title']}")
```

**Available Functions:**
- `joke()` - Random joke
- `fact()` - Random fact
- `randommeme()` - Random meme data
- `car()` - Random car information
- `showerthought()` - Random shower thought
- `wouldyourather()` - Would you rather question
- `eightball()` / `_8ball()` - Magic 8-ball response

### Utilities (4 functions)

General-purpose utility functions for various needs.

```python
# Music and lyrics
song_lyrics = popcat.lyrics("Bohemian Rhapsody Queen")
song_lyrics2 = popcat.lyrics("Taylor Swift - Shake It Off")

# Web screenshots
screenshot_url = popcat.screenshot("https://github.com")

# AI chatbot
bot_response = popcat.chatbot("Hello there!", "John", "MyBot")

# Welcome cards for Discord/servers
welcome_img = popcat.welcomecard(
    background="https://example.com/bg.png",
    avatar="https://example.com/avatar.jpg",
    text_1="Welcome",
    text_2="John Doe", 
    text_3="to our awesome server!"
)
```

**Available Functions:**
- `lyrics(song)` - Get song lyrics
- `screenshot(url)` - Website screenshot
- `chatbot(message, ownername, botname)` - AI chatbot
- `welcomecard(background, avatar, text_1, text_2, text_3)` - Welcome card

### Specialized Classes (2 classes)

Advanced services with full-featured class interfaces.

#### CodeClient - Code Paste Creation

```python
# Initialize with API key
client = popcat.CodeClient("your-api-key")

# Create a code paste
paste = client.create_bin(
    title="Hello World",
    description="A simple Python example", 
    code="print('Hello, World!')",
    theme="Monokai",
    language="Python"
)

print(f"Paste URL: {paste['url']}")

# Get available themes and languages
themes = popcat.CodeClient.get_available_themes()
languages = popcat.CodeClient.get_available_languages()

print(f"Available themes: {len(themes)}")
print(f"Supported languages: {len(languages)}")
```

**Available Themes:** GitHub Dark, Monokai, Dracula, VS Code Dark, and 40+ more
**Supported Languages:** Python, JavaScript, Java, C++, TypeScript, and 50+ more

#### Shortener - URL Shortening

```python
# Create shortened URL
short_data = popcat.Shortener.shorten("https://github.com", "gh")
print(f"Short URL: {short_data['short_url']}")  # https://popcat.xyz/gh

# Get URL information
info = popcat.Shortener.get_info("gh")
print(f"Original: {info['original_url']}")
print(f"Clicks: {info['clicks']}")
```

## Installation & Requirements

### Requirements
- Python 3.7+
- requests library

### Installation

```bash
# Install from PyPI
pip install popcatapi-wrapper

# Install from source
git clone https://github.com/example/popcatapi-wrapper.git
cd popcatapi-wrapper
pip install -e .
```

### Optional Dependencies

```bash
# For development
pip install popcatapi-wrapper[dev]

# For testing
pip install popcatapi-wrapper[test]
```

## Usage Examples

### Discord Bot Integration

```python
import discord
import popcatapi_wrapper as popcat

@client.command()
async def meme(ctx, *, text):
    """Generate a random meme with user text"""
    if ' | ' in text:
        text1, text2 = text.split(' | ', 1)
        meme_url = popcat.drake(text1, text2)
    else:
        meme_url = popcat.oogway(text)
    
    embed = discord.Embed()
    embed.set_image(url=meme_url)
    await ctx.send(embed=embed)

@client.command()
async def weather(ctx, *, location):
    """Get weather for a location"""
    weather_data = popcat.weather(location)
    embed = discord.Embed(title=f"Weather in {weather_data['location']}")
    embed.add_field(name="Temperature", value=weather_data['temperature'])
    embed.add_field(name="Condition", value=weather_data['condition'])
    await ctx.send(embed=embed)
```

### Web Application

```python
from flask import Flask, render_template, request
import popcatapi_wrapper as popcat

app = Flask(__name__)

@app.route('/meme-generator', methods=['GET', 'POST'])
def meme_generator():
    if request.method == 'POST':
        meme_type = request.form['type']
        text1 = request.form['text1']
        text2 = request.form.get('text2', '')
        
        if meme_type == 'drake':
            meme_url = popcat.drake(text1, text2)
        elif meme_type == 'supreme':
            meme_url = popcat.supreme(text1)
        
        return render_template('meme_result.html', meme_url=meme_url)
    
    return render_template('meme_form.html')

@app.route('/random-content')
def random_content():
    content = {
        'joke': popcat.joke(),
        'fact': popcat.fact(),
        'color': popcat.randomcolor(),
        'meme': popcat.randommeme()
    }
    return render_template('random.html', content=content)
```

### Data Analysis

```python
import popcatapi_wrapper as popcat
import pandas as pd

# Analyze GitHub users
users = ['octocat', 'torvalds', 'gaearon', 'sindresorhus']
github_data = []

for user in users:
    try:
        data = popcat.github(user)
        github_data.append({
            'username': data['username'],
            'followers': data['followers'],
            'repos': data['public_repos'],
            'language': data.get('most_used_language', 'Unknown')
        })
    except Exception as e:
        print(f"Error fetching {user}: {e}")

df = pd.DataFrame(github_data)
print(df)

# Get weather for multiple cities
cities = ['London', 'New York', 'Tokyo', 'Sydney']
weather_data = []

for city in cities:
    try:
        weather = popcat.weather(city)
        weather_data.append({
            'city': city,
            'temperature': weather['temperature'],
            'condition': weather['condition']
        })
    except Exception as e:
        print(f"Error fetching weather for {city}: {e}")

weather_df = pd.DataFrame(weather_data)
print(weather_df)
```

## Authentication & Rate Limits

### API Keys
- **CodeClient**: Requires an API key for code paste creation
- **Most endpoints**: No authentication required
- **Shortener**: May require authentication for some operations

### Rate Limiting
The Popcat API may have rate limits. For production applications:

```python
import time
import popcatapi_wrapper as popcat

def rate_limited_request(func, *args, delay=1, **kwargs):
    """Make rate-limited API requests"""
    try:
        result = func(*args, **kwargs)
        time.sleep(delay)  # Add delay between requests
        return result
    except Exception as e:
        if "rate limit" in str(e).lower():
            time.sleep(5)  # Wait longer on rate limit
            return func(*args, **kwargs)
        raise e

# Example usage
meme = rate_limited_request(popcat.drake, "Fast requests", "Rate limited requests")
```

## Error Handling

The package includes comprehensive error handling:

```python
import popcatapi_wrapper as popcat

try:
    # Invalid image URL
    result = popcat.jail("not-a-url")
except ValueError as e:
    print(f"Validation error: {e}")

try:
    # API request failure
    result = popcat.weather("NonexistentCity123")
except Exception as e:
    print(f"API error: {e}")

# Graceful error handling
def safe_meme_generation(text1, text2):
    try:
        return popcat.drake(text1, text2)
    except ValueError:
        return None  # Invalid input
    except Exception:
        return popcat.supreme(text1)  # Fallback to different meme
```

## Contributing

We welcome contributions. Please follow these guidelines:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/LandWarderer2772/popcatapi-wrapper.git
cd popcatapi-wrapper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .[dev]

# Run tests
python -m pytest tests/
```

### Adding New Endpoints

1. **Identify the endpoint** on [Popcat API](https://popcat.xyz/api)
2. **Choose the appropriate module** (image, meme, data, text, random, utilities)
3. **Implement the function** with proper validation and documentation
4. **Add tests** for the new function
5. **Update the README** with examples

Example:

```python
def new_endpoint(parameter: str) -> str:
    """
    Description of what this endpoint does.
    
    Args:
        parameter (str): Description of parameter
        
    Returns:
        str: Description of return value
        
    Raises:
        ValueError: If parameter is invalid
        Exception: If API request fails
        
    Example:
        >>> result = new_endpoint("example")
        >>> print(result)
        Expected output
    """
    _validate_text(parameter)
    return _make_request("/new-endpoint", {"param": parameter})
```

### Testing

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_image.py

# Run with coverage
python -m pytest --cov=popcatapi_wrapper

# Run integration tests (requires internet)
python -m pytest tests/integration/
```

### Code Style

We use Black for code formatting and flake8 for linting:

```bash
# Format code
black popcatapi_wrapper/

# Check linting
flake8 popcatapi_wrapper/

# Type checking
mypy popcatapi_wrapper/
```

## Changelog

### v1.0.0 (2023-01-15)
- Initial release
- All 63 Popcat API endpoints implemented
- Comprehensive documentation and examples
- Full test coverage
- CodeClient and Shortener classes

### v0.9.0 (2023-01-10)
- Beta release
- Core functionality implemented
- Basic documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- **PyPI**: https://pypi.org/project/popcatapi-wrapper/
- **GitHub**: https://github.com/LandWarderer2772/popcatapi-wrapper
- **Documentation**: https://popcatapi-wrapper.readthedocs.io/
- **Popcat API**: https://popcat.xyz/api
- **Issues**: https://github.com/LandWarderer2772/popcatapi-wrapper/issues

## Support

If you find this package helpful, consider:
- Starring the repository
- Reporting bugs
- Suggesting new features
- Contributing code
- Sharing with others

## Contact

- **Email**: mh3as81gb@mozmail.com
- **Discord**: land_lmao
- **GitHub**: @LandWarderer2772

---

Developed for the Python community. Professional API wrapper solution.
