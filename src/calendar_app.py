#!/usr/bin/env python3
"""
Perpetual Calendar - Interactive Explorer

A comprehensive, interactive GUI calendar application featuring:
- Date range from 1500 to 9999
- Date highlighting with visual markers
- Historical events database (Past, Present, Future predictions)
- Interactive user experience with guided exploration
- Educational content across multiple eras

Author: Tharun Ponnam
Created: June 2020
"""

import calendar
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from typing import Optional, Dict, List, Tuple


class EventsDatabase:
    """
    Comprehensive database of historical, present, and predicted future events.
    
    The database is organized into three main eras:
    - Past Events: Historical facts from 1500 onwards
    - Present Era: Events from 2010 to June 2020
    - Future Predictions: Forecasts made in June 2020 about upcoming developments
    
    Note: Future predictions reflect the perspective and knowledge available in June 2020.
    """
    
    EVENTS: Dict[str, Dict[str, List[Tuple[str, str, str]]]] = {
        "🏛️ Past Events (1500-2010)": {
            "📜 Ancient & Medieval History": [
                ("1500-01-01", "Renaissance Era", "The Renaissance transforms European art, science, and culture"),
                ("1517-10-31", "Protestant Reformation", "Martin Luther posts 95 Theses, sparking religious reformation"),
                ("1543-05-24", "Heliocentric Theory", "Copernicus publishes revolutionary theory that Earth orbits the Sun"),
                ("1564-04-26", "Shakespeare Born", "William Shakespeare, the greatest English writer, is born"),
                ("1600-02-17", "Giordano Bruno Executed", "Philosopher burned for supporting Copernican heliocentrism"),
                ("1609-08-25", "Galileo's Telescope", "Galileo presents his telescope to Venetian lawmakers"),
                ("1687-07-05", "Newton's Principia", "Isaac Newton publishes laws of motion and universal gravitation"),
                ("1776-07-04", "US Independence", "United States Declaration of Independence adopted"),
                ("1789-07-14", "French Revolution", "Storming of the Bastille marks beginning of French Revolution"),
            ],
            "⚙️ Industrial Revolution": [
                ("1712-01-01", "First Steam Engine", "Thomas Newcomen builds first practical steam engine for pumping water"),
                ("1769-01-01", "Watt's Steam Engine", "James Watt patents improved steam engine with separate condenser"),
                ("1793-03-14", "Cotton Gin Invented", "Eli Whitney invents cotton gin, revolutionizing textile industry"),
                ("1804-02-21", "First Steam Locomotive", "Richard Trevithick demonstrates first railway steam locomotive"),
                ("1825-09-27", "First Public Railway", "Stockton and Darlington Railway opens as first public railway"),
                ("1831-08-29", "Electromagnetic Induction", "Michael Faraday discovers electromagnetic induction"),
                ("1856-01-01", "Bessemer Steel Process", "Henry Bessemer patents mass steel production method"),
                ("1876-03-10", "Telephone Invented", "Alexander Graham Bell patents the telephone"),
                ("1879-10-21", "Electric Light Bulb", "Thomas Edison successfully tests incandescent light bulb"),
                ("1885-01-29", "First Automobile", "Karl Benz patents the first true gasoline-powered automobile"),
                ("1895-12-28", "First Film Screening", "Lumière brothers hold first public film screening in Paris"),
                ("1903-12-17", "First Powered Flight", "Wright Brothers achieve first controlled powered airplane flight"),
                ("1908-10-01", "Model T Production", "Ford begins mass production of affordable Model T automobile"),
                ("1913-12-01", "Assembly Line", "Henry Ford introduces moving assembly line, revolutionizing manufacturing"),
            ],
            "⚔️ World Wars Era": [
                ("1914-06-28", "Archduke Assassination", "Assassination of Archduke Franz Ferdinand triggers WWI"),
                ("1914-07-28", "World War I Begins", "Austria-Hungary declares war on Serbia, starting WWI"),
                ("1917-04-06", "US Enters WWI", "United States declares war on Germany"),
                ("1918-11-11", "World War I Ends", "Armistice signed at 11am on 11/11, ending WWI"),
                ("1929-10-29", "Black Tuesday", "Stock market crash triggers the Great Depression"),
                ("1939-09-01", "World War II Begins", "Germany invades Poland, starting World War II"),
                ("1941-12-07", "Pearl Harbor Attack", "Japan attacks Pearl Harbor; US enters WWII"),
                ("1944-06-06", "D-Day Invasion", "Allied forces land on Normandy beaches"),
                ("1945-05-08", "Victory in Europe", "Nazi Germany surrenders unconditionally"),
                ("1945-08-06", "Hiroshima", "First atomic bomb used in warfare on Hiroshima"),
                ("1945-08-15", "WWII Ends", "Japan announces surrender, ending World War II"),
            ],
            "🚀 Space Exploration": [
                ("1957-10-04", "Sputnik 1 Launch", "Soviet Union launches first artificial satellite into orbit"),
                ("1961-04-12", "First Human in Space", "Yuri Gagarin becomes first human to journey into outer space"),
                ("1962-02-20", "Glenn Orbits Earth", "John Glenn becomes first American to orbit Earth"),
                ("1963-06-16", "First Woman in Space", "Valentina Tereshkova becomes first woman in space"),
                ("1969-07-20", "Moon Landing", "Neil Armstrong and Buzz Aldrin walk on the Moon"),
                ("1971-04-19", "First Space Station", "Soviet Union launches Salyut 1, first space station"),
                ("1981-04-12", "First Space Shuttle", "Columbia becomes first reusable spacecraft to reach orbit"),
                ("1986-01-28", "Challenger Disaster", "Space Shuttle Challenger breaks apart 73 seconds after launch"),
                ("1990-04-24", "Hubble Telescope", "Hubble Space Telescope deployed in Earth orbit"),
                ("1998-11-20", "ISS Construction", "First module of International Space Station launched"),
                ("2004-01-04", "Mars Rovers Land", "Spirit and Opportunity rovers begin Mars exploration"),
            ],
            "💻 Computing Revolution": [
                ("1946-02-14", "ENIAC Unveiled", "ENIAC, first general-purpose electronic computer, is unveiled"),
                ("1947-12-23", "Transistor Invented", "Bell Labs demonstrates the first transistor"),
                ("1958-09-12", "Integrated Circuit", "Jack Kilby demonstrates first working integrated circuit"),
                ("1969-10-29", "ARPANET First Message", "First message sent over ARPANET, precursor to the Internet"),
                ("1971-11-15", "First Microprocessor", "Intel releases 4004, the first commercial microprocessor"),
                ("1975-04-04", "Microsoft Founded", "Bill Gates and Paul Allen found Microsoft"),
                ("1976-04-01", "Apple Founded", "Steve Jobs and Steve Wozniak found Apple Computer"),
                ("1981-08-12", "IBM PC Released", "IBM introduces the Personal Computer, defining the PC standard"),
                ("1983-01-01", "TCP/IP Adopted", "ARPANET adopts TCP/IP protocol, birth of modern Internet"),
                ("1984-01-24", "Macintosh Introduced", "Apple introduces the Macintosh with revolutionary GUI"),
                ("1989-03-12", "WWW Proposed", "Tim Berners-Lee proposes the World Wide Web"),
                ("1991-08-06", "World Wide Web Live", "First website goes live, making the web publicly available"),
                ("1995-08-24", "Windows 95", "Microsoft releases Windows 95, revolutionizing PC usage"),
                ("1998-09-04", "Google Founded", "Larry Page and Sergey Brin found Google Inc."),
                ("2004-02-04", "Facebook Launched", "Mark Zuckerberg launches Facebook from Harvard"),
                ("2007-01-09", "iPhone Unveiled", "Steve Jobs unveils iPhone, beginning the smartphone revolution"),
            ],
            "🔬 Science & Medicine": [
                ("1859-11-24", "Origin of Species", "Charles Darwin publishes theory of evolution by natural selection"),
                ("1895-11-08", "X-Rays Discovered", "Wilhelm Röntgen discovers X-rays"),
                ("1905-06-30", "Special Relativity", "Einstein publishes special theory of relativity (E=mc²)"),
                ("1928-09-28", "Penicillin Discovered", "Alexander Fleming discovers penicillin antibiotic"),
                ("1953-04-25", "DNA Structure", "Watson and Crick publish DNA double helix structure"),
                ("1967-12-03", "First Heart Transplant", "Dr. Christiaan Barnard performs first human heart transplant"),
                ("1978-07-25", "First IVF Baby", "Louise Brown, first test-tube baby, is born"),
                ("1996-07-05", "Dolly the Sheep", "First mammal cloned from an adult cell"),
                ("2003-04-14", "Human Genome Complete", "Human Genome Project completes mapping of human DNA"),
            ],
            "🌍 Political & Social Milestones": [
                ("1863-01-01", "Emancipation Proclamation", "Lincoln declares slaves in rebel states free"),
                ("1865-04-15", "Lincoln Assassinated", "President Abraham Lincoln is assassinated"),
                ("1893-09-19", "Women's Suffrage NZ", "New Zealand becomes first country with women's voting rights"),
                ("1920-08-26", "US Women Vote", "19th Amendment grants American women right to vote"),
                ("1947-08-15", "India Independence", "India gains independence from British rule"),
                ("1948-05-14", "Israel Founded", "State of Israel declared, recognized by major powers"),
                ("1963-08-28", "I Have a Dream", "Martin Luther King Jr. delivers iconic speech in Washington"),
                ("1964-07-02", "Civil Rights Act", "Landmark US legislation outlaws discrimination"),
                ("1989-11-09", "Berlin Wall Falls", "Fall of Berlin Wall symbolizes end of Cold War"),
                ("1990-02-11", "Mandela Released", "Nelson Mandela freed after 27 years in prison"),
                ("1991-12-26", "Soviet Union Dissolves", "USSR officially dissolves, ending the Cold War"),
                ("1994-04-27", "South Africa Democracy", "Nelson Mandela elected in first multi-racial election"),
            ],
        },
        "📱 Present Era (2010-2020)": {
            "🔧 Technology Breakthroughs": [
                ("2010-01-27", "iPad Announced", "Apple unveils iPad, creating modern tablet market"),
                ("2010-10-06", "Instagram Launched", "Photo-sharing app Instagram launches on iOS"),
                ("2011-10-05", "Steve Jobs Passes Away", "Apple co-founder Steve Jobs dies at age 56"),
                ("2012-04-09", "Facebook Buys Instagram", "Facebook acquires Instagram for $1 billion"),
                ("2012-05-18", "Facebook IPO", "Facebook goes public at $38 per share"),
                ("2013-11-15", "PlayStation 4 Released", "Sony releases next-gen gaming console"),
                ("2014-03-25", "Facebook Buys Oculus", "Facebook acquires Oculus VR for $2 billion"),
                ("2015-04-24", "Apple Watch Released", "Apple enters wearables market with Apple Watch"),
                ("2016-07-06", "Pokemon Go Released", "Augmented reality game becomes global phenomenon"),
                ("2017-11-03", "iPhone X Released", "Apple introduces Face ID and full-screen display"),
                ("2018-02-06", "SpaceX Falcon Heavy", "SpaceX launches most powerful rocket since Saturn V"),
                ("2019-04-10", "First Black Hole Image", "Event Horizon Telescope captures first black hole image"),
            ],
            "🤖 AI & Machine Learning": [
                ("2011-10-04", "Siri Introduced", "Apple introduces Siri voice assistant with iPhone 4S"),
                ("2012-06-26", "Google Brain", "Neural network learns to recognize cats from YouTube videos"),
                ("2014-01-26", "Google Buys DeepMind", "Google acquires AI company DeepMind for $500 million"),
                ("2015-12-11", "OpenAI Founded", "Elon Musk and others found AI research organization OpenAI"),
                ("2016-03-15", "AlphaGo Defeats Lee Sedol", "DeepMind's AI defeats world Go champion 4-1"),
                ("2017-05-27", "AlphaGo Retires", "AlphaGo defeats world #1 Ke Jie, then retires from competition"),
                ("2017-10-18", "AlphaGo Zero", "AI learns Go from scratch, surpasses all human knowledge"),
                ("2018-06-15", "GPT-1 Released", "OpenAI releases first Generative Pre-trained Transformer"),
                ("2019-02-14", "GPT-2 Announced", "OpenAI announces GPT-2, initially withholds full release"),
                ("2020-06-11", "GPT-3 Released", "OpenAI releases GPT-3 with 175 billion parameters"),
            ],
            "🌐 World Events (2010-2020)": [
                ("2010-04-20", "Deepwater Horizon", "BP oil spill becomes largest marine oil spill in history"),
                ("2011-03-11", "Fukushima Disaster", "Earthquake and tsunami cause nuclear disaster in Japan"),
                ("2011-05-02", "Bin Laden Killed", "US forces kill Al-Qaeda leader Osama bin Laden"),
                ("2012-08-06", "Curiosity on Mars", "NASA's Curiosity rover successfully lands on Mars"),
                ("2015-12-12", "Paris Climate Agreement", "195 nations adopt landmark climate change agreement"),
                ("2016-06-23", "Brexit Vote", "UK votes 52%-48% to leave the European Union"),
                ("2016-11-08", "Trump Elected", "Donald Trump wins US presidential election"),
                ("2018-06-12", "US-North Korea Summit", "Historic meeting between Trump and Kim Jong-un"),
                ("2019-12-31", "COVID-19 First Cases", "First cases of novel coronavirus reported in Wuhan, China"),
                ("2020-01-31", "UK Leaves EU", "United Kingdom officially exits the European Union"),
                ("2020-03-11", "COVID-19 Pandemic", "WHO declares COVID-19 a global pandemic"),
            ],
        },
        "🔮 Future Predictions (from 2020)": {
            "🧠 AI Revolution (Predicted)": [
                ("2021-06-01", "AI Medical Diagnosis", "AI systems predicted to achieve doctor-level diagnosis accuracy"),
                ("2022-01-01", "AI Writing Tools", "Advanced AI writing assistants predicted for mainstream use"),
                ("2023-01-01", "AI Art Generation", "AI systems predicted to create professional-quality artwork"),
                ("2024-01-01", "AI Personal Assistants", "Highly capable AI assistants predicted for daily tasks"),
                ("2025-01-01", "AI in Education", "AI tutors predicted to revolutionize personalized learning"),
                ("2027-01-01", "AI-Human Collaboration", "AI predicted to become standard workplace collaborator"),
                ("2030-01-01", "AGI Progress", "Significant progress toward Artificial General Intelligence predicted"),
                ("2035-01-01", "AI Governance", "International AI regulation and ethics frameworks predicted"),
                ("2040-01-01", "AI Scientific Discovery", "AI predicted to independently make major scientific breakthroughs"),
                ("2050-01-01", "Human-AI Integration", "Deep integration between human cognition and AI predicted"),
            ],
            "⚛️ Quantum Computing (Predicted)": [
                ("2021-01-01", "50+ Qubit Systems", "Quantum computers with 50+ stable qubits predicted"),
                ("2023-01-01", "100+ Qubit Milestone", "Quantum computers reaching 100+ qubits predicted"),
                ("2025-01-01", "Quantum Cloud Access", "Quantum computing predicted available via major cloud platforms"),
                ("2027-01-01", "Quantum Drug Discovery", "Quantum computers predicted to revolutionize pharmaceutical research"),
                ("2030-01-01", "Quantum Cryptography", "Quantum-safe encryption predicted to become industry standard"),
                ("2035-01-01", "Quantum Internet", "First experimental quantum internet networks predicted"),
                ("2040-01-01", "Quantum Advantage", "Quantum computers predicted to solve previously impossible problems"),
                ("2050-01-01", "Universal Quantum Computing", "General-purpose quantum computers predicted for widespread use"),
            ],
            "🚀 Space Exploration (Predicted)": [
                ("2021-02-01", "Mars Perseverance", "NASA Perseverance rover predicted to land on Mars"),
                ("2021-12-01", "James Webb Telescope", "Next-generation space telescope predicted to launch"),
                ("2024-01-01", "Artemis Moon Mission", "NASA predicted to return humans to the Moon"),
                ("2025-01-01", "Commercial Space Stations", "Private space stations predicted to begin operations"),
                ("2026-01-01", "SpaceX Starship to Mars", "SpaceX predicted to send Starship toward Mars"),
                ("2028-01-01", "Lunar Gateway", "Orbital lunar station predicted to be operational"),
                ("2030-01-01", "First Humans on Mars", "SpaceX or NASA predicted to land humans on Mars"),
                ("2035-01-01", "Permanent Moon Base", "Permanent human presence on the Moon predicted"),
                ("2040-01-01", "Mars Colony Started", "First permanent Mars settlement predicted to begin"),
                ("2050-01-01", "Regular Mars Travel", "Regular Earth-Mars transportation predicted"),
            ],
            "💾 AI Chips & Hardware (Predicted)": [
                ("2021-01-01", "Neural Processing Units", "Dedicated AI chips predicted in most new smartphones"),
                ("2022-01-01", "AI-Optimized GPUs", "Next-gen GPUs with enhanced AI capabilities predicted"),
                ("2023-01-01", "Edge AI Devices", "Powerful AI processing in small devices predicted"),
                ("2025-01-01", "AI Chips Everywhere", "Specialized AI processors predicted in all smart devices"),
                ("2027-01-01", "Neuromorphic Chips", "Brain-inspired computing chips predicted for commercial use"),
                ("2030-01-01", "AI Supercomputers", "Exascale AI-dedicated supercomputers predicted"),
                ("2035-01-01", "Quantum-AI Hybrid", "Quantum-classical hybrid AI processors predicted"),
                ("2040-01-01", "Molecular Computing", "Molecular-scale computing elements predicted"),
            ],
            "🌱 Society & Environment (Predicted)": [
                ("2022-01-01", "Remote Work Standard", "Remote work predicted to become permanent for many jobs"),
                ("2025-01-01", "Electric Vehicles Dominant", "EVs predicted to outsell gasoline vehicles in major markets"),
                ("2027-01-01", "Renewable Energy Majority", "Renewables predicted to provide majority of new electricity"),
                ("2030-01-01", "Smart Cities", "AI-managed smart cities predicted in major metropolitan areas"),
                ("2035-01-01", "Carbon Capture", "Large-scale carbon capture technology predicted to operate"),
                ("2040-01-01", "Fusion Power Progress", "Commercial nuclear fusion power plants predicted"),
                ("2050-01-01", "Net Zero Progress", "Many developed nations predicted to achieve net-zero emissions"),
            ],
        },
    }
    
    @classmethod
    def get_eras(cls) -> List[str]:
        """Return list of available time eras."""
        return list(cls.EVENTS.keys())
    
    @classmethod
    def get_categories(cls, era: str) -> List[str]:
        """Return categories available for a specific era."""
        return list(cls.EVENTS.get(era, {}).keys())
    
    @classmethod
    def get_events_by_category(cls, era: str, category: str) -> List[Tuple[str, str, str]]:
        """Return events for a specific era and category combination."""
        return cls.EVENTS.get(era, {}).get(category, [])
    
    @classmethod
    def get_all_events_in_era(cls, era: str) -> List[Tuple[str, str, str]]:
        """Return all events within a specific era, sorted by date."""
        all_events = []
        for category_events in cls.EVENTS.get(era, {}).values():
            all_events.extend(category_events)
        return sorted(all_events, key=lambda x: x[0])
    
    @classmethod
    def get_all_events(cls) -> List[Tuple[str, str, str]]:
        """Return all events across all eras, sorted by date."""
        all_events = []
        for era_data in cls.EVENTS.values():
            for category_events in era_data.values():
                all_events.extend(category_events)
        return sorted(all_events, key=lambda x: x[0])
    
    @classmethod
    def search_events(cls, keyword: str) -> List[Tuple[str, str, str]]:
        """Search events by keyword in title or description."""
        keyword_lower = keyword.lower()
        results = []
        for era_data in cls.EVENTS.values():
            for category_events in era_data.values():
                for event in category_events:
                    if keyword_lower in event[1].lower() or keyword_lower in event[2].lower():
                        results.append(event)
        return sorted(results, key=lambda x: x[0])
    
    @classmethod
    def get_total_event_count(cls) -> int:
        """Return total number of events in the database."""
        count = 0
        for era_data in cls.EVENTS.values():
            for category_events in era_data.values():
                count += len(category_events)
        return count


