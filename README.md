# 🌱 Forraje Testing System

Sistema de pruebas de software desarrollado en Python utilizando `pytest`, enfocado en la validación de un sistema de recomendación de cultivos de forraje para ovinos y caprinos.

---

## 📌 Descripción

Este proyecto implementa un conjunto completo de pruebas de software sobre un sistema simulado que incluye:

- Autenticación de usuarios (login)
- Recomendación de cultivos basada en variables ambientales (pH y temperatura)

El objetivo principal es demostrar la aplicación de diferentes tipos de testing en el desarrollo de software, siguiendo buenas prácticas de arquitectura y validación.

---

## 🧱 Arquitectura del Proyecto

El sistema está organizado bajo una arquitectura modular:


app/
│
├── models/ # Modelos de datos
├── services/ # Lógica de negocio
├── utils/ # Validaciones
│
data/ # Datos simulados
tests/ # Pruebas automatizadas


---

## ⚙️ Tecnologías Utilizadas

- Python 
- pytest
- unittest.mock (MagicMock)

---

## 🧪 Tipos de Pruebas Implementadas

El proyecto incluye múltiples tipos de testing:

### ✔ Pruebas Unitarias
Validan funciones individuales como:
- Login
- Recomendación de cultivos

### ✔ Pruebas de Integración
Evalúan la interacción entre:
- Servicios y datos simulados

### ✔ Pruebas de Rendimiento
Miden el tiempo de respuesta del sistema.

### ✔ Pruebas de Seguridad
Validan entradas inválidas y comportamientos inesperados.

### ✔ Pruebas de Regresión
Aseguran que funcionalidades existentes no se vean afectadas por cambios.

### ✔ Pruebas de Humo (Smoke Tests)
Verifican que el sistema funcione correctamente en su nivel básico.

---

## 🔧 Técnicas Aplicadas

- Uso de **fixtures** (`conftest.py`)
- Parametrización de pruebas (`pytest.mark.parametrize`)
- Manejo de excepciones
- Uso de **mocks** (`MagicMock`) para simular dependencias externas
- Separación de responsabilidades (services, models, utils)

---

## 📊 Datos Simulados

El sistema utiliza datos simulados para representar:

- Usuarios (`fake_users.py`)
- Cultivos (`fake_cultivos.py`)

Esto permite ejecutar pruebas sin necesidad de una base de datos real.

---

## ▶️ Ejecución del Proyecto

### 1. Clonar repositorio

git clone https://github.com/TU-USUARIO/forraje-testing-system.git
cd forraje-testing-system

2. Crear entorno virtual
   
python -m venv .venv

Activar:

.venv\Scripts\activate

3. Instalar dependencias
   
pip install -r requirements.txt

4. Ejecutar pruebas
   
python -m pytest

📈 Resultados Esperados

El sistema ejecuta múltiples pruebas de manera automatizada, mostrando resultados como:

XX passed in 0.XXs

Esto indica que todas las pruebas fueron exitosas.

🎯 Objetivo Académico

Este proyecto tiene como propósito:

Aplicar conceptos de testing de software
Implementar pruebas automatizadas en Python
Simular un sistema real con arquitectura organizada
Demostrar el uso de diferentes niveles y tipos de pruebas

👨‍💻 Autores
ForraTech Dev Team (Estudiantes de Ingeniería de Sistemas)

📚 Licencia

Este proyecto es de uso académico.
