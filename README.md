# Ubuntu_Requests
Ubuntu Image Fetcher
A Python script I have been using for collecting 3D inspiration images from the web for my Blender projects

## About This Tool
I created this Python script to help me collect and organize inspiration images for my 3D projects in Blender. As a 3D artist, I'm constantly finding visual references online that inspire my work, and this tool helps me build a personal library of these references in an organized way.

Feel free to use this script for any purpose you find helpful - whether you're also a 3D artist, a designer, or just someone who wants to save images from the web in an organized manner.

## Purpose
This tool helps me:

Build a reference library for my Blender projects

Collect texture inspiration and material references

Save character design concepts and environment ideas

Create mood boards for 3D scenes

Organize inspiration for lighting and composition studies

## Features
Downloads images from any publicly accessible URL

Organizes images in a dedicated "Fetched_Images" folder

Handles various image formats (JPEG, PNG, GIF, WebP, SVG)

Graceful error handling for failed connections

Prevents duplicate file overwrites

Respectful user-agent identification

## Let's fetch some Images 📷
Install the required dependencies using Ubuntu's package manager:
sudo apt install python3-requests

Run the script

When prompted, enter the full URL of the image you want to download
Make use of websites where you can find images with direct URLs 
Note: Even though the sites you find offer free images, always verify the license to ensure compliance, especially for public projects.

The image will be saved to the "Fetched_Images" directory in your current folder

## Testing the Script
To ensure the script works correctly, try these test cases:

### Test 1: Valid Image Download

Enter URL: https://picsum.photos/200/300
Expected Result: Image downloads successfully to Fetched_Images folder

### Test 2: Invalid URL

Enter URL: https://nonexistent-domain-12345.com/image.jpg
Expected Result: Clear error message without program crash

### Test 3: Non-Image Content

Enter URL: https://www.ubuntu.com
Expected Result: Message indicating URL doesn't point to an image

### Test 4: URL Without Clear Filename

Enter URL: https://httpbin.org/image/jpeg
Expected Result: Image downloads with generated filename

### Test 5: Duplicate Download
Run the same URL twice to test duplicate handling
Expected Result: Second download gets a numbered suffix (e.g., image_1.jpg)

## File Organization
All downloaded images are saved in the "Fetched_Images" directory with these naming conventions:

Uses the original filename when available

Generates appropriate names when filename isn't clear

Adds numbering to prevent overwrites (image.jpg, image_1.jpg, image_2.jpg)


## Ubuntu Philosophy Implementation
This script embodies Ubuntu principles:

Community: Connects to the global web community to share resources

Respect: Handles errors gracefully and respects website resources

Sharing: Organizes content for later sharing and inspiration

Practicality: Solves a real need for creative professionals

## Legal Considerations
Always respect copyright and usage rights:

Only download images you have permission to use

Attribute creators when required

Follow website terms of service

Use for personal inspiration and reference (most sites allow this)

## Contributing
Feel free to modify and adapt this script for your specific needs. If you make improvements that could benefit others, consider sharing them with the community.

## License
This script is provided as-is for educational and personal use. Please respect the rights of content creators when using downloaded images.