import json
import os
import time

# Definitions
edge_stable = "Edge"
edge_beta = "Edge Beta"
edge_dev = "Edge Dev"
exported_time = time.strftime('%Y-%m-%d_%H-%M-%S')

# Choose the Edge Release (edge_stable, edge_beta, edge_dev) you like to Backup:
edge_release = edge_stable

# Path to Edge Bookmarks Source-File
json_file_path = os.path.join(os.environ['LOCALAPPDATA'], f"Microsoft\\{edge_release}\\User Data\\Default\\Bookmarks")

# Directory where to store HTML-Export (Backup-Destination-Directory)
# html_file_dir = "C:\\Temp"
# html_file_dir = os.path.join(os.environ['USERPROFILE'], "backup")
# html_file_dir = os.environ['USERPROFILE']
html_file_dir = os.path.join(os.environ['USERPROFILE'], "Documents")

# Filename of HTML-Export (Backup-Filename), choose with YYYY-MM-DD_HH-MM-SS Date-Suffix or fixed Filename
# html_file_path = os.path.join(html_file_dir, "EdgeChromium-Bookmarks.backup.html")
html_file_path = os.path.join(html_file_dir, f"EdgeChromium-Bookmarks.backup_{exported_time}.html")

# Reference-Timestamp needed to convert Timestamps of JSON (Milliseconds / Ticks since LDAP / NT epoch 01.01.1601 00:00:00 UTC) to Unix-Timestamp (Epoch)
date_ldap_nt_epoch = 11644473600

if not os.path.isfile(json_file_path):
    raise ValueError(f"Source-File Path {json_file_path} does not exist!")
if not os.path.isdir(html_file_dir): 
    raise ValueError(f"Destination-Directory Path {html_file_dir} does not exist!")

# ---- HTML Header ----
bookmarks_html_header = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
'''
with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(bookmarks_html_header)

# ---- Enumerate Bookmarks Folders ----
def get_bookmark_folder(node):
    def convert_to_unix_timestamp(timestamp):
        date = timestamp / 1000000 - date_ldap_nt_epoch
        if date > 0:
            return int(date)

    if node['name'] == "Favorites Bar":
        date_added = convert_to_unix_timestamp(node['date_added'])
        date_modified = convert_to_unix_timestamp(node['date_modified'])
        with open(html_file_path, "a", encoding="utf-8") as f:
            f.write(f'        <DT><H3 FOLDED ADD_DATE="{date_added}" LAST_MODIFIED="{date_modified}" PERSONAL_TOOLBAR_FOLDER="true">{node["name"]}</H3>\n')
            f.write('        <DL><p>\n')
    for child in node['children']:
        date_added = convert_to_unix_timestamp(child['date_added'])
        date_modified = convert_to_unix_timestamp(child['date_modified'])
        if child['type'] == 'folder':
            with open(html_file_path, "a", encoding="utf-8") as f:
                f.write(f'        <DT><H3 ADD_DATE="{date_added}" LAST_MODIFIED="{date_modified}">{child["name"]}</H3>\n')
                f.write('        <DL><p>\n')
