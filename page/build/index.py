from page.build import INDEX_OUT_FILE

HTML = """<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <p>peak.<br><br>
            <a href="personality.html">personality</a><br>
            <a href="ego.html">ego</a><br>
            <a href="announcer.html">announcer</a><br>
            <a href="item.html">item</a><br>
        </p>
    </body>
</html>
"""


def build():
    print(f"Building {INDEX_OUT_FILE}...")
    open(INDEX_OUT_FILE, "w").write(HTML)
