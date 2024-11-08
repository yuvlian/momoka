from page.build import EGOS_OUT_DIR

FILES = [
    EGOS_OUT_DIR + "20101.html",
    EGOS_OUT_DIR + "20102.html",
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
