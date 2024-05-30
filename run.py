from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea todas las tablas en la base de datos
        app.run(debug=True)  # Inicia el servidor de desarrollo con el modo de depuración activado
