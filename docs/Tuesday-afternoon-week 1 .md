<div style="display: flex; gap: 1rem; margin-bottom: 2rem; flex-wrap: wrap;">
    <img src="docs/IMG_9687.webp" alt="Drum Loop Recorder" style="width: calc(33.333% - 0.67rem); min-width: 200px; border: 3px solid #000; flex: 1;">
    <div style="width: calc(33.333% - 0.67rem); min-width: 200px; border: 3px solid #000; background-color: #f0f0f0; display: flex; align-items: center; justify-content: center; color: #999; flex: 1; aspect-ratio: 4/3;">Image 2</div>
    <div style="width: calc(33.333% - 0.67rem); min-width: 200px; border: 3px solid #000; background-color: #f0f0f0; display: flex; align-items: center; justify-content: center; color: #999; flex: 1; aspect-ratio: 4/3;">Image 3</div>
</div>

# Drum Loop Recorder - Complete Project Documentation

## Project Overview

A hardware-controlled drum loop recorder that combines an Arduino controller with a macOS application. Users can record and play back up to 4 audio loops using physical buttons connected to Arduino.

**Created:** November 18, 2025
**Platform:** macOS (SwiftUI)
**Hardware:** Arduino + 5 buttons
**Language:** Swift, Arduino C++

---

## Architecture

### System Design

```
┌─────────────────┐         USB Serial        ┌──────────────────┐
│                 │◄─────────────────────────►│                  │
│    Arduino      │    Commands (9600 baud)   │   Mac App        │
│   Controller    │                            │   (SwiftUI)      │
│                 │                            │                  │
│  5 Buttons      │                            │  Audio Engine    │
│  (Pins 1-5)     │                            │  Recording       │
│                 │                            │  Playback        │
└─────────────────┘                            └──────────────────┘
                                                        │
                                                        ├─► Mac Microphone (Input)
                                                        └─► Mac Speakers (Output)
```

### Component Overview

**Arduino Side:**
- 5 push buttons connected to pins 1-5
- Serial communication at 9600 baud
- Sends commands: RECORD, PLAY1, PLAY2, PLAY3, PLAY4

**Mac Side:**
- Serial port manager for Arduino communication
- Shared audio engine for recording and playback
- 4 independent loop slots
- Real-time audio processing

---

## Development Journey

### Phase 1: Initial Setup
**Goal:** Create basic Mac app and Arduino controller

**Tasks Completed:**
1. Created Xcode project for macOS app
2. Wrote Arduino sketch for button reading
3. Implemented serial communication protocol
4. Created basic SwiftUI interface

### Phase 2: Serial Communication
**Goal:** Get Arduino talking to Mac app

**Challenges:**
- App Sandbox blocking serial port access
- Permission errors (errno: 1 - Operation not permitted)
- Line parsing issues with \r\n endings

**Solutions:**
1. Disabled App Sandbox in Xcode project settings
2. Added detailed error logging with errno codes
3. Fixed line parsing to handle Windows-style line endings (\r\n)
4. Used `CharacterSet.newlines` for robust parsing

### Phase 3: Audio System
**Goal:** Record and play back audio loops

**Challenges:**
- Audio engine conflicts (two engines competing)
- HAL audio overload errors
- Channel mismatch between recording and playback
- Format incompatibility

**Solutions:**
1. Created shared `AudioEngineManager` singleton
2. Single audio engine for both recording and playback
3. Dynamic format matching for player nodes
4. Increased buffer size from 4096 to 8192 for stability

### Phase 4: Recording Implementation
**Challenges:**
- Recording not starting (timing bug)
- `isRecording` flag set after tap installation
- No microphone permission handling

**Solutions:**
1. Set `isRecording = true` BEFORE installing audio tap
2. Added microphone permission request
3. Added NSMicrophoneUsageDescription to Info.plist
4. Comprehensive debug logging at every step

### Phase 5: Features & Polish
**Added:**
- 4-second auto-stop timer for recordings
- Reset/clear buttons for each loop
- Visual feedback (waveform icons, status indicators)
- Auto-save when timer expires
- Loop cycling (automatically moves to next slot)

---

## File Structure

