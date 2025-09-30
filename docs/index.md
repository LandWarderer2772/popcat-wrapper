# PopcatAPI Wrapper Documentation

Welcome to the **PopcatAPI Wrapper** documentation! This is a comprehensive Python wrapper for the [Popcat API](https://popcat.xyz/api) providing access to over 60 endpoints.

```{toctree}
:maxdepth: 2
:caption: Contents:

quickstart
api_reference
examples
contributing
changelog
```

## Features

- 🎨 **Image Manipulation**: Apply filters and effects (jail, blur, colorify, etc.)
- 😂 **Meme Generation**: Create popular meme formats (Drake, Pooh, Supreme, etc.)
- 📊 **Data APIs**: Access real-world data (weather, GitHub, Steam, etc.)
- 🔤 **Text Utilities**: Transform text (translate, morse code, reverse, etc.)
- 🎲 **Random Content**: Get jokes, facts, shower thoughts, and more
- 🛠️ **Utilities**: Screenshots, lyrics, chatbot, welcome cards
- 🏗️ **Specialized Classes**: Code paste creation and URL shortening

## Quick Example

```python
import popcatapi_wrapper as popcat

# Generate a meme
drake_meme = popcat.drake("Using other APIs", "Using Popcat API")

# Get weather data
weather = popcat.weather("London")

# Apply image filter
jail_image = popcat.jail("https://example.com/image.png")
```

## Installation

```bash
pip install popcatapi-wrapper
```

## Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`