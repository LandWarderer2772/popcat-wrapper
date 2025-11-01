# Quick Start Guide

## Installation

Install the package using pip:

```bash
pip install popcat.py
```

## Basic Usage

Import the package and start using the API:

```python
import popcat

# Your first meme
meme_url = popcat.drake("Regular APIs", "Popcat API")
print(f"Meme created: {meme_url}")
```

## Common Use Cases

### Image Manipulation

```python
# Apply filters to images
jail_image = popcat.jail("https://example.com/image.png")
blurred = popcat.blur("https://example.com/photo.jpg")
colorized = popcat.colorify("https://example.com/image.png", "#FF0000")
```

### Meme Generation

```python
# Create popular meme formats
drake_meme = popcat.drake("Old way", "New way")
supreme_logo = popcat.supreme("POPCAT")
quote_img = popcat.quote("https://example.com/person.jpg", "Hello World!", "Developer")
```

### Data Retrieval

```python
# Get real-world data
weather = popcat.weather("London")
github_user = popcat.github("octocat")
color_info = popcat.colorinfo("#FF0000")
```

### Text Utilities

```python
# Transform text
translated = popcat.translate("Hello", "es")
morse_code = popcat.texttomorse("SOS")
mocked = popcat.mock("This is a test")
```

### Random Content

```python
# Get random entertainment
joke = popcat.joke()
fact = popcat.fact()
meme_data = popcat.randommeme()
```

## Error Handling

The package includes comprehensive error handling:

```python
try:
    result = popcat.weather("InvalidCity")
except ValueError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"API error: {e}")
```

## Next Steps

- Check out the {doc}`api_reference` for complete function documentation
- See {doc}`examples` for detailed usage scenarios
- Read about {doc}`contributing` to help improve the package