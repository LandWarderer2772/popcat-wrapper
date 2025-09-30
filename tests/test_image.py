"""
Test cases for image manipulation functions.
"""

import pytest
import responses
from popcat_wrapper import image


class TestImageManipulation:
    """Test cases for image manipulation functions."""
    
    @responses.activate
    def test_jail_valid_url(self):
        """Test jail function with valid image URL."""
        test_url = "https://example.com/image.png"
        expected_response_url = "https://api.popcat.xyz/jail?image=https%3A//example.com/image.png"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/jail",
            status=200
        )
        
        result = image.jail(test_url)
        assert isinstance(result, str)
        assert "api.popcat.xyz" in result
    
    def test_jail_invalid_url(self):
        """Test jail function with invalid URL."""
        with pytest.raises(ValueError, match="Image URL must start with http"):
            image.jail("not-a-url")
        
        with pytest.raises(ValueError, match="Image URL must be a non-empty string"):
            image.jail("")
    
    @responses.activate
    def test_blur_function(self):
        """Test blur function."""
        test_url = "https://example.com/photo.jpg"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/blur",
            status=200
        )
        
        result = image.blur(test_url)
        assert isinstance(result, str)
    
    @responses.activate
    def test_colorify_with_hex(self):
        """Test colorify function with hex color."""
        test_url = "https://example.com/image.png"
        test_color = "#FF0000"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/colorify",
            status=200
        )
        
        result = image.colorify(test_url, test_color)
        assert isinstance(result, str)
    
    def test_colorify_invalid_color(self):
        """Test colorify function with invalid color."""
        test_url = "https://example.com/image.png"
        
        with pytest.raises(ValueError, match="Color must be a non-empty string"):
            image.colorify(test_url, "")
    
    @responses.activate
    def test_gun_with_text(self):
        """Test gun function with optional text."""
        test_url = "https://example.com/person.jpg"
        test_text = "Always has been"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/gun",
            status=200
        )
        
        result = image.gun(test_url, test_text)
        assert isinstance(result, str)
    
    @responses.activate
    def test_gun_without_text(self):
        """Test gun function without optional text."""
        test_url = "https://example.com/person.jpg"
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/gun",
            status=200
        )
        
        result = image.gun(test_url)
        assert isinstance(result, str)


if __name__ == "__main__":
    pytest.main([__file__])