```
drum.loop/
├── README.md                           # User guide
├── FIX_SERIAL_PORT.md                  # Troubleshooting serial issues
├── WIRING.txt                          # Hardware wiring diagram
├── XCODE_SETUP.md                      # Xcode configuration guide
├── PROJECT_DOCUMENTATION.md            # This file
│
├── arduino_controller/
│   └── arduino_controller.ino          # Arduino sketch
│
└── drum.loop.code/
    ├── drum.loop.code.xcodeproj        # Xcode project
    └── drum.loop.code/
        ├── drum_loop_codeApp.swift     # App entry point
        ├── ContentView.swift            # Main UI and logic
        ├── AudioEngineManager.swift     # Shared audio engine
        ├── AudioRecorder.swift          # Recording functionality
        ├── AudioPlayer.swift            # Playback functionality
        └── SerialPortManager.swift      # Arduino communication
```

---

## Component Details

### 1. Arduino Controller (`arduino_controller.ino`)

**Purpose:** Read button states and send commands via serial

**Pin Configuration:**
- Pin 1: Record button
- Pin 2: Play Loop 1
- Pin 3: Play Loop 2
- Pin 4: Play Loop 3
- Pin 5: Play Loop 4

**Features:**
- Button debouncing (50ms)
- Internal pull-up resistors
- LED feedback on button press
- Serial output at 9600 baud

**Commands Sent:**
```
RECORD\r\n    - When pin 1 button pressed
PLAY1\r\n     - When pin 2 button pressed
PLAY2\r\n     - When pin 3 button pressed
PLAY3\r\n     - When pin 4 button pressed
PLAY4\r\n     - When pin 5 button pressed
```

### 2. SerialPortManager.swift

**Purpose:** Handle serial communication with Arduino

**Key Features:**
- Auto-scan for USB serial ports
- Configures port: 9600 baud, 8N1, raw mode
- Background thread for reading data
- Robust line parsing (handles \r\n, \n, \r)
- Detailed error reporting with errno codes

**Important Functions:**
- `scanForPorts()` - Find available serial devices
- `connect(to:)` - Open and configure serial port
- `disconnect()` - Close port and cleanup
- `readSerialData()` - Background thread reading loop

**Debug Output:**
- Port scanning results
- Connection status
- Bytes received (hex dump)
- Parsed commands
- Error messages with suggestions

### 3. AudioEngineManager.swift

**Purpose:** Provide shared audio engine for recording and playback

**Why It Exists:**
Originally, AudioRecorder and AudioPlayer each had their own audio engine, causing:
- Resource conflicts
- HAL audio overload errors
- Poor performance

**Solution:**
Single shared `AVAudioEngine` instance that:
- Starts once and stays running
- Used by both recorder and player
- Better performance and stability

### 4. AudioRecorder.swift

**Purpose:** Record audio from Mac's internal microphone

**Key Features:**
- Records to 4 separate slots
- 8192 sample buffer size (stability)
- Auto-stop timer (4 seconds)
- Audio tap on shared engine's input node
- Buffer copying for reliable storage

**Recording Flow:**
1. Clear previous recording in slot
2. Remove existing audio tap
3. Set `isRecording = true`
4. Install tap on input node
5. Start 4-second timer
6. Capture and copy audio buffers
7. Auto-stop or manual stop

**Functions:**
- `startRecording(slot:)` - Begin recording
- `stopRecording()` - End recording, cancel timer
- `getRecordedBuffers(forSlot:)` - Retrieve buffers
- `hasRecording(forSlot:)` - Check if slot has audio
- `clearRecording(forSlot:)` - Delete loop

### 5. AudioPlayer.swift

**Purpose:** Play back recorded loops with mixing

**Key Features:**
- 4 independent player nodes
- Dynamic format matching
- Seamless looping
- Multiple simultaneous playback (mixing)
- Auto-reconnection with correct format

**Playback Flow:**
1. Get recorded buffers for slot
2. Connect player node with buffer's format
3. Schedule all buffers
4. Add completion handler for looping
5. Start playback
6. Re-schedule on completion (infinite loop)

**Functions:**
- `setLoop(slot:buffers:)` - Load loop into slot
- `togglePlayback(slot:)` - Start/stop playback
- `clearLoop(slot:)` - Remove loop and disconnect node
- `stopAll()` - Stop all playback

### 6. ContentView.swift

**Purpose:** Main UI and coordination logic

**UI Components:**
- Arduino connection section
  - Port scanner and selector
  - Connect/disconnect button
  - Connection status indicator

- Recording status section
  - Shows current recording state
  - Displays which slot is recording

- Loop slots section (4 slots)
  - Loop number and waveform icon
  - Status: Empty/Ready/Playing
  - Clear button (trash icon)

**Key Functions:**
- `handleArduinoCommand()` - Process serial commands
- `handleRecord()` - Toggle recording
- `handlePlay(slot:)` - Toggle playback
- `handleClearLoop(slot:)` - Delete loop
- `saveRecordedLoop(slot:)` - Save buffers to player

