# Contributing

We welcome contributions to Popcat.py! Here's how you can help.

## Development Setup

### Prerequisites

- Python 3.7 or higher
- Git

### Setting up the development environment

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/LandWarderer2772/pop-wrapper.git
   cd pop-wrapper
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**:
   ```bash
   pip install -e .[dev]
   ```

4. **Install pre-commit hooks** (optional but recommended):
   ```bash
   pre-commit install
   ```

## Making Changes

### Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **flake8** for linting  
- **mypy** for type checking
- **pytest** for testing

Run these before submitting:

```bash
black popcat/ tests/
   flake8 popcat/ tests/
   pytest
```

### Adding New Endpoints

When the Popcat API adds new endpoints, here's how to add them:

1. **Choose the appropriate module** based on the endpoint's purpose:
   - `image.py` - Image manipulation
   - `meme.py` - Meme generation
   - `data.py` - Data/information APIs
   - `text.py` - Text utilities
   - `random.py` - Random content
   - `utilities.py` - General utilities

2. **Implement the function** following the existing pattern:

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
    _validate_text(parameter)  # Use appropriate validation
    return _make_request("/new-endpoint", {"param": parameter})
```

3. **Add the function to `__all__`** in the module
4. **Add it to the main `__init__.py`** imports
5. **Write tests** in the appropriate test file
6. **Update documentation** in the README

### ONLY ADD ENPOINTS THAT ARE STABLE AND DOCUMENTED IN THE OFFICIAL POPCAT API DOCS

### Writing Tests

All new functions should have tests. Use the existing test structure:

```python
@responses.activate
def test_new_function(self):
    """Test new function with valid input."""
    responses.add(
        responses.GET,
        "https://api.popcat.xyz/new-endpoint",
        json={"result": "expected"},
        status=200
    )
    
    result = module.new_function("test_input")
    assert isinstance(result, dict)
    assert "result" in result

def test_new_function_invalid_input(self):
    """Test new function with invalid input."""
    with pytest.raises(ValueError, match="Input must be valid"):
        module.new_function("")
```

### Documentation

When adding new features:

1. **Add comprehensive docstrings** with examples
2. **Update the README** with new functions
3. **Add to the docs** if needed
4. **Include usage examples**

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_image.py

# Run with coverage
pytest --cov=popcat

# Run integration tests (requires internet)
pytest tests/integration/ -m integration
```

### Test Categories

- **Unit tests**: Test individual functions with mocked responses
- **Integration tests**: Test actual API calls (run manually)
- **Error handling tests**: Test validation and error cases

### Writing Integration Tests

For integration tests (that make real API calls):

```python
import pytest

@pytest.mark.integration
def test_weather_integration():
    """Integration test - makes real API call."""
    result = popcat.weather("London")
    assert isinstance(result, dict)
    assert "temperature" in result
```

Run integration tests with: `pytest -m integration`

## Submitting Changes

### Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/add-new-endpoint
   ```

2. **Make your changes** following the guidelines above

3. **Test your changes**:
   ```bash
   pytest tests/
   black popcat/ tests/
   flake8 popcat/ tests/
   ```

4. **Commit with clear messages**:
   ```bash
   git add .
   git commit -m "Add support for new endpoint"
   ```

5. **Push and create a pull request**:
   ```bash
   git push origin feature/add-new-endpoint
   ```

### Pull Request Guidelines

- **Clear title and description**
- **Reference any related issues**
- **Include tests for new functionality**
- **Update documentation as needed**
- **Ensure all checks pass**

### Commit Message Format

Use clear, descriptive commit messages:

```
Add weather endpoint support

- Implement weather() function in data.py
- Add comprehensive error handling
- Include tests and documentation
- Update README with usage examples

Fixes #123
```

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

- **Python version**
- **Package version**
- **Minimal code to reproduce**
- **Expected vs actual behavior**
- **Error messages/tracebacks**

### Feature Requests

For new features:

- **Describe the use case**
- **Explain the expected behavior**
- **Provide examples if possible**
- **Consider backwards compatibility**

## Release Process

For maintainers:

1. **Update version** in `pyproject.toml` and `__init__.py`
2. **Update CHANGELOG.md**
3. **Create a release tag**
4. **Build and upload to PyPI**:
   ```bash
   python -m build
   twine upload dist/*
   ```

## Getting Help

- **Open an issue**: For bugs or feature requests on [GitHub](https://github.com/LandWarderer2772/pop-wrapper/issues)
- **Discord**: Contact land_lmao
- **Email**: mh3as81gb@mozmail.com

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## Recognition

Contributors will be:

- **Listed in CONTRIBUTORS.md**
- **Mentioned in release notes**
- **Given credit in documentation**

Thank you for contributing to pop-wrapper! 🎉
