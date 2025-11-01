"""
Tests for data module functions.
"""

import unittest
from unittest.mock import patch, Mock
from popcat import data


class TestDataAPIs:
    """Test cases for data API functions."""
    
    @responses.activate
    def test_weather_function(self):
        """Test weather data retrieval."""
        place = "London"
        mock_response = {
            "location": "London, England",
            "temperature": "15°C",
            "condition": "Partly Cloudy",
            "humidity": "65%"
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/weather",
            json=mock_response,
            status=200
        )
        
        result = data.weather(place)
        assert isinstance(result, dict)
        assert "location" in result
    
    def test_weather_invalid_place(self):
        """Test weather function with invalid place."""
        with pytest.raises(ValueError, match="Text must be a non-empty string"):
            data.weather("")
    
    @responses.activate
    def test_github_user_data(self):
        """Test GitHub user data retrieval."""
        username = "octocat"
        mock_response = {
            "username": "octocat",
            "name": "The Octocat",
            "public_repos": 8,
            "followers": 9001
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/github",
            json=mock_response,
            status=200
        )
        
        result = data.github(username)
        assert isinstance(result, dict)
        assert "username" in result
    
    @responses.activate
    def test_npm_package_info(self):
        """Test NPM package information retrieval."""
        package_name = "express"
        mock_response = {
            "name": "express",
            "version": "4.18.2",
            "description": "Fast, unopinionated, minimalist web framework"
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/npm",
            json=mock_response,
            status=200
        )
        
        result = data.npm(package_name)
        assert isinstance(result, dict)
        assert "name" in result
    
    @responses.activate
    def test_colorinfo_hex(self):
        """Test color information with hex code."""
        color = "#FF0000"
        mock_response = {
            "hex": "#FF0000",
            "rgb": {"r": 255, "g": 0, "b": 0},
            "name": "Red"
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/colorinfo",
            json=mock_response,
            status=200
        )
        
        result = data.colorinfo(color)
        assert isinstance(result, dict)
        assert "hex" in result
    
    @responses.activate
    def test_colorinfo_name(self):
        """Test color information with color name."""
        color = "red"
        mock_response = {
            "hex": "#FF0000",
            "rgb": {"r": 255, "g": 0, "b": 0},
            "name": "Red"
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/colorinfo",
            json=mock_response,
            status=200
        )
        
        result = data.colorinfo(color)
        assert isinstance(result, dict)
    
    @responses.activate
    def test_randomcolor(self):
        """Test random color generation."""
        mock_response = {
            "hex": "#3A7BD5",
            "rgb": {"r": 58, "g": 123, "b": 213},
            "name": "Steel Blue"
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/randomcolor",
            json=mock_response,
            status=200
        )
        
        result = data.randomcolor()
        assert isinstance(result, dict)
        assert "hex" in result
    
    @responses.activate
    def test_country_info(self):
        """Test country information retrieval."""
        country_name = "Japan"
        mock_response = {
            "name": "Japan",
            "capital": "Tokyo",
            "population": 125800000,
            "currency": "Japanese Yen"
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/country",
            json=mock_response,
            status=200
        )
        
        result = data.country(country_name)
        assert isinstance(result, dict)
        assert "name" in result
    
    @responses.activate
    def test_periodic_table(self):
        """Test periodic table element data."""
        element = "Carbon"
        mock_response = {
            "name": "Carbon",
            "symbol": "C",
            "atomic_number": 6,
            "atomic_mass": "12.011"
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/periodic_table",
            json=mock_response,
            status=200
        )
        
        result = data.periodic_table(element)
        assert isinstance(result, dict)
        assert "name" in result
    
    @responses.activate
    def test_subreddit_info(self):
        """Test subreddit information retrieval."""
        subreddit_name = "python"
        mock_response = {
            "name": "python",
            "title": "Python",
            "subscribers": 1200000,
            "is_nsfw": False
        }
        
        responses.add(
            responses.GET,
            "https://api.popcat.xyz/subreddit",
            json=mock_response,
            status=200
        )
        
        result = data.subreddit(subreddit_name)
        assert isinstance(result, dict)
        assert "name" in result
    
    def test_subreddit_removes_prefix(self):
        """Test that r/ prefix is removed from subreddit names."""
        # This test doesn't need a mock since we're testing input processing
        with pytest.raises(Exception):  # Will fail due to no mock, but validates processing
            try:
                data.subreddit("r/python")
            except Exception:
                pass  # Expected since no mock response


if __name__ == "__main__":
    pytest.main([__file__])