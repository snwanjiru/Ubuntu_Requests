import requests
import os
from urllib.parse import urlparse, unquote
import mimetypes

def get_extension_from_content_type(content_type):
    """Extract file extension from content-type header"""
    if not content_type:
        return None
    
    # Map common MIME types to extensions
    mime_map = {
        'image/jpeg': '.jpg',
        'image/png': '.png',
        'image/gif': '.gif',
        'image/webp': '.webp',
        'image/svg+xml': '.svg'
    }
    
    return mime_map.get(content_type.split(';')[0].lower())

def extract_filename(url, response):
    """Extract appropriate filename from URL or response headers"""
    parsed_url = urlparse(url)
    
    # Get filename from URL path
    filename = unquote(os.path.basename(parsed_url.path))
    
    # If no filename in URL, generate one
    if not filename or '.' not in filename:
        content_type = response.headers.get('content-type', '')
        ext = get_extension_from_content_type(content_type) or mimetypes.guess_extension(content_type) or '.jpg'
        filename = f"downloaded_image{ext}"
    
    return filename

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ").strip()
    
    if not url:
        print("✗ No URL provided. Please try again.")
        return
    
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch the image with appropriate headers
        headers = {
            'User-Agent': 'UbuntuImageFetcher/1.0 (Community Image Collection Tool)'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        # Check if content is actually an image
        content_type = response.headers.get('content-type', '').lower()
        if not content_type.startswith('image/'):
            print("✗ The URL does not point to an image file.")
            return
        
        # Extract appropriate filename
        filename = extract_filename(url, response)
        filepath = os.path.join("Fetched_Images", filename)
        
        # Handle duplicate filenames
        counter = 1
        name, ext = os.path.splitext(filename)
        while os.path.exists(filepath):
            filename = f"{name}_{counter}{ext}"
            filepath = os.path.join("Fetched_Images", filename)
            counter += 1
        
        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {os.path.abspath(filepath)}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()