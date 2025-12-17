# AI Documentation Website - Development Conversation Log

## Project Overview
An interactive website for showcasing AI experiments from the CIID Interaction Design Program, built collaboratively with Claude Code.

---

## Conversation Summary

### Initial Setup

**User Request:** Set up a simple static website that others on the local network can access.

**Implementation:**
- Created `index.html` with basic structure
- Created `server.py` - Python HTTP server with no-cache headers
- Server prints local network IP address for easy sharing

---

### Homepage Design

**User Request:** Create a clean page with:
- Header: "AI experimentations" in Press Start 2P font (bold)
- Description text in Courier New font

**Implementation:**
- Added Google Fonts (Press Start 2P)
- Centered layout with hero section
- Clean, minimal styling with gray background

---

### Content Updates

**User Request:** Update description to introduce Nikhil from CIID Interaction Design Program

**Final Description:**
"Hi, I'm Nikhil, currently enrolled in the Interaction Design Program at CIID. This website showcases my AI experimentations from this week's course: AI Experiments. Week 1 faculties."

---

### Experiment Archive Section

**User Request:** Add a second fold with:
- Heading: "The Experiment Archive"
- Two dropdowns: Week selector (Week 1-2) and Day selector (Monday-Friday)
- Subtitle: "Pick a week and day to dive into the experiments"

**Implementation:**
- Created experiments section with full viewport height
- Added dropdown selectors with hover effects
- Content display section that appears when selections are made

---

### Document Management System

**User Request:** Integrate markdown documents from `docs/` folder
- File naming pattern: `day-morning/afternoon-week#.md`
- Show morning/afternoon sections separately with collapsible details

**Implementation:**
- Created `docsMapping` object to track files
- Added collapsible details/summary elements for morning/afternoon
- Implemented file loading via fetch API
- Added scrollable windows (400px max-height) for content

**Example Files:**
- Tuesday Week 1: afternoon only
- Wednesday Week 1: both morning and afternoon

---

### Interactive Features

**User Request:** Make the main heading color change based on cursor position in the first fold

**Implementation:**
- Added mousemove event listener to hero section
- HSL color calculation based on cursor X/Y position
- Horizontal movement: changes hue (rainbow spectrum)
- Vertical movement: changes saturation (70-95% for vibrant colors)
- Transition speed: 0.15s for responsive feel
- Resets to default (#333) when cursor leaves

---

### Footer Development

**User Request:** Create footer with:
- "nikhil sajjan" in heading font (30% bigger, split on two lines)
- Connect section with social links (left side)
- Back to top button (right side)
- Line above footer

**Implementation:**
- Three-section layout with vertical divider
- Social links: Personal Website, LinkedIn, Instagram (underlined, no icons)
- Back to top button: square with Material Symbols arrow icon
- Button text changed to "go to top" in small font
- Smooth scroll functionality

**Styling:**
- No background colors
- 3px border-top
- Dark text on light background
- Hover effects: darken on hover

---

### Dark Mode Feature

**User Request:** Add dark/light mode toggle button

**Implementation:**
- Toggle button positioned in bottom-left corner of footer
- Comprehensive dark mode styling:
  - Background: #1a1a1a, #252525
  - Text: #e0e0e0, #b0b0b0
  - Borders: #555
- LocalStorage integration to remember preference
- Button text changes: "dark mode" ↔ "light mode"

**Button Styling:**
- Matches "go to top" button style
- Font: Courier New, 0.75rem
- Font-weight: normal
- Border: 2px solid
- Hover: inverts colors

---

### Git Repository Setup

**User Request:** Push code to GitHub

**Implementation:**
1. Created `.gitignore` file (macOS, Python, IDEs, temp files)
2. Initialized fresh git repository in `/personal` directory
3. Added all project files:
   - index.html
   - server.py
   - docs/ folder (3 markdown files)
   - week1-wednesday.md
4. Created initial commit with descriptive message
5. Created GitHub repository: `ai-documentation-website`
6. Pushed to: https://github.com/nikhilsajjan/ai-documentation-website

**Repository Details:**
- Owner: nikhilsajjan
- Name: ai-documentation-website
- Visibility: Public
- Description: "Interactive website showcasing AI experiments from CIID Interaction Design Program"

---

## Technical Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Fonts:**
  - Press Start 2P (Google Fonts)
  - Courier New (system font)
  - Material Symbols Outlined (icons)
- **Backend:** Python HTTP Server (built-in)
- **Version Control:** Git + GitHub

---

## Key Features

1. **Interactive Color-Changing Header**
   - HSL color manipulation based on cursor position
   - Smooth transitions (0.15s)

2. **Experiment Archive**
   - Week/Day dropdown selectors
   - Dynamic content loading from markdown files
   - Morning/Afternoon collapsible sections
   - Scrollable content windows (400px max)

3. **Dark Mode Toggle**
   - Persistent preference (localStorage)
   - Comprehensive styling across all elements
   - Smooth transitions

4. **Responsive Design**
   - Mobile-friendly layout
   - Adaptive footer (stacks vertically on mobile)
   - Flexible typography

5. **Python Server**
   - No-cache headers for instant updates
   - Local network access
   - Port 8000

---

## File Structure

```
personal/
├── .git/
├── .gitignore
├── index.html              # Main website file
├── server.py               # Python HTTP server
├── week1-wednesday.md      # Legacy experiment doc
├── docs/
│   ├── Tuesday-afternoon-week 1 .md
│   ├── Wednesday-morning-week 1.md
│   └── wednesday-afternoon-week 1 .md
└── conversation-log.md     # This file
```

---

## Running the Server

```bash
python3 server.py
```

The server will display:
- Local access: http://localhost:8000
- Network access: http://[your-local-ip]:8000

---

## Future Updates

To add new experiments:
1. Add markdown files to `docs/` folder
2. Update `docsMapping` in index.html (around line 292)
3. Format: `{day}-{morning/afternoon}-week {#}.md`

Example:
```javascript
monday: {
    morning: "docs/monday-morning-week1.md"
}
```

---

## GitHub Pages Deployment (Optional)

1. Go to repository settings
2. Navigate to "Pages"
3. Select "main" branch as source
4. Site will be live at: https://nikhilsajjan.github.io/ai-documentation-website/

---

## Making Future Updates

```bash
# Make your changes
git add .
git commit -m "Description of changes"
git push origin main
```

---

## Development Notes

- All buttons use consistent styling (font-weight: normal, 0.75rem)
- Material Symbols requires internet connection for icons
- Server runs on port 8000 (configurable in server.py)
- Dark mode preference stored in browser localStorage
- Content files loaded via fetch API (requires running server)

---

*Created: November 20, 2024*
*Project: AI Experimentations Documentation Website*
*Developer: Nikhil Sajjan*
*Built with: Claude Code*
