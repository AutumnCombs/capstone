import os
import re

def scan_file_for_scripts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    patterns = [
        r'<script.*?>.*?</script>',
        r'on\w+="[^"]+"',
        r'document\.write',
        r'eval\(',
        r'javascript:'
    ]

    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            print(f"Suspicious pattern found in {file_path}: {pattern}")

def scan_directory(directory):
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.html', '.js', '.php', '.jsp')):
                scan_file_for_scripts(os.path.join(root, filename))

# web app's output folder
scan_directory('.')
