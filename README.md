# Agenda de Contactos Personal

Aplicación web desarrollada con Django para administrar contactos personales.

## Funcionalidades

- Registrar nombre, teléfono, correo electrónico y dirección.
- Validar automáticamente el formato del correo electrónico.
- Buscar contactos por nombre o correo.
- Consultar y administrar los registros desde el panel de administración de Django.

## Instalación y ejecución

Requiere Python 3.12 o superior.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` en el navegador.

Para ejecutar las pruebas:

```powershell
python manage.py test
```

## Estructura MVC de Django

- **Modelo:** `contacts/models.py` define el contacto y sus campos.
- **Vista:** `contacts/views.py` procesa altas y búsquedas.
- **Formulario:** `contacts/forms.py` usa `ModelForm` y la validación `EmailField`.
- **URLs:** `config/urls.py` conecta la página principal con la vista.
- **Plantilla:** `contacts/templates/contacts/contact_list.html` presenta la interfaz.

