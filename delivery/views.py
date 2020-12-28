""""Extensão Flask """


from flask import Flask


def init_app(app: Flask):
    """"Inicialização de extensão """

    @app.route("/")
    def index():
        return "Hello, world!"
