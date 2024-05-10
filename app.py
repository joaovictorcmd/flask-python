from app import app, db

if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)