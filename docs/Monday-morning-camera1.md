# Camera 1

A macOS camera application with real-time photo filters and multi-camera support, built with SwiftUI and AVFoundation.

## Features

- **Multi-Camera Support**: Switch between built-in and external cameras in real-time
- **Live Filter Preview**: See filter effects applied in real-time before capturing
- **Photo Filters**:
  - **Kodak Portra 400**: Film-style aesthetic with warm tones and subtle grain
  - **Remove Background**: AI-powered background removal using Vision framework
  - **Pixelate People**: Pixelate detected people while keeping background clear
  - **Pixel Scenes**: Apply pixelation to entire scenes
- **Adjustable Filter Intensity**: Control filter strength from 0-100%
- **Auto-Save Gallery**: Captured photos automatically saved with timestamps
- **Mirror Preview**: Horizontal flip for front-facing cameras

## Requirements

- macOS 13.0 (Ventura) or later
- Xcode 14.0 or later
- Camera permissions enabled

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd camera_1
   ```

2. Open the project in Xcode:
   ```bash
   open camera_1.xcodeproj
   ```

3. Build and run the project (⌘R)

4. Grant camera permissions when prompted

## Usage

### Basic Operation

1. **Start Camera**: The camera starts automatically when the app launches
2. **Select Camera**: Choose from available cameras using the dropdown menu
3. **Choose Filter**: Select a filter from the Filter picker
4. **Adjust Intensity**: Use the slider to control filter strength (0-100%)
5. **Capture Photo**: Click the camera button to take a photo
6. **Stop/Start**: Toggle camera on/off using the Start/Stop button

### Photo Filters

#### Kodak Portra 400
A film-style filter that emulates the classic Kodak Portra 400 film stock with:
- Warm color temperature
- Lifted shadows
- Soft contrast
- Subtle grain texture
- Reduced saturation for natural skin tones

#### Remove Background
Uses Apple's Vision framework for AI-powered person segmentation:
- **0-70% intensity**: Progressively blurs background (0-40px radius)
- **70-100% intensity**: Fades background to transparency
- Fast quality mode optimized for real-time performance

#### Pixelate People
AI-powered pixelation that only affects detected people:
- Detects people using Vision framework
- Pixelation size scales with intensity (1x to 50x)
- Background remains sharp and clear

#### Pixel Scenes
Applies pixelation effect to entire scene:
- Uniform pixelation across the whole image
- Pixelation size scales with intensity (1x to 50x)
- Creates retro 8-bit/pixel art aesthetic

### Gallery

Photos are automatically saved to:
```
/Users/nikhilsajjan/Documents/AI/camera_1/gallery/
```

Filename format: `photo_YYYY-MM-DD_HH-mm-ss.jpg`

## Project Structure

```
camera_1/
├── camera_1App.swift          # Main app entry point
├── ContentView.swift           # Main UI with camera controls
├── CameraManager.swift         # AVFoundation camera session management
├── CameraView.swift           # Custom preview view with filter rendering
├── PhotoFilter.swift          # Filter implementations
├── Info.plist                 # App permissions and configuration
└── camera_1.entitlements      # App entitlements
```

## Key Components

### CameraManager
- Handles AVFoundation camera session
- Manages camera device discovery and switching
- Processes video frames for live preview
- Captures photos with applied filters
- Implements frame throttling for performance (30 FPS max)

### FilteredPreviewView
- Custom NSView for rendering camera preview
- Displays filtered frames in real-time
- Maintains aspect ratio
- Optimized for smooth playback

### PhotoFilter
- Implements all filter effects using Core Image
- Supports adjustable intensity for smooth transitions
- Uses Vision framework for AI-based filters
- Nonisolated functions for thread-safe operation

## Performance Optimizations

- Frame throttling (30 FPS) prevents UI freezing
- Background processing queues for heavy operations
- Downscaled image processing for Vision framework (640px max)
- Fast quality mode for real-time person segmentation
- Async/await for concurrent operations

## Permissions

The app requires camera access. If denied:
1. A permission screen will appear
2. Click "Open System Settings"
3. Enable camera access for the app
4. Restart the application

## Development

### Building from Source

```bash
# Clone and build
git clone <repository-url>
cd camera_1
xcodebuild -project camera_1.xcodeproj -scheme camera_1 build
```

### Dependencies

All dependencies are built-in frameworks:
- SwiftUI (UI framework)
- AVFoundation (Camera and media)
- CoreImage (Image filtering)
- Vision (AI person segmentation)
- AppKit (macOS native components)

## Technical Details

- **Language**: Swift 5.9+
- **UI Framework**: SwiftUI
- **Camera Framework**: AVFoundation
- **Image Processing**: Core Image, Vision
- **Concurrency**: Async/await, DispatchQueue
- **Architecture**: MVVM with ObservableObject

## Known Limitations

- Gallery path is hardcoded to project directory
- Requires macOS 13.0 or later
- Some filters require powerful hardware for real-time performance
- Background removal works best with good lighting

## License

[Add your license here]

## Author

Created by Nikhil Sajjan

## Acknowledgments

- Apple's AVFoundation and Vision frameworks
- Core Image filter documentation
- Film stock color science references
