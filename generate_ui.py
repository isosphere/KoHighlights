import os

# Inputs
FORM_PATH = os.path.join("resources", "forms")
RESOURCE_PATH = os.path.join("resources", "images.qrc")

# Outputs
FORM_OUTPUT = os.path.join("gui")
RESOURCE_OUTPUT = os.path.join("gui", "images_rc.py")

assert os.path.exists(FORM_PATH), f"Form path does not exist: {FORM_PATH}"
assert os.path.exists(RESOURCE_PATH), f"Resource path does not exist: {RESOURCE_PATH}"

# Generate UI
for root, dirs, files in os.walk(FORM_PATH):
    for file in files:
        if file.endswith(".ui"):
            print(f"Generating UI: {file}")
            this_output = os.path.join(FORM_OUTPUT, file.replace(".ui", ".py"))
            os.system(f"pyside6-uic -o {this_output} {os.path.join(FORM_PATH, file)}")

# Tweak images_rc.py location
print("Tweaking images_rc.py path referred to by generated UI files")
for root, dirs, files in os.walk(FORM_OUTPUT):
    for file in files:
        if file.endswith(".py") and file != "images_rc.py":
            with open(os.path.join(root, file), "r", encoding="utf8") as f:
                contents = f.read()
            contents = contents.replace("import images_rc", "from gui import images_rc")
            with open(os.path.join(root, file), "w", encoding="utf8") as f:
                f.write(contents)

print("Generating resources")
os.system(f"pyside6-rcc -o {RESOURCE_OUTPUT} {RESOURCE_PATH}")

print("Done")
