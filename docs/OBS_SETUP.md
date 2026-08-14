# OBS Setup Guide

This document outlines the manual steps to record and go live using OBS Studio.

## Prerequisites
1. Download and install [OBS Studio](https://obsproject.com/).
2. Create a new Scene Collection named "Teen AI YT".

## Scene Configuration
Create the following scenes:
1. **Screen Share**: 
   - Source: Display Capture (or Window Capture for specific IDE/Browser)
   - Source: Audio Output Capture (to catch system/Meet audio)
2. **Webcam Overlay**:
   - Source: Video Capture Device (Webcam)
   - Source: Audio Input Capture (Microphone)
   - *Note: Add Webcam Overlay on top of Screen Share in a combined scene.*

## Streaming Setup (Manual)
1. Go to OBS Settings -> Stream.
2. Select "YouTube - RTMPS".
3. Use Stream Key (provided in YouTube Studio).
4. Click Apply.

## Recording & Streaming Process
1. Open OBS.
2. Verify audio levels.
3. To Record only: Click "Start Recording".
4. To Stream and Record: Click "Start Streaming" (make sure "Automatically record when streaming" is checked in Settings -> General).
5. When finished, click "Stop Recording/Streaming".

*Note: In Phase 2, these steps will be automated via `obsws-python`!*
