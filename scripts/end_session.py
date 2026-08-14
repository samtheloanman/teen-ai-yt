import os
import json
from datetime import datetime
import obsws_python as obs
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Connecting to OBS WebSocket to end session...")
    try:
        client = obs.ReqClient(host=os.getenv('OBS_HOST', 'localhost'), 
                               port=int(os.getenv('OBS_PORT', 4455)), 
                               password=os.getenv('OBS_PASSWORD', ''))
        
        # Stop streaming
        print("Stopping stream...")
        try:
            client.stop_stream()
        except Exception as e:
            print(f"Warning: Stream was not active or could not be stopped: {e}")

        # Stop recording and get the file path
        print("Stopping recording...")
        resp = client.stop_record()
        # obsws-python stop_record returns a string path for outputPath in modern OBS, 
        # let's safely handle it
        output_path = getattr(resp, 'output_path', 'Unknown Path')
        
        print(f"Recording stopped. File saved to: {output_path}")

        # Save the session info to config/last_session.json for Phase 3 (Auto-Clip Engine)
        session_info = {
            "timestamp": datetime.now().isoformat(),
            "recording_path": output_path
        }
        
        os.makedirs("../config", exist_ok=True)
        with open("../config/last_session.json", "w") as f:
            json.dump(session_info, f, indent=4)
            
        print("Session info saved to config/last_session.json")
        print("Session ended successfully.")

    except Exception as e:
        print(f"Error connecting to OBS: {e}")

if __name__ == "__main__":
    main()
