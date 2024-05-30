from app import app, db

if name == 'main':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
