# Contexto (App out of context)
```python
    from flask import Flask
    app = Flask(__name__)
```

## 1 Configuração

### Add configuração

```python
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DB;_URI"] = "msql://.."
```

### Registrar Rotas


```python
    @app.router("/path")
    def funcao():
        ...

    app.add_url_rule("/path", callable)
```

### Inicializar extensões

```python
    from flask_admin import Admin
    Admin.init_app(app)
```

### Blueprints
```python
    app.register_blueprints()
```

# Add hooks
```python
    @app.before_request()
    @app.error_handler()
```

### Chamar outras factory
```python
    views.init_app()
```

## 2 App Context

### App está pronto!

### Testar

```python
    app.test_client
```
 - debug
 - objetos globais do Flask
 -- (importar request, session, g)
```python
    from flask import current_app, g
```
 - Hooks são executados (nem todos)

## 3 Request Context

### Usar globais do Flask

```python
    from flask import request, session, g

    request.args
    request.form
```

