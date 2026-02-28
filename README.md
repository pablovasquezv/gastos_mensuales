```markdown
# 🚀 Gastos Mensuales con Categorías (Django + Bootstrap + CSS + JQUERY)

Una aplicación web robusta y elegante diseñada para el control financiero personal. Permite gestionar gastos diarios, organizarlos por categorías y visualizar el balance mensual con una interfaz moderna y responsiva.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** [Django 6.0](https://www.djangoproject.com/)
* **Frontend:** [Bootstrap 5](https://getbootstrap.com/) & [Axios](https://axios-http.com/)
* **Base de Datos:** SQLite (desarrollo) / PostgreSQL (opcional)
* **Iconos:** Bootstrap Icons

---

## 📁 Estructura del Proyecto

El proyecto sigue una arquitectura modular, separando la lógica de negocio en la aplicación `gastos` y manteniendo los recursos estáticos centralizados.Además se han aplicado una de las mejores prácticas de Django: el Namespacing de plantillas.Al crear una carpeta templates/ en la raíz (a la altura del proyecto) y organizar todos los archivos como account/login.html

```text
gastos_app/
├── manage.py
├── gastos_app/           # Configuración del proyecto base
│   ├── settings.py
│   └── urls.py
├── gastos/                # Aplicación principal de lógica
│   ├── models.py          # Modelos de Gasto y Categoría
│   ├── views.py           # Controladores de la interfaz
│   ├── urls.py            # Rutas internas de la app
│   └── templates/gastos/  # Plantillas HTML (Base, Index, Listar, Agregar)
├── static/                # Recursos Estáticos
│   └── gastos/
│       ├── css/           # Estilos personalizados (style.css)
│       └── js/            # Lógica Frontend (main.js / Axios)
├── templates/                # Recursos Estáticos
│   └── gastos/
│       ├── cear/           # Estilos personalizados (style.css)
│       ├── editar/           # Estilos personalizados (style.css)
│       └── listar/            # Lógica Frontend (main.js / Axios)
└── requirements.txt       # Dependencias del sistema

```

---

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto localmente:

### 1. Clonar el repositorio y crear entorno virtual

```bash
git clone [https://github.com/tu-usuario/gastos-app.git](https://github.com/tu-usuario/gastos-app.git)
cd gastos_app
python -m venv .env

```

### 2. Activar el entorno virtual

* **Windows:** `.env\Scripts\activate`
* **Mac/Linux:** `source .env/bin/activate`

### 3. Instalar dependencias

```bash
pip install -r requirements.txt

```

### 4. Ejecutar migraciones y servidor

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

Accede a `http://127.0.0.1:8000/` en tu navegador.

---

## ✨ Características Principales

* **Gestión de Gastos:** Crear, leer, actualizar y eliminar (CRUD) registros de gastos.
* **Categorización Dinámica:** Clasificación de gastos por etiquetas (Alimentación, Transporte, etc.).
* **Middleware de Seguridad:** Protección de rutas para usuarios autenticados.
* **Interfaz Pro:** Uso de Overlays de redirección y validaciones asíncronas con Axios.

---

## 💡 Notas Técnicas

Este proyecto utiliza **Namespacing** para los templates y archivos estáticos (`gastos/`), lo que garantiza que no existan colisiones con otras aplicaciones del proyecto. La lógica de navegación está optimizada mediante **data-attributes** en el DOM para una integración limpia entre Django y JavaScript.

---

**¿Deseas que añada una sección de "Roadmap" con las próximas funciones (como gráficos de torta para los gastos)?**

```

¡Espero que este README le dé ese toque profesional a tu repositorio de GitHub! ¿Te gustaría que agreguemos alguna sección más específica?

```
***

## **📱 COMO USARLO:**

1. **Copiar** todo el contenido
2. **Crear** `README.md` en raíz del proyecto
3. **Pegar** → `Ctrl + S`
4. **Subir** a GitHub → **README renderizado hermoso** 🎉

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para reportar bugs o sugerir mejoras. Envía pull requests para colaborar con nuevas funcionalidades o correcciones.

## 👨‍💻 Autor

**Juan Pablo Vásquez** – Proyecto desarrollado y mantenido.
**Pablo** - [LinkedIn](https://www.linkedin.com/in/juan-pablo-vasquez-vasquez-8a9693206)  
**Email**: vasquezsoftwaresolutions.com

---

#### Última actualización  
*Juan Pablo Vásquez* - 27-02-2026