**State Management:**
- `@StateObject` for managers (serial, recorder, player)
- `@Published` properties trigger UI updates
- `onChange` modifiers for reactive behavior

---

## Features

### ✅ Implemented Features

1. **Hardware Control**
   - Physical button interface via Arduino
   - USB serial communication
   - Real-time command processing

2. **Recording**
   - Record from Mac's internal microphone
   - Up to 4 independent loop slots
   - 4-second maximum recording length
   - Auto-stop timer
   - Manual stop support

3. **Playback**
   - Play any or all loops simultaneously
   - Seamless looping
   - Toggle play/stop per loop
   - Real-time audio mixing

4. **User Interface**
   - Connection status indicator
   - Recording status display
   - Loop slot status (Empty/Ready/Playing)
   - Clear button for each loop
   - Visual feedback (colors, icons)

5. **Error Handling**
   - Microphone permission checks
   - Serial port error diagnostics
   - Audio format mismatch handling
   - Comprehensive debug logging

### 🎛️ User Workflow

**Setup:**
1. Connect Arduino via USB
2. Launch Mac app
3. Scan for ports
4. Select Arduino port
5. Click Connect

**Recording a Loop:**
1. Press RECORD button (Pin 1)
2. Make sounds into microphone
3. Press RECORD again OR wait 4 seconds
4. Loop auto-saves to next available slot

**Playing Loops:**
1. Press PLAY1-4 buttons (Pins 2-5)
2. Loops play simultaneously (mixed)
3. Press again to stop playback

**Clearing a Loop:**
1. Click trash icon next to loop in UI
2. Slot becomes available for new recording

---

## Technical Specifications

### Audio Configuration
- **Sample Rate:** 48000 Hz (default system rate)
- **Format:** Float32, deinterleaved
- **Channels:** 2 (stereo) or 1 (mono) - auto-detected
- **Buffer Size:** 8192 samples
- **Max Recording:** 4 seconds per loop
- **Loops:** 4 independent slots

### Serial Communication
- **Baud Rate:** 9600
- **Data Bits:** 8
- **Parity:** None
- **Stop Bits:** 1
- **Flow Control:** None
- **Line Ending:** \r\n (Windows style)

### System Requirements
- **macOS:** 12.0 or later
- **Xcode:** 14.0 or later
- **Arduino:** Uno, Nano, or compatible
- **USB:** Type-A or Type-C with adapter
- **Microphone:** Built-in or external

---

## Build Configuration

### Xcode Settings

**Critical Settings:**
```
ENABLE_APP_SANDBOX = NO
ENABLE_HARDENED_RUNTIME = YES
GENERATE_INFOPLIST_FILE = YES
INFOPLIST_KEY_NSMicrophoneUsageDescription = "This app needs microphone access to record audio loops."
```

**Why App Sandbox is Disabled:**
- macOS App Sandbox blocks access to `/dev/cu.usbmodem*` devices
- Serial port access requires full system permissions
- Safe for personal development use

### Dependencies
- **AVFoundation** - Audio recording and playback
- **IOKit** - Serial port access
- **Combine** - Reactive state management
- **SwiftUI** - User interface

---

## Troubleshooting Guide

### Problem: "Operation not permitted (errno: 1)"

**Cause:** App Sandbox is enabled

**Solution:**
1. In Xcode: Project → Target → Signing & Capabilities
2. Remove "App Sandbox" capability
3. Clean build: Cmd+Shift+K
4. Rebuild: Cmd+R

### Problem: No serial ports found

**Causes:**
- Arduino not connected
- Wrong USB cable (charge-only cable)
- Driver not installed

**Solutions:**
- Check Arduino is powered (LED on)
- Try different USB cable
- Replug Arduino
- Install CH340/CP2102 drivers if needed

### Problem: Commands not received

