import startlocal
from bokeh.server import start
if __name__ == "__main__":
    import werkzeug.serving
    @werkzeug.serving.run_with_reloader
    def helper ():
        start.start_app()
