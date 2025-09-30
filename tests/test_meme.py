"""
Test cases for meme generation functions.
"""

import pytest
import responses
from popcat_wrapper import meme


class TestMemeGeneration:
    """Test cases for meme generation functions."""
    
    @responses.activate
    def test_drake_meme(self):
        """Test drake meme generation."""
        text1 = "Regular APIs"
        text2 = "Popcat API"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/drake",
            status=200
        )
        
        result = meme.drake(text1, text2)
        assert isinstance(result, str)
    
    def test_drake_invalid_text(self):
        """Test drake function with invalid text."""
        with pytest.raises(ValueError, match="Text must be a non-empty string"):
            meme.drake("", "valid text")
        
        with pytest.raises(ValueError, match="Text must be a non-empty string"):
            meme.drake("valid text", "")
    
    @responses.activate
    def test_supreme_logo(self):
        """Test supreme logo generation."""
        test_text = "POPCAT"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/supreme",
            status=200
        )
        
        result = meme.supreme(test_text)
        assert isinstance(result, str)
    
    @responses.activate
    def test_ship_compatibility(self):
        """Test ship compatibility meme."""
        image1 = "https://example.com/person1.jpg"
        image2 = "https://example.com/person2.jpg"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/ship",
            status=200
        )
        
        result = meme.ship(image1, image2)
        assert isinstance(result, str)
    
    def test_ship_invalid_images(self):
        """Test ship function with invalid image URLs."""
        with pytest.raises(ValueError, match="Image URL must start with http"):
            meme.ship("not-a-url", "https://example.com/image.jpg")
    
    @responses.activate
    def test_quote_generation(self):
        """Test quote image generation."""
        image_url = "https://example.com/einstein.jpg"
        text = "Imagination is more important than knowledge"
        name = "Albert Einstein"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/quote",
            status=200
        )
        
        result = meme.quote(image_url, text, name)
        assert isinstance(result, str)
    
    def test_quote_text_too_long(self):
        """Test quote function with text that's too long."""
        image_url = "https://example.com/image.jpg"
        long_text = "x" * 126  # Exceeds 125 character limit
        name = "Test Name"
        
        with pytest.raises(ValueError, match="Text must be 125 characters or less"):
            meme.quote(image_url, long_text, name)
    
    @responses.activate
    def test_discord_message_minimal(self):
        """Test discord message with minimal parameters."""
        username = "TestUser"
        content = "Hello world!"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/discord",
            status=200
        )
        
        result = meme.discord_message(username, content)
        assert isinstance(result, str)
    
    @responses.activate
    def test_discord_message_full(self):
        """Test discord message with all parameters."""
        username = "TestUser"
        content = "Hello world!"
        avatar = "https://example.com/avatar.png"
        color = "#FF5733"
        timestamp = "2023-01-15T10:30:00Z"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/discord",
            status=200
        )
        
        result = meme.discord_message(username, content, avatar, color, timestamp)
        assert isinstance(result, str)
    
    @responses.activate 
    def test_lulcat_returns_dict(self):
        """Test lulcat function returns dictionary."""
        test_text = "I can haz cheezburger?"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/lulcat",
            json={"url": "https://example.com/lulcat.png"},
            status=200
        )
        
        result = meme.lulcat(test_text)
        assert isinstance(result, dict)


if __name__ == "__main__":
    pytest.main([__file__])