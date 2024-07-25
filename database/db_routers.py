class DbRouter:
    def db_for_read(self, model, **hints):
        return "sqlite3"
    def db_for_write(self, model, **hints):
        return "sqlite3"