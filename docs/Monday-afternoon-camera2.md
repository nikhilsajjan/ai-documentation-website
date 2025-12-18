# Camera 2 iOS

A professional iOS camera application with real-time photo filters and advanced camera controls built using SwiftUI and AVFoundation.

## Features

### Camera Controls
- **Multiple Camera Support**: Seamlessly switch between all available iPhone cameras
  - Wide-angle camera
  - Ultra-wide camera
  - Telephoto camera
  - Front-facing camera
- **Automatic & Manual Rotation**: Choose between automatic device-based rotation or manually control the orientation
- **Real-time Preview**: Live camera preview with applied filters before capturing

### Photo Filters

#### Film-Style Filters
- **Kodak Portra 400**: Warm, subtle tones with soft contrast and gentle grain
- **Fujifilm C200**: Bright, saturated colors with peachy warmth typical of consumer film
- **None**: No filter applied (original image)

#### AI-Powered Filters
- **Remove Background**: Uses Vision framework to detect and remove/blur backgrounds
- **Pixelate People**: Applies pixelation effect only to detected people in the scene
- **Pixel Scenes**: Pixelates the entire scene for a retro 8-bit aesthetic

### Advanced Features
- **Filter Intensity Control**: Adjust filter strength from 0-100% with a slider
- **Flash Animation**: Visual feedback when capturing photos
- **Photo Gallery Integration**: Automatic saving to Photos library with proper orientation
- **Permission Handling**: Seamless camera and photo library permission management
- **Performance Optimized**: Frame throttling at 30 FPS for smooth real-time filtering

## Technical Details

### Built With
- **SwiftUI**: Modern declarative UI framework
- **AVFoundation**: Camera capture and video processing
- **CoreImage**: Real-time image filtering and effects
- **Vision Framework**: Person segmentation for AI-powered filters
- **Photos Framework**: Photo library integration

### Architecture
- **MVVM Pattern**: Clean separation with `CameraManager` as the view model
- **Async/Await**: Modern Swift concurrency for camera operations
- **Combine**: Reactive state management with `@Published` properties
- **Thread Safety**: Proper queue management for camera and processing operations

### Key Components

#### CameraManager.swift
Main camera controller handling:
- Camera device discovery and switching
- Session management (start/stop)
- Video output with filter preview
- Photo capture with filters applied
- Orientation management (automatic and manual)
- Person segmentation for background effects

#### CameraView.swift
Custom UIView wrapper for filtered camera preview:
- Real-time video display with applied filters
- Optimized image rendering pipeline

#### PhotoFilter.swift
Comprehensive filter system with:
- Multiple filter types (film, AI-based, effects)
- Intensity blending for smooth transitions
- Performance-optimized filter application
- Background removal with depth-based intensity
- Person detection and pixelation

#### ContentView.swift
Main UI providing:
- Camera preview with overlays
- Filter and camera selection pickers
- Intensity slider control
- Rotation mode controls
- Capture button with visual feedback

## Requirements

- iOS 15.0 or later
- Xcode 13.0 or later
- iPhone with camera support
- Camera and Photo Library permissions

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd camera_2_ios
```

2. Open the project in Xcode:
```bash
open camera_2_ios.xcodeproj
```

3. Build and run on your device or simulator (camera features require a physical device)

## Permissions

The app requires the following permissions:
- **Camera Access**: For capturing photos and video preview
- **Photo Library Access**: For saving captured photos

Permissions are requested automatically on first launch.

## Usage

1. **Launch the app** - Grant camera and photo library permissions when prompted
2. **Select a camera** - Use the camera picker to switch between available cameras
3. **Choose a filter** - Select from film-style or AI-powered filters
4. **Adjust intensity** - Use the slider to control filter strength (0-100%)
5. **Set rotation** - Toggle between automatic (device-based) or manual rotation control
6. **Capture photos** - Tap the camera button to take a photo
7. **Photos are saved** - Images are automatically saved to your photo library

## Performance Optimizations

- Frame rate throttling at 30 FPS to prevent UI freezing
- Background processing queues for image filtering
- Downscaled images for AI segmentation (640px max dimension)
- Efficient filter blending algorithms
- Minimal frame processing overhead

## Credits

Created by Nikhil Sajjan

## License

[Add your license here]
