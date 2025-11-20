# 🛠 BikeBike Development Log

This document contains the complete development history and all features implemented during the creation of BikeBike.

## 📋 Project Overview

**Goal:** Create an iOS cycling app that tracks speed using the accelerometer and provides gamified challenges.

## 🗓 Development Timeline

### Phase 1: Initial Setup
- Created basic iOS app structure
- Set up SwiftUI views
- Implemented deployment target (iOS 16.0)

### Phase 2: Speed Tracking
**Initial Approach:** GPS-based tracking
- Implemented CoreLocation for speed
- Used GPS speed data

**Final Approach:** Accelerometer-based tracking
- Switched to CoreMotion
- Implemented acceleration integration
- Added friction/decay simulation
- More responsive and works indoors

### Phase 3: UI/UX Design

#### Speed Display
- Large 120pt bold text at top
- "km/h" label below
- Real-time updates
- Speed-based color changes

#### Background
- Started with gradient (black to dark blue)
- Changed to pure black per user request
- Clean, minimal design

#### Bike Animation
- Initial: Custom-drawn bike with wheels
- Updated: User-provided SVG asset
- Features:
  - Tilt animation based on speed
  - Bounce effect (faster at higher speeds)
  - Shake effect at 20+ km/h
  - Speed-based scaling
  - Color changes matching speed

#### Scenery Elements
- Cloud lines in sky (parallax scrolling)
- Ground line below bike
- Initially had lamp posts (later removed)
- Minimalist design approach

### Phase 4: Challenge System

#### Challenge Types Implemented

1. **Wiggle for Coins**
   - Detects lateral phone movement
   - Threshold: 2.5g lateral force
   - Cooldown: 0.3s between detections
   - Target: 10-20 wiggles

2. **Speed Burst**
   - Reach target speeds: 15, 20, 25, or 30 km/h
   - Instant completion on reaching speed

3. **Acceleration Combo**
   - Chain accelerations (speed increase of 2+ km/h)
   - 3-second window to maintain combo
   - 5-second timeout resets combo
   - Target: 5-10 combos

4. **Smooth Rider**
   - Maintain speed variance < 1.5 km/h
   - Minimum speed: 10 km/h
   - Duration: 15-30 seconds

5. **Obstacle Dodge**
   - Visual obstacles spawn on screen
   - Three types: Cones, Rocks, Barriers
   - Three lanes (left, center, right)
   - Swipe to dodge
   - Collision detection
   - Target: 3-8 dodges

6. **Time Trial**
   - Stay above 15 km/h
   - Duration: 30 seconds

7. **Trick System**
   - Detects vertical movement (jumps/wheelies)
   - Threshold: 0.8g vertical change
   - Requires velocity > 5 m/s
   - Cooldown: 1.0s
   - Target: 3-6 tricks

8. **Speed Challenge**
   - Maintain 20+ km/h
   - Duration: 10-20 seconds
   - Timer resets if speed drops

9. **Ghost Race**
   - Simulated distance tracking
   - Target: 100m ahead of ghost

10. **Virtual Race**
    - Race to distance: 50, 100, or 150m
    - Distance calculated from speed × time

#### Challenge UI

**Challenge Box:**
- Position: Top of screen (above speed)
- Content:
  - Title (left) + Total coins (right)
  - Description
  - Animated progress bar (green to blue gradient)
  - Current progress text
  - Coin reward amount
- Size: Compact (14pt title, 11pt description)
- Padding: 12pt
- Border: 1.5pt white stroke
- Background: Black with 60% opacity

**Completion Popup:**
- Center screen overlay
- Success checkmark icon
- Challenge name
- Coin reward with icon
- Green/blue/purple gradient border
- Scale animation on appear
- Auto-dismiss after 2.5 seconds

#### Coin System
- Random rewards: 20-120 coins per challenge
- Displayed in challenge header
- Persistent accumulation
- Yellow coin icon with count

### Phase 5: Motion Detection

#### Accelerometer Implementation
```swift
- Update interval: 0.1s (10Hz)
- Shake detection: Lateral force > 2.5g
- Trick detection: Vertical change > 0.8g
- Speed calculation: Integration with decay
```

#### Speed Calculation Algorithm
```
1. Get acceleration (x, y, z)
2. Calculate magnitude: sqrt(x² + y² + z²) - 1g
3. Apply noise threshold: > 0.1g
4. Convert to m/s²: magnitude × 9.81
5. Integrate: velocity += acceleration × deltaTime
6. Apply decay: velocity × 0.98
7. Convert to km/h: velocity × 3.6
```

