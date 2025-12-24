# Design Documentation

## Overview

This document describes the architecture and design decisions of the Perpetual Calendar - Interactive Explorer application.

## Project Goals

1. Create an educational tool for exploring historical dates
2. Provide an intuitive, interactive GUI experience
3. Include comprehensive events covering past, present, and future
4. Ensure cross-platform compatibility
5. Maintain zero external dependencies

## Architecture

### High-Level Structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           Application Window                             │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                            Header                                  │  │
│  │  [Title] [Subtitle]                              [Help] [About]   │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌─────────────────────────────┐  ┌───────────────────────────────────┐│
│  │       Left Panel            │  │         Right Panel               ││
│  │                             │  │                                   ││
│  │  ┌───────────────────────┐  │  │  ┌───────────────────────────┐   ││
│  │  │    Date Controls      │  │  │  │    Events Explorer        │   ││
│  │  │  [Month] [Day] [Year] │  │  │  │  [Era Dropdown]           │   ││
│  │  │  [Show] [Highlight]   │  │  │  │  [Category Dropdown]      │   ││
│  │  │  [Today] [Clear]      │  │  │  │  [Search Box] [Search]    │   ││
│  │  └───────────────────────┘  │  │  │                           │   ││
│  │                             │  │  │  [Events List]            │   ││
│  │  ┌───────────────────────┐  │  │  │                           │   ││
│  │  │   Calendar Display    │  │  │  │  [Event Details]          │   ││
│  │  │                       │  │  │  └───────────────────────────┘   ││
│  │  │   Mon Tue Wed ...     │  │  │                                   ││
│  │  │    1   2   3  ...     │  │  │                                   ││
│  │  │                       │  │  │                                   ││
│  │  └───────────────────────┘  │  │                                   ││
│  │                             │  │                                   ││
│  │  ┌───────────────────────┐  │  │                                   ││
│  │  │    Quick Jump         │  │  │                                   ││
│  │  │  [Moon] [ENIAC] ...   │  │  │                                   ││
│  │  └───────────────────────┘  │  │                                   ││
│  └─────────────────────────────┘  └───────────────────────────────────┘│
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                          Footer/Status Bar                         │  │
│  └───────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

### Class Structure

```
PerpetualCalendar
├── Constants
│   ├── MIN_YEAR = 1500
│   ├── MAX_YEAR = 9999
│   ├── MONTH_NAMES
│   ├── WEEKDAYS
│   └── COLORS
│
├── Initialization
│   ├── _setup_window()
│   ├── _setup_styles()
│   └── _init_variables()
│
├── UI Building
│   ├── _build_header()
│   ├── _build_left_panel()
│   │   ├── _build_date_controls()
│   │   ├── _build_calendar_display()
│   │   └── _build_quick_jump()
│   ├── _build_right_panel()
│   │   └── _build_events_explorer()
│   └── _build_footer()
│
├── Calendar Logic
│   ├── _render_calendar()
│   ├── _validate_year()
│   ├── _validate_day()
│   └── _get_month_number()
│
├── Event Handlers
│   ├── _on_show_calendar()
│   ├── _on_highlight_date()
│   ├── _on_era_change()
│   ├── _on_category_change()
│   ├── _on_search()
│   ├── _on_event_select()
│   └── _on_event_double_click()
│
└── Navigation
    ├── _show_today()
    ├── _jump_to_date()
    └── _clear_selection()


EventsDatabase
├── EVENTS (nested dictionary)
│   ├── "🏛️ Past Events (1500-2010)"
│   │   ├── "📜 Ancient & Medieval History"
│   │   ├── "⚙️ Industrial Revolution"
│   │   ├── "⚔️ World Wars Era"
│   │   ├── "🚀 Space Exploration"
│   │   ├── "💻 Computing Revolution"
│   │   ├── "🔬 Science & Medicine"
│   │   └── "🌍 Political & Social Milestones"
│   │
│   ├── "📱 Present Era (2010-2020)"
│   │   ├── "🔧 Technology Breakthroughs"
│   │   ├── "🤖 AI & Machine Learning"
│   │   └── "🌐 World Events (2010-2020)"
│   │
│   └── "🔮 Future Predictions (from 2020)"
│       ├── "🧠 AI Revolution (Predicted)"
│       ├── "⚛️ Quantum Computing (Predicted)"
│       ├── "🚀 Space Exploration (Predicted)"
│       ├── "💾 AI Chips & Hardware (Predicted)"
│       └── "🌱 Society & Environment (Predicted)"
│
└── Methods
    ├── get_eras()
    ├── get_categories()
    ├── get_events_by_category()
    ├── get_all_events_in_era()
    ├── get_all_events()
    ├── search_events()
    └── get_total_event_count()
```

## Design Decisions

### Year Range: 1500-9999

**Why 1500?**
- Renaissance marks beginning of modern era
- Gregorian calendar calculations remain accurate
- Covers all significant historical events
- Python's calendar module handles this reliably

**Why 9999?**
- Maximum supported by Python's datetime
- Allows far-future predictions
- Practical upper limit for any use case

### Three-Era Structure

1. **Past Events (1500-2010)**: Verified historical facts
2. **Present Era (2010-2020)**: Recent events users remember
3. **Future Predictions (from 2020)**: Clearly labeled forecasts

This structure helps users understand the nature of the information.

### Event Date Format

All events use **ISO 8601**: `YYYY-MM-DD`
- Internationally recognized
- Sortable as strings
- Unambiguous parsing

### Color Scheme

| Element | Color | Purpose |
|---------|-------|---------|
| Primary | #1a73e8 | Actions, highlights |
| Text Dark | #202124 | Main text |
| Text Light | #80868b | Secondary text |
| Highlight | #ea4335 | Selected date |
| Today | #34a853 | Current date |
| Weekend | #ea4335 | Sat/Sun |

### Interactive Features

1. **Double-click navigation**: Industry-standard pattern
2. **Welcome dialog**: Onboards new users
3. **Status bar**: Provides feedback
4. **Quick jump buttons**: Reduces clicks for common tasks

## Future Enhancements

### Planned
- Dark mode theme
- Export to PDF/image
- Custom user events
- Multiple calendar systems

### Potential
- Sound effects
- Animations
- Cloud sync
- Mobile version

## Testing Strategy

### Unit Tests
- Calendar calculations
- Leap year logic
- Date validation
- Event database integrity

### Manual Tests
- Cross-platform appearance
- UI responsiveness
- Event interactions
- Edge cases (year 1500, 9999)

## Conclusion

The Perpetual Calendar provides a comprehensive, educational tool for date exploration. Its clean architecture and thoughtful design make it maintainable and extensible.
