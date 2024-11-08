from page.build import PERSONALITY_INDEX_OUT_FILE

HTML = """<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <p>placeholder</p>
    </body>
</html>
"""


def build():
    print(f"Building {PERSONALITY_INDEX_OUT_FILE}...")
    open(PERSONALITY_INDEX_OUT_FILE, "w").write(HTML)
