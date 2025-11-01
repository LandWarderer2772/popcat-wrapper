#!/usr/bin/env python3
"""Test script to verify package installation and basic functionality."""

import sys

def test_import():
    """Test that the package imports correctly."""
    try:
        import popcat
        print("✅ Package import successful")
        print(f"📦 Version: {popcat.__version__}")
        print(f"👤 Author: {popcat.__author__}")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_basic_functions():
    """Test basic functions without making API calls."""
    try:
        import popcat
        
        # Test that functions exist
        functions_to_test = [
            'joke', 'fact', 'drake', 'weather', 'translate', 'jail'
        ]
        
        for func_name in functions_to_test:
            if hasattr(popcat, func_name):
                print(f"✅ Function '{func_name}' exists")
            else:
                print(f"❌ Function '{func_name}' missing")
                return False
        
        # Test classes
        try:
            client = popcat.CodeClient("test-key")
            print("✅ CodeClient class works")
        except Exception as e:
            print(f"❌ CodeClient error: {e}")
            return False
            
        print("✅ All basic function tests passed")
        return True
        
    except Exception as e:
        print(f"❌ Basic function test failed: {e}")
        return False

def test_live_api_calls():
    """Test actual API calls (optional - requires internet)."""
    try:
        import popcat
        
        print("\n🌐 Testing live API calls...")
        
        # Test a simple endpoint
        joke = popcat.joke()
        print(f"✅ Joke API: {joke[:50]}...")
        
        # Test another endpoint
        fact = popcat.fact()
        print(f"✅ Fact API: {fact[:50]}...")
        
        print("✅ Live API tests passed")
        return True
        
    except Exception as e:
        print(f"❌ Live API test failed: {e}")
        print("💡 This might be due to network issues or API rate limits")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing popcat.py Installation\n")
    
    # Test 1: Import
    if not test_import():
        sys.exit(1)
    
    print()
    
    # Test 2: Basic functionality
    if not test_basic_functions():
        sys.exit(1)
    
    # Test 3: Live API (optional)
    test_live_api_calls()
    
    print("\n🎉 All tests completed!")

if __name__ == "__main__":
    main()