import os
import json
import sys
from pathlib import Path

def generate_index_files():
    # Configure paths
    base_dir = Path(__file__).parent
    api_dir = base_dir / 'API'
    folders = ['animations', 'fonts', 'music', 'sfx']

    print(f"Starting JSON generation in: {base_dir}")
    
    # Create API structure if missing
    api_dir.mkdir(exist_ok=True)
    for folder in folders:
        (api_dir / folder).mkdir(exist_ok=True)

    # Generate index files
    for folder in folders:
        folder_path = api_dir / folder
        files = []
        
        try:
            # Get all files (ignore subdirectories)
            files = [f.name for f in folder_path.iterdir() if f.is_file()]
            print(f"Found {len(files)} files in {folder}")
            
            # Create JSON content
            index_data = {
                "folder": folder,
                "generated_at": str(os.path.getctime(folder_path)),
                "files": files
            }
            
            # Write to file
            index_file = folder_path / 'index.json'
            with open(index_file, 'w') as f:
                json.dump(index_data, f, indent=2)
                
            print(f"Created {index_file}")

        except Exception as e:
            print(f"Error processing {folder}: {str(e)}")
            continue

if __name__ == '__main__':
    try:
        generate_index_files()
        print("\n✅ Generation complete!")
    except Exception as e:
        print(f"\n❌ Critical error: {str(e)}")
        sys.exit(1)