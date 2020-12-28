""""Extensão Flask """


from flask import Flask, request


def init_app(app: Flask):
    """"Inicialização de extensão """

    @app.route("/")
    def index():
        print(request.args)
        return "Hello, world!"
