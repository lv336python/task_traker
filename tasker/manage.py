"""
This module starts app at port 0.0.0.0
"""
from app import app


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
