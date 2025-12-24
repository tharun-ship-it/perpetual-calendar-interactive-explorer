# Contributing to Perpetual Calendar

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/perpetual-calendar.git
   cd perpetual-calendar
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

## Code Style

This project follows:
- [Black](https://github.com/psf/black) code formatting (line length: 100)
- [Type hints](https://docs.python.org/3/library/typing.html) for all functions
- Comprehensive docstrings for classes and methods

Before submitting a PR:
```bash
# Format code
black src/ tests/

# Type check
mypy src/ --ignore-missing-imports

# Run tests
python -m pytest tests/ -v
```

## Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit with clear messages:
   ```bash
   git commit -m "Add feature: description of what you added"
   ```

3. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Open a Pull Request** with a clear description

5. **Ensure all CI checks pass**

## Adding Events

When adding new historical events:

1. Use ISO 8601 date format: `YYYY-MM-DD`
2. Verify the date accuracy from multiple sources
3. Keep titles concise (under 40 characters)
4. Write descriptive but brief descriptions
5. Place in the appropriate era and category

Example:
```python
("1969-07-20", "Moon Landing", "Neil Armstrong and Buzz Aldrin walk on the Moon"),
```

## Reporting Issues

When reporting issues, include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers
- Focus on the code, not the person

## Questions?

Feel free to open an issue for questions or discussions.

Thank you for contributing! 🙏
