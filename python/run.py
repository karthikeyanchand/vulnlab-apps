from vulnlab import create_app

app = create_app()

if __name__ == "__main__":
    # Bound to 127.0.0.1 so the lab is never reachable from the network.
    app.run(host="127.0.0.1", port=5001, debug=True)
