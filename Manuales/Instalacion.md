# 🎥 Manual de Instalación - OnlyUses Jellyfin

Este portal permite el registro de usuarios en una base de datos **MariaDB** independiente y la creación automática de la cuenta en el servidor **Jellyfin**.

## 🛠️ Requisitos
* Docker y Docker Compose instalado.
* Servidor Jellyfin accesible (Puerto 8096).
* Clave de API de Jellyfin.

## 📂 Estructura del Proyecto
* `/config`: Contiene el `docker-compose.yml` para levantar los servicios.
* `/app`: Código fuente en Python (FastAPI) para el procesamiento de datos.
* `/Manuales`: Documentación del sistema.

## 🚀 Puesta en marcha
1. Configura tu `API_KEY` en `app/main.py`.
2. Ejecuta `docker compose up -d` desde la carpeta config.
3. Accede a `http://tu-ip:8000` para ver el formulario rojo y negro de OnlyUses.
4. Gestiona la base de datos en el puerto `8080` con Adminer.

---
*Desarrollado por Eric-Alba*
