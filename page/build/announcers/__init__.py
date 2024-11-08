from page.build import ANNOUNCERS_OUT_DIR

FILES = [
    ANNOUNCERS_OUT_DIR + "1.html",
    ANNOUNCERS_OUT_DIR + "2.html",
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
