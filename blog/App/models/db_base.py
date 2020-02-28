from App.extensions import db

class DB Base:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:db.session.rollback()
