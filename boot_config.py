import gzip
import json
import os
import sys
import time
import traceback
from os.path import dirname, join, isdir, expanduser

APP_NAME = "KOHighlights"
APP_DIR = dirname(os.path.abspath(sys.argv[0]))
os.chdir(APP_DIR)  # Set the current working directory to the app's directory

PORTABLE = False

if sys.platform == "win32":  # Windows
    try:
        portable_arg = sys.argv[1]
        PORTABLE = portable_arg == "-p"
    except IndexError:  # no arguments in the call
        pass

    PROFILE_DIR = join(os.environ[str("APPDATA")], APP_NAME)
    PORTABLE_DIR = join(APP_DIR, "portable_settings")
    SETTINGS_DIR = PORTABLE_DIR if PORTABLE else PROFILE_DIR
elif sys.platform == "darwin":  # MacOS 2check: needs to be tested
    SETTINGS_DIR = join(expanduser("~"), "Library", "Application Support", APP_NAME)
else:  # Linux+
    SETTINGS_DIR = join(expanduser("~"), ".config", APP_NAME)

if not isdir(SETTINGS_DIR):
    os.makedirs(SETTINGS_DIR)

def except_hook(class_type, value, trace_back):
    """ Print the error to a log file
    """
    name = join(SETTINGS_DIR, "error_log_{}.txt".format(time.strftime(str("%Y-%m-%d"))))
    with open(name, "a", encoding="utf8") as log:
        log.write("\nCrash@{}\n".format(time.strftime(str("%Y-%m-%d %H:%M:%S"))))
    traceback.print_exception(class_type, value, trace_back, file=open(name, "a", encoding="utf8"))
    sys.__excepthook__(class_type, value, trace_back)


sys.excepthook = except_hook

FIRST_RUN = False

try:
    with gzip.GzipFile(join(SETTINGS_DIR, "settings.json.gz")) as settings:
        j_text = settings.read().decode("utf8")
        app_config = json.loads(j_text)
except Exception:  # IOError on first run or everything else
    app_config = {}
    FIRST_RUN = True


BOOKS_VIEW, HIGHLIGHTS_VIEW = range(2)  # app views
CHANGE_DB, NEW_DB, RELOAD_DB = range(3)  # db change mode
(TITLE, AUTHOR, TYPE, PERCENT, RATING,
 HIGH_COUNT, MODIFIED, PATH) = range(8)  # file_table columns
PAGE, HIGHLIGHT_TEXT, DATE, PAGE_ID, COMMENT = range(5)  # high_list item data
(HIGHLIGHT_H, COMMENT_H, DATE_H, TITLE_H,
 AUTHOR_H, PAGE_H, CHAPTER_H, PATH_H) = range(8)  # high_table columns
(MANY_TEXT, ONE_TEXT, MANY_HTML, ONE_HTML,
 MANY_CSV, ONE_CSV, MANY_MD, ONE_MD) = range(8)  # save_actions
DB_MD5, DB_DATE, DB_PATH, DB_DATA = range(4)  # db data (columns)
FILTER_ALL, FILTER_HIGH, FILTER_COMM, FILTER_TITLES = range(4)  # db data (columns)

DB_VERSION = 0
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
CSV_HEAD = "Title\tAuthors\tPage\tDate\tChapter\tHighlight\tComment\n"
CSV_KEYS = ["title", "authors", "page", "date", "chapter", "text", "comment"]
HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body {background-color: white;}
        .book-block {
            border: 2px solid rgba(20, 20, 20, 0.5);
            padding: 20px;
            padding-top: 5px;
            background-color: #cdcdcd;
            border-radius: 25px;
        }
        .high-block {
            border: 2px solid rgba(115, 173, 33, 0.5);
            padding: 20px;
            background-color: #ebebeb;
            border-radius: 20px;
        }
    </style>
    <title>KoHighlights</title>
</head>
<body>
"""
BOOK_BLOCK = """
<div class="book-block">

<div align="center">
    <h2 style="display: inline;">%(title)s</h2><br/>
    <h3 style="display: inline;">%(authors)s</h3>
</div>
"""
HIGH_BLOCK = """
<div class="high-block">
    <p style="text-align:left;float:left;padding:1px; margin:0;">%(page)s</p>
    <p style="text-align:right;float:right;padding:1px; margin:0;">%(date)s</p>
    <hr style="clear:both;"/>
    <h4>%(chapter)s</h4>
    <p>%(highlight)s</p>
    <p>%(comment)s</p>
</div>
"""
