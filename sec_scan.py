import os
import re

def scan_file_for_scripts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    patterns = {
        r'<script.*?>.*?</script>': 'Inline <script>',
        r'on\w+="[^"]+"': 'Inline event handler (e.g. onclick)',
        r'document\.write': 'Use of document.write',
        r'eval\(': 'Use of eval()',
        r'javascript:': 'javascript: URI scheme'
    }

    for i, line in enumerate(lines, start=1):
        for pattern, description in patterns.items():
            for match in re.finditer(pattern, line, re.IGNORECASE):
                print(f"[{file_path}] Line {i}: {description}")
                print(f"  Match: {match.group(0)}")
                print()

def scan_directory(directory):
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.html', '.js', '.php', '.jsp')):
                scan_file_for_scripts(os.path.join(root, filename))

# Web app's output folder
scan_directory('.')