**Debug Steps:**
1. Check console for "📖 Read X bytes from serial port"
2. If no bytes, check Arduino is running sketch
3. Open Arduino Serial Monitor - see commands?
4. Close Serial Monitor (port can't be shared)
5. Try reconnecting in Mac app

### Problem: No audio recording

**Checks:**
- Microphone permission granted?
  - System Settings → Privacy & Security → Microphone
- See "🎤 Starting recording" in console?
- See "📊 Recorded X buffers" messages?
- Making sounds into correct microphone?

### Problem: Audio format mismatch

**Error:** `_outputFormat.channelCount == buffer.format.channelCount`

**Cause:** Fixed in current version

**Explanation:** Player nodes now dynamically connect with recorded audio format

### Problem: HAL audio overload

**Error:** `HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload`

**Cause:** Fixed in current version

**Explanation:** Now using single shared audio engine instead of multiple competing engines

---

## Debug Output Examples

### Successful Connection
```
Scanning for serial ports...
  Found: /dev/cu.usbmodem11301
  Total ports found: 1
Attempting to open port: /dev/cu.usbmodem11301
Starting serial read thread...
📖 Serial read thread started
✅ Connected to /dev/cu.usbmodem11301
Waiting for data from Arduino...
```

### Successful Recording
```
📨 Received command: 'RECORD'
  → Handling RECORD command
🎙️ handleRecord() called - isRecording: false
  Starting recording to slot 1...
🎤 Starting recording to slot 1...
  Input format: <AVAudioFormat 0x...: 2 ch, 48000 Hz, Float32>
✅ Recording started successfully! (will auto-stop in 4.0 seconds)
  📊 Recorded 50 buffers...
  📊 Recorded 100 buffers...
```

### Auto-Stop Timer
```
⏰ Auto-stopping recording after 4.0 seconds
⏹️ Stopping recording...
✅ Stopped recording. Slot 1 has 216 buffers
  📊 Estimated duration: ~4.0 seconds
📦 Auto-saving loop from 4-second timer...
  Saving 216 buffers to player slot 1
🔊 Loop 1 loaded with 216 buffers
   Format: <AVAudioFormat 0x...: 2 ch, 48000 Hz, Float32>
```

### Successful Playback
```
📨 Received command: 'PLAY1'
  → Handling PLAY1 command
Started playback for slot 1
```

---

## Known Issues & Limitations

### Current Limitations

1. **Loops are not persistent**
   - Stored in memory only
   - Lost when app closes
   - Future: Add save/load functionality

2. **Fixed 4-second limit**
   - Hardcoded in AudioRecorder
   - Future: Make configurable

3. **No visual waveform**
   - Only status indicators
   - Future: Add waveform visualization

4. **No editing**
   - Can't trim or edit loops
   - Only clear and re-record
   - Future: Add basic editing

5. **No effects**
   - Raw audio playback only
   - Future: Add reverb, delay, filters

### Known Warnings (Safe to Ignore)

1. **"Unable to obtain a task name port right for pid 606"**
   - Audio HAL trying to inspect other processes
   - Blocked by System Integrity Protection
   - Does not affect functionality

2. **"AddInstanceForFactory: No factory registered"**
   - Audio component factory message
   - Harmless system warning
   - Does not affect functionality

---

## Future Enhancements

### High Priority
- [ ] Save/load loops to disk
- [ ] Configurable recording length
- [ ] Volume control per loop
- [ ] Master volume control

### Medium Priority
- [ ] Visual waveform display
- [ ] Loop length quantization
- [ ] Metronome/click track
- [ ] Undo last recording

### Low Priority
- [ ] Audio effects (reverb, delay, EQ)
- [ ] Export loops as audio files
- [ ] MIDI sync
- [ ] Multi-user profiles
- [ ] Keyboard shortcuts

---

## Code Statistics

### Lines of Code (Approximate)
- **Arduino:** ~120 lines
- **SwiftUI (UI):** ~270 lines
- **Audio Logic:** ~400 lines
- **Serial Communication:** ~200 lines
- **Total:** ~990 lines

### Files Created
- **Swift Files:** 6
- **Arduino Files:** 1
- **Documentation:** 5
- **Total:** 12 files

---

## Credits & Acknowledgments

**Developed by:** Claude (Anthropic AI) + User collaboration
**Development Time:** ~4 hours (single session)
**Date:** November 18, 2025

**Technologies Used:**
- Swift 5.9
- SwiftUI
- AVFoundation
- IOKit
- Arduino IDE
- Xcode 15

**Special Thanks:**
- Arduino community for hardware inspiration
- Apple's AVFoundation documentation
- Loop pedal enthusiasts for feature ideas

---

## License

MIT License - Free to use, modify, and distribute

---

## Conclusion

This project successfully demonstrates:
1. Hardware-software integration (Arduino + Mac)
2. Real-time audio processing
3. Serial communication protocols
4. Multi-threaded Swift programming
5. SwiftUI reactive patterns
6. Audio engine architecture

The resulting drum loop recorder provides a tactile, hardware-based interface for creating layered audio loops, suitable for:
- Live performance
- Beatboxing
- Music composition
- Sound design
- Educational purposes

**Project Status:** ✅ Complete and functional

---

**Last Updated:** November 18, 2025
**Version:** 1.0
**Document Version:** 1.0
