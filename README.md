# Perpetual Calendar - Interactive Explorer v2.0

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive, interactive calendar application built with Python and Tkinter. Explore any date from 1500 to 9999, discover historical events, and see future technology predictions — all through an intuitive graphical interface.

<p align="center">
  <img src="assets/screenshot.png" alt="Perpetual Calendar Screenshot" width="900">
</p>

## ✨ Features

### 📅 Calendar Features
- **Extended Date Range**: Navigate any date from 1500 to 9999
- **Date Highlighting**: Mark specific dates with visual `[N]` indicator
- **Today Indicator**: Current date shown with `(N)` marker
- **Weekend Highlighting**: Saturday and Sunday in distinct color
- **Quick Jump Buttons**: Instantly visit famous historical dates

### 🌍 Events Explorer
- **100+ Events**: Comprehensive database spanning 500+ years
- **Three Time Eras**:
  - 🏛️ **Past Events (1500-2010)**: Ancient history, Industrial Revolution, World Wars, Space exploration, Computing revolution
  - 📱 **Present Era (2010-2020)**: Technology breakthroughs, AI milestones, World events
  - 🔮 **Future Predictions**: AI revolution, Quantum computing, Space colonization, AI chips

### 🎯 Interactive Experience
- **Welcome Guide**: Tutorial on first launch
- **Help System**: Comprehensive documentation
- **Search Function**: Find events by keyword
- **Double-Click Navigation**: Jump to any event's date
- **Real-time Status**: Feedback on all actions

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (included with most Python installations)

### Setup

```bash
# Clone the repository
git clone https://github.com/tharun-ship-it/perpetual-calendar.git
cd perpetual-calendar

# Run the application
python src/calendar_app.py
```

**No additional dependencies required** — uses only Python standard library.

## 📖 Usage

### Basic Calendar Navigation
1. Select month, day, and year using the controls
2. Click **"Show Calendar"** or press **Enter**
3. Calendar displays with current selection

### Highlighting a Date
1. Choose your desired date
2. Click **"Highlight Date"**
3. The date appears marked as `[N]` on the calendar

### Exploring Events
1. Select a **Time Era** (Past/Present/Future)
2. Optionally choose a **Category** to filter
3. **Single-click** an event for details
4. **Double-click** an event to jump to its date

### Quick Jump
Use preset buttons to instantly visit:
- 🌙 Moon Landing (July 20, 1969)
- 💻 First Computer (February 14, 1946)
- 🇺🇸 US Independence (July 4, 1776)
- 🇮🇳 India Independence (August 15, 1947)
- 🌐 WWW Launch (August 6, 1991)
- 📱 iPhone Launch (June 29, 2007)

## 📚 Event Categories

### 🏛️ Past Events (1500-2010)

| Category | Events | Highlights |
|----------|--------|------------|
| 📜 Ancient & Medieval | 9 | Renaissance, Reformation, Newton |
| ⚙️ Industrial Revolution | 14 | Steam engine, Railways, Automobiles |
| ⚔️ World Wars | 11 | WWI, WWII, key battles |
| 🚀 Space Exploration | 11 | Sputnik, Moon landing, Mars rovers |
| 💻 Computing Revolution | 16 | ENIAC, Internet, iPhone |
| 🔬 Science & Medicine | 9 | DNA, Penicillin, Genome |
| 🌍 Political & Social | 12 | Independence movements, Civil rights |

### 📱 Present Era (2010-2020)

| Category | Events |
|----------|--------|
| 🔧 Technology Breakthroughs | 12 |
| 🤖 AI & Machine Learning | 10 |
| 🌐 World Events | 11 |

### 🔮 Future Predictions (from June 2020)

| Category | Predictions |
|----------|-------------|
| 🧠 AI Revolution | 10 |
| ⚛️ Quantum Computing | 8 |
| 🚀 Space Exploration | 10 |
| 💾 AI Chips & Hardware | 8 |
| 🌱 Society & Environment | 7 |

> **Note**: Future predictions reflect forecasts made in June 2020 and are included for educational purposes.

## 🚀 Live Demo

**[👉 Click here to try the Live Demo](https://tharun-ship-it.github.io/perpetual-calendar-interactive-explorer/)**

## 📁 Project Structure
```
perpetual-calendar-interactive-explorer/
├── src/
│   ├── __init__.py          # Package initialization
│   └── calendar_app.py      # Main application (800+ lines)
├── tests/
│   ├── __init__.py
│   └── test_calendar.py     # Unit tests
├── docs/
│   └── DESIGN.md            # Architecture documentation
├── assets/
│   └── screenshot.png       # Application screenshot
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI/CD
├── index.html               # Web version (Live Demo)
├── .gitignore
├── LICENSE                  # MIT License
├── README.md
├── CONTRIBUTING.md
├── pyproject.toml
└── requirements.txt
```

## 🧪 Running Tests

```bash
# Using pytest
python -m pytest tests/ -v

# Using unittest
python -m unittest tests.test_calendar -v
```

## 🔧 Technical Details

### Calendar Calculations
- Uses Python's `calendar` module with proleptic Gregorian calendar
- **Leap year rules**: Divisible by 4, except centuries unless divisible by 400
- **Week start**: Monday (ISO 8601 standard)

### Architecture
```
PerpetualCalendar (Main Class)
├── UI Components
│   ├── Header (title, buttons)
│   ├── Left Panel (controls, calendar, quick jump)
│   └── Right Panel (events explorer)
├── Calendar Logic
│   ├── Date validation
│   ├── Calendar rendering
│   └── Navigation
└── Events System
    ├── EventsDatabase (static data)
    ├── Search functionality
    └── Interactive navigation

EventsDatabase (Data Class)
├── Past Events (7 categories)
├── Present Era (3 categories)
└── Future Predictions (5 categories)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- [ ] Dark mode theme
- [ ] Export to PDF/Image
- [ ] Custom user events
- [ ] Multiple calendar systems
- [ ] Localization support
- [ ] Sound effects

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Tharun Ponnam**

- GitHub: [@tharun-ship-it](https://github.com/tharun-ship-it)
- Email: tharunponnam007@gmail.com

---

*Created: June 2020*