### Phase 6: Obstacle System

#### Obstacle Rendering
- Three distinct types with unique visuals
- SVG-style custom shapes
- Shadow effects for depth

#### Obstacle Spawning
- Timer: Every 1.5 seconds
- Only when speed > 5 km/h
- Random lane selection
- Random type selection
- Start position: Above screen

#### Obstacle Animation
- Movement: 5 pixels per 0.05s tick
- Collision zone: yPosition 50-100
- Auto-cleanup: Remove when yPosition > 200

#### Dodge Mechanics
- Swipe gesture detection
- Lane switching: -80px, 0px, +80px
- Spring animation (0.3s response)
- Auto-return to center
- Collision distance: 40px threshold

### Phase 7: App Icon

#### Design
- White background
- Black bicycle SVG centered
- 150px padding on all sides
- 1024x1024 resolution

#### Implementation
- Created HTML generator tool
- Canvas-based rendering
- One-click download
- Ready for all iOS icon slots

## 🎨 Design Decisions

### Why Accelerometer Instead of GPS?
1. Works indoors/simulator
2. Faster response time
3. No location permissions needed
4. More privacy-friendly
5. Better for testing

### Why Pure Black Background?
- User preference
- Better OLED display efficiency
- Cleaner aesthetic
- Better contrast for colors
- Less distracting

### Why Challenge at Top?
- First thing user sees
- More prominent position
- Better visibility while cycling
- Integrated coin display
- Speed remains visible below

### Why Random Coin Rewards?
- Adds excitement/unpredictability
- Encourages replay
- Prevents monotony
- Balances difficulty with reward

## 🔧 Technical Challenges & Solutions

### Challenge 1: Speed Tracking Accuracy
**Problem:** Accelerometer drift
**Solution:** Applied decay factor (0.98) to simulate friction

### Challenge 2: Array Mutation
**Problem:** Can't directly mutate struct in array
**Solution:** Create copy, modify, replace: `obstacles[index] = updatedObstacle`

### Challenge 3: iOS Version Compatibility
**Problem:** `onChange(of:initial:_:)` requires iOS 17
**Solution:** Use iOS 16 compatible version: `onChange(of:) { _ in }`

### Challenge 4: Challenge Progression
**Problem:** Timer-based challenges resetting
**Solution:** Separate timer tracking for each challenge type

### Challenge 5: Collision Detection
**Problem:** Obstacles disappearing too fast
**Solution:** Window-based checking (yPosition 50-100)

## 📊 Code Statistics

- **Total Files Created:** 7 Swift files + 1 HTML tool
- **Lines of Code:** ~1000+ lines
- **Challenge Types:** 10 unique challenges
- **Obstacle Types:** 3 visual types
- **Animation States:** 5 different bike animations

## 🎯 User Requests Implemented

1. ✅ iOS app with accelerometer speed tracking
2. ✅ Large bold speed display at top
3. ✅ Animated bike in center responding to speed
4. ✅ Line below bike as road/path
5. ✅ Scrolling scenery elements
6. ✅ Changed to use SVG bike asset
7. ✅ Removed road/dashed lines
8. ✅ Used reference images as inspiration
9. ✅ Removed lamp posts
10. ✅ Moved challenge to top of speed
11. ✅ Integrated coins into challenge display
12. ✅ Reduced challenge and coin display size
13. ✅ Changed to accelerometer (from GPS)
14. ✅ Auto-start tracking on app open
15. ✅ Implemented 13 different challenge types
16. ✅ Challenge box below speed with progress
17. ✅ Random coin rewards per challenge
18. ✅ Completion popup animation
19. ✅ Pure black background
20. ✅ App icon with bicycle on white
21. ✅ Visual obstacles for dodge challenge

## 🚀 Future Enhancement Ideas

- Persistent storage (save coins/progress)
- Leaderboards (local or online)
- More challenge types
- Customizable bike skins
- Sound effects
- Haptic feedback
- Route tracking/history
- Statistics dashboard
- Social sharing
- Achievements system
- Weather integration
- Time of day themes
- Multiplayer races
- Power-ups/boosts
- Season pass/events

## 📝 Notes

- Built with iOS 16.0 minimum deployment
- Requires physical device for accelerometer
- Best experience while actually cycling
- Smooth animations with spring physics
- Efficient battery usage
- No backend required
- Fully offline capable

---

**Generated with Claude Code 🤖**
