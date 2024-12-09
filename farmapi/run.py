from farmapi import create_app
farmapi = create_app()
if __name__ == "__main__":
    
    farmapi.run(
        debug=True,
        host='0.0.0.0',
        port=5000
        )