from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the nyc_taxi.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "nyc_taxi.ipynb", "--allow-websocket-origin=*"])