class PerpetualCalendar:
    """
    Interactive Perpetual Calendar Application.
    
    A comprehensive calendar application that allows users to:
    - Navigate any date from 1500 to 9999
    - Highlight specific dates with visual markers
    - Explore historical events, present milestones, and future predictions
    - Search for events by keyword
    - Interactively jump to event dates
    
    The application features a user-friendly interface with guided exploration
    and educational content spanning over 500 years of history plus future forecasts.
    """
    
    MIN_YEAR = 1500
    MAX_YEAR = 9999
    APP_TITLE = "📅 Perpetual Calendar - Interactive Explorer"
    WINDOW_GEOMETRY = "1200x800"
    MIN_WIDTH = 1100
    MIN_HEIGHT = 700
    
    MONTH_NAMES = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # Modern color scheme
    COLORS = {
        "bg_main": "#f0f2f5",
        "bg_card": "#ffffff",
        "primary": "#1a73e8",
        "primary_dark": "#1557b0",
        "secondary": "#5f6368",
        "text_dark": "#202124",
        "text_medium": "#5f6368",
        "text_light": "#80868b",
        "accent_red": "#ea4335",
        "accent_green": "#34a853",
        "accent_yellow": "#fbbc04",
        "accent_blue": "#4285f4",
        "border": "#dadce0",
        "highlight": "#ea4335",
        "today": "#34a853",
        "weekend": "#ea4335",
    }
    
    def __init__(self, root: tk.Tk) -> None:
        """Initialize the Perpetual Calendar application."""
        self.root = root
        self.selected_date: Optional[Tuple[int, int, int]] = None
        self.current_events: List[Tuple[str, str, str]] = []
        
        self._setup_window()
        self._setup_styles()
        self._init_variables()
        self._build_ui()
        self._bind_events()
        self._show_today()
        self._show_welcome()
    
    def _setup_window(self) -> None:
        """Configure the main application window."""
        self.root.title(self.APP_TITLE)
        self.root.geometry(self.WINDOW_GEOMETRY)
        self.root.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.root.configure(bg=self.COLORS["bg_main"])
        
        # Grid configuration
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(1, weight=1)
    
    def _setup_styles(self) -> None:
        """Configure ttk styles for the application."""
        style = ttk.Style()
        
        if "clam" in style.theme_names():
            style.theme_use("clam")
        
        # Frame styles
        style.configure("Card.TFrame", background=self.COLORS["bg_card"])
        style.configure("Main.TFrame", background=self.COLORS["bg_main"])
        
        # Label styles
        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 22, "bold"),
            foreground=self.COLORS["text_dark"],
            background=self.COLORS["bg_card"]
        )
        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 11),
            foreground=self.COLORS["text_medium"],
            background=self.COLORS["bg_card"]
        )
        style.configure(
            "Header.TLabel",
            font=("Segoe UI", 13, "bold"),
            foreground=self.COLORS["text_dark"],
            background=self.COLORS["bg_card"]
        )
        style.configure(
            "Normal.TLabel",
            font=("Segoe UI", 10),
            foreground=self.COLORS["text_dark"],
            background=self.COLORS["bg_card"]
        )
        style.configure(
            "Small.TLabel",
            font=("Segoe UI", 9),
            foreground=self.COLORS["text_light"],
            background=self.COLORS["bg_card"]
        )
        
        # Button styles
        style.configure(
            "Primary.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(12, 8)
        )
        style.configure(
            "Secondary.TButton",
            font=("Segoe UI", 10),
            padding=(10, 6)
        )
        
        # LabelFrame style
        style.configure(
            "Card.TLabelframe",
            background=self.COLORS["bg_card"]
        )
        style.configure(
            "Card.TLabelframe.Label",
            font=("Segoe UI", 11, "bold"),
            foreground=self.COLORS["primary"],
            background=self.COLORS["bg_card"]
        )
    
    def _init_variables(self) -> None:
        """Initialize tkinter StringVar variables."""
        now = datetime.now()
        self.month_var = tk.StringVar(value=self.MONTH_NAMES[now.month - 1])
        self.day_var = tk.StringVar(value=str(now.day))
        self.year_var = tk.StringVar(value=str(now.year))
        self.era_var = tk.StringVar(value="")
        self.category_var = tk.StringVar(value="")
        self.search_var = tk.StringVar()
    
    def _build_ui(self) -> None:
        """Build the complete user interface."""
        self._build_header()
        self._build_left_panel()
        self._build_right_panel()
        self._build_footer()
    
    def _build_header(self) -> None:
        """Build the application header section."""
        header = ttk.Frame(self.root, style="Card.TFrame", padding="20 15")
        header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 5))
        
        # Title section
        title_frame = ttk.Frame(header, style="Card.TFrame")
        title_frame.pack(side="left", fill="x", expand=True)
        
        ttk.Label(
            title_frame,
            text="📅 Perpetual Calendar",
            style="Title.TLabel"
        ).pack(side="left")
        
        ttk.Label(
            title_frame,
            text="  •  Explore 1500 to 9999  •  100+ Historical Events  •  Future Predictions",
            style="Subtitle.TLabel"
        ).pack(side="left", padx=(10, 0))
        
        # Action buttons
        btn_frame = ttk.Frame(header, style="Card.TFrame")
        btn_frame.pack(side="right")
        
        ttk.Button(
            btn_frame,
            text="❓ Help",
            command=self._show_help,
            style="Secondary.TButton"
        ).pack(side="left", padx=5)
        
        ttk.Button(
            btn_frame,
            text="ℹ️ About",
            command=self._show_about,
            style="Secondary.TButton"
        ).pack(side="left")
    
    def _build_left_panel(self) -> None:
        """Build the left panel with calendar controls and display."""
        left_panel = ttk.Frame(self.root, style="Main.TFrame", padding="5")
        left_panel.grid(row=1, column=0, sticky="nsew", padx=(10, 5), pady=5)
        left_panel.columnconfigure(0, weight=1)
        left_panel.rowconfigure(1, weight=1)
        
        self._build_date_controls(left_panel)
        self._build_calendar_display(left_panel)
        self._build_quick_jump(left_panel)
    
    def _build_date_controls(self, parent: ttk.Frame) -> None:
        """Build the date selection controls."""
        control_frame = ttk.LabelFrame(
            parent,
            text="📆 Select Date",
            style="Card.TLabelframe",
            padding="15"
        )
        control_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        
        # Input row
        input_row = ttk.Frame(control_frame, style="Card.TFrame")
        input_row.pack(fill="x", pady=(0, 15))
        
        # Month
        month_frame = ttk.Frame(input_row, style="Card.TFrame")
        month_frame.pack(side="left", padx=(0, 15))
        ttk.Label(month_frame, text="Month", style="Small.TLabel").pack(anchor="w")
        self.month_combo = ttk.Combobox(
            month_frame,
            textvariable=self.month_var,
            values=self.MONTH_NAMES,
            state="readonly",
            width=12,
            font=("Segoe UI", 11)
        )
        self.month_combo.pack()
        
        # Day
        day_frame = ttk.Frame(input_row, style="Card.TFrame")
        day_frame.pack(side="left", padx=(0, 15))
        ttk.Label(day_frame, text="Day", style="Small.TLabel").pack(anchor="w")
        self.day_spin = ttk.Spinbox(
            day_frame,
            textvariable=self.day_var,
            from_=1,
            to=31,
            width=5,
            font=("Segoe UI", 11)
        )
        self.day_spin.pack()
        
        # Year
        year_frame = ttk.Frame(input_row, style="Card.TFrame")
        year_frame.pack(side="left", padx=(0, 15))
        ttk.Label(year_frame, text="Year (1500-9999)", style="Small.TLabel").pack(anchor="w")
        self.year_spin = ttk.Spinbox(
            year_frame,
            textvariable=self.year_var,
            from_=self.MIN_YEAR,
            to=self.MAX_YEAR,
            width=7,
            font=("Segoe UI", 11)
        )
        self.year_spin.pack()
        
        # Buttons row
        btn_row = ttk.Frame(control_frame, style="Card.TFrame")
        btn_row.pack(fill="x")
        
        ttk.Button(
            btn_row,
            text="📆 Show Calendar",
            command=self._on_show_calendar,
            style="Primary.TButton"
        ).pack(side="left", padx=(0, 8))
        
        ttk.Button(
            btn_row,
            text="🔴 Highlight Date",
            command=self._on_highlight_date,
            style="Primary.TButton"
        ).pack(side="left", padx=(0, 8))
        
        ttk.Button(
            btn_row,
            text="📍 Today",
            command=self._show_today,
            style="Secondary.TButton"
        ).pack(side="left", padx=(0, 8))
        
        ttk.Button(
            btn_row,
            text="✖ Clear",
            command=self._clear_selection,
            style="Secondary.TButton"
        ).pack(side="left")
    
    def _build_calendar_display(self, parent: ttk.Frame) -> None:
        """Build the calendar display area."""
        display_frame = ttk.LabelFrame(
            parent,
            text="📅 Calendar View",
            style="Card.TLabelframe",
            padding="15"
        )
        display_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 10))
        display_frame.columnconfigure(0, weight=1)
        display_frame.rowconfigure(1, weight=1)
        
        # Month/Year header
        self.calendar_header = ttk.Label(
            display_frame,
            text="",
            style="Header.TLabel"
        )
        self.calendar_header.pack(pady=(0, 10))
        
        # Calendar text
        self.calendar_display = tk.Text(
            display_frame,
            font=("Consolas", 15),
            width=36,
            height=12,
            state="disabled",
            relief="flat",
            bg=self.COLORS["bg_card"],
            fg=self.COLORS["text_dark"],
            padx=15,
            pady=10,
            cursor="arrow",
            spacing1=4,
            spacing3=4
        )
        self.calendar_display.pack(fill="both", expand=True)
        
        # Text tags for styling
        self.calendar_display.tag_configure(
            "weekday",
            font=("Consolas", 15, "bold"),
            foreground=self.COLORS["primary"]
        )
        self.calendar_display.tag_configure(
            "highlight",
            background=self.COLORS["highlight"],
            foreground="white",
            font=("Consolas", 15, "bold")
        )
        self.calendar_display.tag_configure(
            "today",
            background=self.COLORS["today"],
            foreground="white"
        )
        self.calendar_display.tag_configure(
            "weekend",
            foreground=self.COLORS["weekend"]
        )
        
        # Info label
        self.info_label = ttk.Label(
            display_frame,
            text="💡 Double-click an event on the right to jump to its date",
            style="Small.TLabel"
        )
        self.info_label.pack(pady=(10, 0))
    
    def _build_quick_jump(self, parent: ttk.Frame) -> None:
        """Build quick jump buttons for famous dates."""
        quick_frame = ttk.LabelFrame(
            parent,
            text="⚡ Quick Jump to Famous Dates",
            style="Card.TLabelframe",
            padding="10"
        )
        quick_frame.grid(row=2, column=0, sticky="ew")
        
        famous_dates = [
            ("🌙 Moon Landing", 1969, 7, 20),
            ("💻 First Computer", 1946, 2, 14),
            ("🇺🇸 US Independence", 1776, 7, 4),
            ("🇮🇳 India Independence", 1947, 8, 15),
            ("🌐 WWW Launch", 1991, 8, 6),
            ("📱 iPhone Launch", 2007, 6, 29),
        ]
        
        for text, year, month, day in famous_dates:
            ttk.Button(
                quick_frame,
                text=text,
                command=lambda y=year, m=month, d=day: self._jump_to_date(y, m, d),
                style="Secondary.TButton"
            ).pack(side="left", padx=3, pady=3)
    
    def _build_right_panel(self) -> None:
        """Build the right panel with events explorer."""
        right_panel = ttk.Frame(self.root, style="Main.TFrame", padding="5")
        right_panel.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=5)
        right_panel.columnconfigure(0, weight=1)
        right_panel.rowconfigure(0, weight=1)
        
        self._build_events_explorer(right_panel)
    
    def _build_events_explorer(self, parent: ttk.Frame) -> None:
        """Build the events explorer section."""
        events_frame = ttk.LabelFrame(
            parent,
            text="🌍 Events Explorer",
            style="Card.TLabelframe",
            padding="15"
        )
        events_frame.grid(row=0, column=0, sticky="nsew")
        events_frame.columnconfigure(0, weight=1)
        events_frame.rowconfigure(4, weight=1)
        
        # Era selection
        era_frame = ttk.Frame(events_frame, style="Card.TFrame")
        era_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(era_frame, text="Select Time Era:", style="Small.TLabel").pack(anchor="w")
        self.era_combo = ttk.Combobox(
            era_frame,
            textvariable=self.era_var,
            values=EventsDatabase.get_eras(),
            state="readonly",
            font=("Segoe UI", 10)
        )
        self.era_combo.pack(fill="x", pady=(3, 0))
        self.era_combo.bind("<<ComboboxSelected>>", self._on_era_change)
        
        # Category selection
        cat_frame = ttk.Frame(events_frame, style="Card.TFrame")
        cat_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(cat_frame, text="Select Category:", style="Small.TLabel").pack(anchor="w")
        self.category_combo = ttk.Combobox(
            cat_frame,
            textvariable=self.category_var,
            state="readonly",
            font=("Segoe UI", 10)
        )
        self.category_combo.pack(fill="x", pady=(3, 0))
        self.category_combo.bind("<<ComboboxSelected>>", self._on_category_change)
        
        # Search
        search_frame = ttk.Frame(events_frame, style="Card.TFrame")
        search_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(search_frame, text="🔍 Search Events:", style="Small.TLabel").pack(anchor="w")
        
        search_input = ttk.Frame(search_frame, style="Card.TFrame")
        search_input.pack(fill="x", pady=(3, 0))
        
        self.search_entry = ttk.Entry(
            search_input,
            textvariable=self.search_var,
            font=("Segoe UI", 10)
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        ttk.Button(
            search_input,
            text="Search",
            command=self._on_search,
            style="Secondary.TButton"
        ).pack(side="right")
        
        # Instructions
        ttk.Label(
            events_frame,
            text="👆 Click: View details  •  👆👆 Double-click: Jump to date",
            style="Small.TLabel"
        ).pack(anchor="w", pady=(0, 5))
        
        # Events list
        list_frame = ttk.Frame(events_frame, style="Card.TFrame")
        list_frame.pack(fill="both", expand=True)
        
        self.events_list = tk.Listbox(
            list_frame,
            font=("Segoe UI", 10),
            height=14,
            selectmode="single",
            bg=self.COLORS["bg_card"],
            fg=self.COLORS["text_dark"],
            selectbackground=self.COLORS["primary"],
            selectforeground="white",
            borderwidth=1,
            relief="solid",
            activestyle="none"
        )
        self.events_list.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.events_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.events_list.configure(yscrollcommand=scrollbar.set)
        
        self.events_list.bind("<<ListboxSelect>>", self._on_event_select)
        self.events_list.bind("<Double-Button-1>", self._on_event_double_click)
        
        # Event details
        details_frame = ttk.LabelFrame(
            events_frame,
            text="📖 Event Details",
            style="Card.TLabelframe",
            padding="10"
        )
        details_frame.pack(fill="x", pady=(10, 0))
        
        self.details_text = tk.Text(
            details_frame,
            font=("Segoe UI", 10),
            height=5,
            wrap="word",
            bg=self.COLORS["bg_card"],
            fg=self.COLORS["text_dark"],
            relief="flat",
            state="disabled"
        )
        self.details_text.pack(fill="x")
        
        # Initial message
        self._set_details("👋 Welcome! Select a Time Era above to start exploring.\n\n"
                         "🏛️ Past: History from 1500 to 2010\n"
                         "📱 Present: Events from 2010-2020\n"
                         "🔮 Future: Predictions made in 2020")
    
    def _build_footer(self) -> None:
        """Build the application footer/status bar."""
        footer = ttk.Frame(self.root, style="Card.TFrame", padding="8")
        footer.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=(5, 10))
        
        self.status_label = ttk.Label(
            footer,
            text="Ready • Created by Tharun Ponnam • June 2020",
            style="Small.TLabel"
        )
        self.status_label.pack(side="left")
        
        event_count = EventsDatabase.get_total_event_count()
        ttk.Label(
            footer,
            text=f"📊 {event_count} events in database",
            style="Small.TLabel"
        ).pack(side="right")
    
    def _bind_events(self) -> None:
        """Bind keyboard and widget events."""
        self.root.bind("<Return>", lambda e: self._on_show_calendar())
        self.search_entry.bind("<Return>", lambda e: self._on_search())
        self.month_combo.bind("<<ComboboxSelected>>", lambda e: self._on_show_calendar())
    
    def _show_welcome(self) -> None:
        """Display welcome message on application start."""
        welcome = """🎉 Welcome to Perpetual Calendar!

📅 WHAT YOU CAN DO:
• View any date from 1500 to 9999
• Highlight specific dates on the calendar
• Explore 100+ historical events
• See future predictions (from 2020 perspective)

🚀 HOW TO START:
1. Select a date using the controls on the left
2. Click 'Show Calendar' or press Enter
3. Use 'Highlight Date' to mark a specific day
4. Browse events in the panel on the right
5. Double-click any event to jump to its date

⚡ QUICK TIP:
Use the 'Quick Jump' buttons for famous dates!

Enjoy exploring history! 🌍"""
        
        messagebox.showinfo("Welcome!", welcome)
    
    def _show_help(self) -> None:
        """Display help information."""
        help_text = """📅 PERPETUAL CALENDAR - HELP GUIDE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CALENDAR NAVIGATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Select month, day, year and click 'Show Calendar'
• Press Enter for quick display
• Click 'Highlight Date' to mark a specific day
• [N] = Your selected date
• (N) = Today's date
• Red numbers = Weekend days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVENTS EXPLORER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Select a Time Era (Past/Present/Future)
2. Choose a Category to filter events
3. Or use Search to find specific events

• Single-click: View event description
• Double-click: Jump to that date on calendar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEARCH TIPS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Try searching for:
• "moon" - Space events
• "computer" - Tech history
• "war" - Military history
• "AI" - Artificial Intelligence
• "quantum" - Quantum computing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ABOUT FUTURE PREDICTIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Future predictions were made in June 2020
and reflect the expectations at that time."""
        
        messagebox.showinfo("Help Guide", help_text)
    
    def _show_about(self) -> None:
        """Display about information."""
        about_text = """📅 Perpetual Calendar - Interactive Explorer

Version: 2.0.0
Created: June 2020
Author: Tharun Ponnam

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FEATURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Calendar range: 1500 to 9999
✓ Date highlighting
✓ 100+ historical events
✓ Past, Present, Future eras
✓ AI, Quantum, Space predictions
✓ Interactive event navigation
✓ Keyword search

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECHNOLOGY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Python 3.7+
• Tkinter GUI
• No external dependencies

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thank you for using Perpetual Calendar!

GitHub: github.com/tharun-ship-it
Email: tharunponnam007@gmail.com"""
        
        messagebox.showinfo("About", about_text)
    
    def _on_show_calendar(self) -> None:
        """Handle show calendar button click."""
        year = self._validate_year()
        if year is None:
            return
        
        month = self._get_month_number()
        self._render_calendar(year, month)
        self._update_status(f"Showing {self.MONTH_NAMES[month-1]} {year}")
    
    def _on_highlight_date(self) -> None:
        """Handle highlight date button click."""
        year = self._validate_year()
        if year is None:
            return
        
        month = self._get_month_number()
        day = self._validate_day(year, month)
        if day is None:
            return
        
        self.selected_date = (year, month, day)
        self._render_calendar(year, month)
        
        weekday = calendar.day_name[calendar.weekday(year, month, day)]
        date_str = f"{weekday}, {self.MONTH_NAMES[month-1]} {day}, {year}"
        self.info_label.config(text=f"📌 Highlighted: {date_str}")
        self._update_status(f"Date highlighted: {date_str}")
    
    def _show_today(self) -> None:
        """Navigate to today's date."""
        now = datetime.now()
        self.year_var.set(str(now.year))
        self.month_var.set(self.MONTH_NAMES[now.month - 1])
        self.day_var.set(str(now.day))
        self.selected_date = (now.year, now.month, now.day)
        self._render_calendar(now.year, now.month)
        self.info_label.config(text="📍 Today's date highlighted")
        self._update_status("Showing today's date")
    
    def _clear_selection(self) -> None:
        """Clear the date selection."""
        self.selected_date = None
        self._on_show_calendar()
        self.info_label.config(text="💡 Double-click an event on the right to jump to its date")
        self._update_status("Selection cleared")
    
    def _jump_to_date(self, year: int, month: int, day: int) -> None:
        """Jump to a specific date."""
        self.year_var.set(str(year))
        self.month_var.set(self.MONTH_NAMES[month - 1])
        self.day_var.set(str(day))
        self.selected_date = (year, month, day)
        self._render_calendar(year, month)
        
        weekday = calendar.day_name[calendar.weekday(year, month, day)]
        date_str = f"{weekday}, {self.MONTH_NAMES[month-1]} {day}, {year}"
        self.info_label.config(text=f"📌 {date_str}")
        self._update_status(f"Jumped to {date_str}")
    
    def _validate_year(self) -> Optional[int]:
        """Validate the year input."""
        try:
            year = int(self.year_var.get())
            if not self.MIN_YEAR <= year <= self.MAX_YEAR:
                raise ValueError()
            return year
        except ValueError:
            messagebox.showerror(
                "Invalid Year",
                f"Please enter a year between {self.MIN_YEAR} and {self.MAX_YEAR}."
            )
            return None
    
    def _validate_day(self, year: int, month: int) -> Optional[int]:
        """Validate the day input for the given month/year."""
        try:
            day = int(self.day_var.get())
            max_day = calendar.monthrange(year, month)[1]
            if not 1 <= day <= max_day:
                raise ValueError()
            return day
        except ValueError:
            max_day = calendar.monthrange(year, month)[1]
            messagebox.showerror(
                "Invalid Day",
                f"Please enter a day between 1 and {max_day} for {self.MONTH_NAMES[month-1]} {year}."
            )
            return None
    
    def _get_month_number(self) -> int:
        """Get the month number from the selected month name."""
        return self.MONTH_NAMES.index(self.month_var.get()) + 1
    
    def _render_calendar(self, year: int, month: int) -> None:
        """Render the calendar for the specified month and year."""
        self.calendar_header.config(text=f"{self.MONTH_NAMES[month-1]} {year}")
        
        cal = calendar.Calendar(calendar.MONDAY)
        weeks = cal.monthdayscalendar(year, month)
        
        self.calendar_display.config(state="normal")
        self.calendar_display.delete("1.0", tk.END)
        
        # Header row
        header = "  Mon  Tue  Wed  Thu  Fri  Sat  Sun"
        self.calendar_display.insert(tk.END, header + "\n", "weekday")
        self.calendar_display.insert(tk.END, "  " + "─" * 37 + "\n")
        
        today = datetime.now()
        
        for week in weeks:
            self.calendar_display.insert(tk.END, "  ")
            for i, day in enumerate(week):
                if day == 0:
                    self.calendar_display.insert(tk.END, "     ")
                else:
                    is_selected = (
                        self.selected_date is not None and
                        self.selected_date == (year, month, day)
                    )
                    is_today = (
                        year == today.year and
                        month == today.month and
                        day == today.day
                    )
                    is_weekend = i >= 5
                    
                    if is_selected:
                        self.calendar_display.insert(tk.END, f"[{day:2d}] ", "highlight")
                    elif is_today:
                        self.calendar_display.insert(tk.END, f"({day:2d}) ", "today")
                    elif is_weekend:
                        self.calendar_display.insert(tk.END, f" {day:2d}  ", "weekend")
                    else:
                        self.calendar_display.insert(tk.END, f" {day:2d}  ")
            
            self.calendar_display.insert(tk.END, "\n")
        
        # Legend
        self.calendar_display.insert(tk.END, "\n  ")
        self.calendar_display.insert(tk.END, "[N]", "highlight")
        self.calendar_display.insert(tk.END, " Selected  ")
        self.calendar_display.insert(tk.END, "(N)", "today")
        self.calendar_display.insert(tk.END, " Today  ")
        self.calendar_display.insert(tk.END, "N", "weekend")
        self.calendar_display.insert(tk.END, " Weekend")
        
        self.calendar_display.config(state="disabled")
    
    def _on_era_change(self, event=None) -> None:
        """Handle era selection change."""
        era = self.era_var.get()
        categories = EventsDatabase.get_categories(era)
        
        self.category_combo.config(values=categories)
        self.category_var.set("")
        
        # Load all events for this era
        self._load_era_events(era)
        self._set_details(f"📂 Showing all events from: {era}\n\n"
                         "Select a category to filter, or click any event below.")
    
    def _on_category_change(self, event=None) -> None:
        """Handle category selection change."""
        era = self.era_var.get()
        category = self.category_var.get()
        
        if era and category:
            self._load_category_events(era, category)
            self._set_details(f"📂 {category}\n\n"
                             "Click an event to see details.\n"
                             "Double-click to jump to that date.")
    
    def _load_era_events(self, era: str) -> None:
        """Load all events for an era into the listbox."""
        self.events_list.delete(0, tk.END)
        self.current_events = EventsDatabase.get_all_events_in_era(era)
        
        for date, title, _ in self.current_events:
            self.events_list.insert(tk.END, f"📌 {date}: {title}")
    
    def _load_category_events(self, era: str, category: str) -> None:
        """Load events for a specific category into the listbox."""
        self.events_list.delete(0, tk.END)
        self.current_events = EventsDatabase.get_events_by_category(era, category)
        
        for date, title, _ in self.current_events:
            self.events_list.insert(tk.END, f"📌 {date}: {title}")
    
    def _on_search(self) -> None:
        """Handle search button click."""
        keyword = self.search_var.get().strip()
        if not keyword:
            messagebox.showinfo(
                "Search",
                "Please enter a search term.\n\n"
                "Try: 'moon', 'computer', 'war', 'AI', 'quantum', 'space'"
            )
            return
        
        self.events_list.delete(0, tk.END)
        self.current_events = EventsDatabase.search_events(keyword)
        
        if not self.current_events:
            self.events_list.insert(tk.END, "❌ No events found")
            self._set_details(f"No events found for '{keyword}'.\n\n"
                             "Try different keywords:\n"
                             "• moon, space, mars\n"
                             "• computer, AI, quantum\n"
                             "• war, revolution, independence")
        else:
            for date, title, _ in self.current_events:
                self.events_list.insert(tk.END, f"🔍 {date}: {title}")
            self._set_details(f"Found {len(self.current_events)} event(s) for '{keyword}'.\n\n"
                             "Click an event to see details.")
        
        self._update_status(f"Search: {len(self.current_events)} results for '{keyword}'")
    
    def _on_event_select(self, event=None) -> None:
        """Handle event selection in listbox."""
        selection = self.events_list.curselection()
        if not selection or not self.current_events:
            return
        
        idx = selection[0]
        if idx < len(self.current_events):
            date_str, title, description = self.current_events[idx]
            
            parts = date_str.split("-")
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            weekday = calendar.day_name[calendar.weekday(year, month, day)]
            
            details = f"📅 {title}\n\n"
            details += f"📆 {weekday}, {self.MONTH_NAMES[month-1]} {day}, {year}\n\n"
            details += f"📖 {description}\n\n"
            details += "💡 Double-click to view this date on calendar"
            
            self._set_details(details)
    
    def _on_event_double_click(self, event=None) -> None:
        """Handle double-click on event to navigate to its date."""
        selection = self.events_list.curselection()
        if not selection or not self.current_events:
            return
        
        idx = selection[0]
        if idx < len(self.current_events):
            date_str, title, _ = self.current_events[idx]
            
            parts = date_str.split("-")
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            
            self._jump_to_date(year, month, day)
            
            weekday = calendar.day_name[calendar.weekday(year, month, day)]
            self.info_label.config(text=f"📌 {title} - {weekday}, {self.MONTH_NAMES[month-1]} {day}, {year}")
    
    def _set_details(self, text: str) -> None:
        """Set the event details text."""
        self.details_text.config(state="normal")
        self.details_text.delete("1.0", tk.END)
        self.details_text.insert("1.0", text)
        self.details_text.config(state="disabled")
    
    def _update_status(self, message: str) -> None:
        """Update the status bar message."""
        self.status_label.config(text=f"{message} • Created by Tharun Ponnam • June 2020")


def main() -> None:
    """Application entry point."""
    root = tk.Tk()
    app = PerpetualCalendar(root)
    root.mainloop()


if __name__ == "__main__":
    main()
