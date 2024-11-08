from page.build import PERSONALITIES_OUT_DIR

FILES = [
    PERSONALITIES_OUT_DIR + "10101.html",
    PERSONALITIES_OUT_DIR + "10201.html",
]

HTML = [
    """<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <p>placeholder</p>
    </body>
</html>
""",
    """<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <p>placeholder</p>
    </body>
</html>
""",
]


def build():
    for file, html_content in zip(FILES, HTML):
        print(f"Building {file}...")
        with open(file, "w") as f:
            f.write(html_content)
