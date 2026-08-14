import os
import time
import obsws_python as obs
from dotenv import load_dotenv

# Load environment variables (e.g., OBS_PASSWORD, OBS_HOST, OBS_PORT)
load_dotenv()

def main():
    print("Connecting to OBS WebSocket...")
    try:
        # Assumes default config if env vars are not set
        # OBS_HOST=localhost, OBS_PORT=4455, OBS_PASSWORD=your_password
        client = obs.ReqClient(host=os.getenv('OBS_HOST', 'localhost'), 
                               port=int(os.getenv('OBS_PORT', 4455)), 
                               password=os.getenv('OBS_PASSWORD', ''))
        
        # Switch to the correct scene (Assuming "Screen Share" is the scene name)
        scene_name = "Screen Share"
        print(f"Switching scene to '{scene_name}'...")
        try:
            client.set_current_program_scene(scene_name)
        except Exception as e:
            print(f"Warning: Could not switch scene (it might not exist yet): {e}")

        # Start recording
        print("Starting recording...")
        client.start_record()
        
        # Start streaming
        print("Starting stream...")
        try:
            client.start_stream()
        except Exception as e:
            print(f"Warning: Could not start stream (check stream key/settings): {e}")

        print("OBS is now LIVE and RECORDING!")

    except Exception as e:
        print(f"Error connecting to OBS: {e}")
        print("Make sure OBS is running and WebSocket server is enabled (Tools -> WebSocket Server Settings).")

if __name__ == "__main__":
    main()
