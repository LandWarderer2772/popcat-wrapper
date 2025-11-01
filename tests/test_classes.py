"""
Tests for specialized classes (CodeClient and Shortener).
"""

import unittest
from unittest.mock import patch, Mock
from popcat.classes import CodeClient, Shortener

import pytest
import responses


class TestCodeClient:
    """Test cases for CodeClient class."""
    
    def test_init_valid_key(self):
        """Test CodeClient initialization with valid API key."""
        client = CodeClient("test-api-key")
        assert client.api_key == "test-api-key"
    
    def test_init_invalid_key(self):
        """Test CodeClient initialization with invalid API key."""
        with pytest.raises(ValueError, match="API key must be a non-empty string"):
            CodeClient("")
        
        with pytest.raises(ValueError, match="API key must be a non-empty string"):
            CodeClient(None)
    
    @responses.activate
    def test_create_bin_basic(self):
        """Test basic bin creation."""
        client = CodeClient("test-key")
        mock_response = {
            "url": "https://code.popcat.xyz/ABC123",
            "id": "ABC123",
            "title": "Test Code",
            "theme": "GitHub Dark",
            "language": "PlainText"
        }
        
        responses.add(
            responses.POST,
            "https://api.popcat.xyz/code",
            json=mock_response,
            status=200
        )
        
        result = client.create_bin(
            "Test Code",
            "A test paste",
            "print('hello')",
            theme="GitHub Dark",
            language="Python"
        )
        
        assert isinstance(result, dict)
        assert "url" in result
    
    def test_create_bin_invalid_theme(self):
        """Test bin creation with invalid theme."""
        client = CodeClient("test-key")
        
        with pytest.raises(ValueError, match="Theme must be one of"):
            client.create_bin(
                "Test",
                "Description", 
                "code",
                theme="InvalidTheme"
            )
    
    def test_create_bin_invalid_language(self):
        """Test bin creation with invalid language."""
        client = CodeClient("test-key")
        
        with pytest.raises(ValueError, match="Language must be one of"):
            client.create_bin(
                "Test",
                "Description",
                "code", 
                language="InvalidLanguage"
            )
    
    def test_create_bin_empty_parameters(self):
        """Test bin creation with empty parameters."""
        client = CodeClient("test-key")
        
        with pytest.raises(ValueError, match="Title must be a non-empty string"):
            client.create_bin("", "description", "code")
        
        with pytest.raises(ValueError, match="Description must be a non-empty string"):
            client.create_bin("title", "", "code")
        
        with pytest.raises(ValueError, match="Code must be a non-empty string"):
            client.create_bin("title", "description", "")
    
    def test_get_available_themes(self):
        """Test getting available themes."""
        themes = CodeClient.get_available_themes()
        assert isinstance(themes, list)
        assert len(themes) > 0
        assert "GitHub Dark" in themes
        assert "Monokai" in themes
    
    def test_get_available_languages(self):
        """Test getting available languages."""
        languages = CodeClient.get_available_languages()
        assert isinstance(languages, list)
        assert len(languages) > 0
        assert "Python" in languages
        assert "JavaScript" in languages


class TestShortener:
    """Test cases for Shortener class."""
    
    @responses.activate
    def test_shorten_url(self):
        """Test URL shortening."""
        mock_response = {
            "short_url": "https://popcat.xyz/example",
            "original_url": "https://example.com",
            "extension": "example"
        }
        
        responses.add(
            responses.POST,
            "https://api.popcat.xyz/shorten",
            json=mock_response,
            status=200
        )
        
        result = Shortener.shorten("https://example.com", "example")
        assert isinstance(result, dict)
        assert "short_url" in result
    
    def test_shorten_invalid_url(self):
        """Test shortening with invalid URL."""
        with pytest.raises(ValueError, match="URL must start with http"):
            Shortener.shorten("not-a-url", "test")
        
        with pytest.raises(ValueError, match="URL must be a non-empty string"):
            Shortener.shorten("", "test")
    
    def test_shorten_invalid_extension(self):
        """Test shortening with invalid extension."""
        url = "https://example.com"
        
        with pytest.raises(ValueError, match="Extension must be a non-empty string"):
            Shortener.shorten(url, "")
        
        with pytest.raises(ValueError, match="Extension must contain only alphanumeric"):
            Shortener.shorten(url, "test-123")
        
        with pytest.raises(ValueError, match="Extension must be between 3 and 20 characters"):
            Shortener.shorten(url, "ab")  # Too short
        
        with pytest.raises(ValueError, match="Extension must be between 3 and 20 characters"):
            Shortener.shorten(url, "x" * 21)  # Too long
    
    @responses.activate
    def test_get_info_existing(self):
        """Test getting info for existing shortened URL."""
        mock_response = {
            "extension": "example",
            "original_url": "https://example.com",
            "clicks": 42
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/shorten/example",
            json=mock_response,
            status=200
        )
        
        result = Shortener.get_info("example")
        assert isinstance(result, dict)
        assert "extension" in result
    
    @responses.activate
    def test_get_info_not_found(self):
        """Test getting info for non-existent shortened URL."""
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/shorten/notfound",
            status=404
        )
        
        with pytest.raises(Exception, match="not found"):
            Shortener.get_info("notfound")
    
    def test_get_info_invalid_extension(self):
        """Test getting info with invalid extension."""
        with pytest.raises(ValueError, match="Extension must be a non-empty string"):
            Shortener.get_info("")
        
        with pytest.raises(ValueError, match="Extension must contain only alphanumeric"):
            Shortener.get_info("test-123")


if __name__ == "__main__":
    pytest.main([__file__])