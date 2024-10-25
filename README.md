# EN - FastAPI Project

This project demonstrates the implementation of essential FastAPI functionalities, including Path Operations, validations with Pydantic, authentication, database connection using SQLAlchemy, modularization, tokens, middlewares, and routing.

---

## Table of Contents

1. **Path Operations**
2. **Validations with Pydantic**
3. **Authentication in FastAPI**
4. **Database Connection with SQLAlchemy**
5. **Modularization**
6. **Tokens**
7. **Middlewares**
8. **Routing**

---

### Path Operations

FastAPI allows the creation of path operations to define endpoints. This section includes methods for `GET`, `POST`, `PUT`, and `DELETE` requests, with route definitions and example parameters.

---

### Validations with Pydantic

With Pydantic, you can enforce data validation through models, ensuring that the incoming request data conforms to the defined schema.

---

### Authentication in FastAPI

Implement different authentication strategies, such as OAuth2, to secure endpoints and manage user access.

---

### Database Connection with SQLAlchemy

FastAPI can be connected to relational databases via SQLAlchemy for data persistence and retrieval. This section details the setup and configuration of SQLAlchemy with FastAPI.

---

### Modularization

Organize code into modules to improve maintainability and scalability. Here, you will find guidelines on structuring a FastAPI project with distinct modules for better organization.

---

### Tokens

Generate and manage access tokens for authenticated sessions, employing JWTs for secure token generation and validation.

---

### Middlewares

Add custom middleware to intercept requests and responses, handling tasks like logging, performance monitoring, or security checks.

---

### Routing

Define and organize route endpoints, creating separate route files for modular design.

---

## Installation

```bash
# Clone this repository
git clone https://github.com/RonaldCedeno/movie-fastapi.git
cd movie-fastapi

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI application
uvicorn main:app --reload
```

# ES - Proyecto FastAPI

Este proyecto demuestra la implementación de funcionalidades esenciales de FastAPI, que incluyen Operaciones de Ruta, validaciones con Pydantic, autenticación, conexión a bases de datos con SQLAlchemy, modularización, tokens, middlewares y enrutamiento.

---

## Tabla de Contenidos

1. **Operaciones de Ruta**
2. **Validaciones con Pydantic**
3. **Autenticación en FastAPI**
4. **Conexión a Base de Datos con SQLAlchemy**
5. **Modularización**
6. **Tokens**
7. **Middlewares**
8. **Rutas**

---

### Operaciones de Ruta

FastAPI permite la creación de operaciones de ruta para definir endpoints. Esta sección incluye métodos para las solicitudes `GET`, `POST`, `PUT` y `DELETE`, con definiciones de rutas y parámetros de ejemplo.

---

### Validaciones con Pydantic

Con Pydantic, puedes aplicar validaciones a los datos mediante modelos, asegurando que los datos de las solicitudes entrantes cumplan con el esquema definido.

---

### Autenticación en FastAPI

Implementa diferentes estrategias de autenticación, como OAuth2, para asegurar los endpoints y gestionar el acceso de usuarios.

---

### Conexión a Base de Datos con SQLAlchemy

FastAPI puede conectarse a bases de datos relacionales mediante SQLAlchemy para persistencia y recuperación de datos. Esta sección detalla la configuración de SQLAlchemy con FastAPI.

---

### Modularización

Organiza el código en módulos para mejorar su mantenibilidad y escalabilidad. Aquí encontrarás guías sobre cómo estructurar un proyecto FastAPI con módulos distintos para una mejor organización.

---

### Tokens

Genera y gestiona tokens de acceso para sesiones autenticadas, empleando JWTs para la generación y validación segura de tokens.

---

### Middlewares

Agrega middleware personalizado para interceptar solicitudes y respuestas, manejando tareas como el registro de eventos, monitoreo de rendimiento o verificaciones de seguridad.

---

### Rutas

Define y organiza los endpoints de rutas, creando archivos de ruta separados para un diseño modular.

---

## Instalación

```bash
# Clona este repositorio
git clone https://github.com/RonaldCedeno/movie-fastapi.git
cd movie-fastapi
# Instala las dependencias
pip install -r requirements.txt

# Inicia la aplicación de FastAPI
uvicorn main:app --reload
```
