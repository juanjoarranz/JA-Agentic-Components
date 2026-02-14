import os
import sys
import re
from datetime import datetime

EMOJI_MAP = {
    'feat': '✨',
    'fix': '🐛',
    'docs': '📚',
    'style': '🎨',
    'refactor': '♻️',
    'perf': '⚡',
    'test': '✅',
    'build': '🏗️',
    'ci': '👷',
    'chore': '🔧',
    'revert': '⏪'
}

def parse_commit_message(msg):
    # Split into subject and body
    parts = msg.split('\n', 1)
    subject = parts[0].strip()
    body = parts[1].strip() if len(parts) > 1 else ""
    
    # Extract type and description from subject
    # Pattern: type(scope): description or type: description
    match = re.match(r'^(\w+)(?:\(([^)]+)\))?:\s*(.*)$', subject)
    if match:
        ctype = match.group(1).lower()
        scope = match.group(2)
        desc = match.group(3)
        return ctype, scope, desc, body
    return None, None, subject, body

def update_changelog(full_message, filename='CHANGELOG.md'):
    if not full_message:
        print("Error: No commit message provided.")
        return
    
    ctype, scope, desc, body = parse_commit_message(full_message)
    emoji = EMOJI_MAP.get(ctype, '🔹')
    date_str = datetime.now().strftime("%Y-%m-%d")
    date_header = f"## [{date_str}]"
    
    # Format the header: ### ✨ feat: add something
    scope_part = f"({scope})" if scope else ""
    entry_header = f"### {emoji} {ctype}{scope_part}: {desc}"
    
    # Format the full entry
    new_entry = f"{entry_header}\n\n"
    if body:
        new_entry += f"{body}\n\n"
    
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n{date_header}\n\n{new_entry}")
        print(f"Created new {filename} with initial entry.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for duplicates (basic check)
    if entry_header in content:
        print(f"Entry '{entry_header}' already exists.")
        return

    # 1. Ensure the date header exists
    if date_header not in content:
        # Insert date header after the main # Changelog title
        main_header_match = re.search(r'^# .*\n', content)
        if main_header_match:
            pos = main_header_match.end()
            # Find the end of any intro text (until next header or beginning of entries)
            # For simplicity, we just insert after the main header
            content = content[:pos] + f"\n{date_header}\n\n" + content[pos:].lstrip()
        else:
            content = f"# Changelog\n\n{date_header}\n\n" + content

    # 2. Insert the entry under the date header
    date_pos = content.find(date_header)
    if date_pos != -1:
        # Find the next newline after the date header
        line_break = content.find('\n', date_pos)
        if line_break != -1:
            # Insertion point is after the date header line plus any immediate whitespace
            insert_pos = line_break + 1
            while insert_pos < len(content) and content[insert_pos] in ['\n', '\r', ' ']:
                insert_pos += 1
            
            content = content[:insert_pos] + new_entry + content[insert_pos:]
        else:
            # Date header was at the very end of file
            content += "\n\n" + new_entry

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully updated {filename} with new entry.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py update_changelog.py \"commit message\" [filename]")
        sys.exit(1)
        
    msg = sys.argv[1]
    target_file = sys.argv[2] if len(sys.argv) > 2 else 'CHANGELOG.md'
    update_changelog(msg, target_file)
