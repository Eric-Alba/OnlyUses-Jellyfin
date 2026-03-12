# 🎬 OnlyUses - Jellyfin

<p align="center">
  <img src="https://jellyfin.org/images/logo.svg" width="100" />
</p>

¡Bienvenido a **OnlyUses**! Este proyecto nace con la misión de dar una **segunda vida** a equipos antiguos o de bajos recursos, transformándolos en un servidor de medios local eficiente, estable y altamente seguro.

Utilizamos **Debian** como base por su ligereza y estabilidad, optimizando **Jellyfin** para que funcione con fluidez incluso en hardware limitado, protegiendo cada bit con herramientas de nivel empresarial.

---

## 🚀 Objetivos del Proyecto

* **♻️ Reutilización:** Optimizar hardware antiguo que de otro modo sería desechado.
* **⚡ Eficiencia:** Configuración mínima de servicios para maximizar el rendimiento.
* **🏠 Uso Local Pro:** Streaming de alta calidad dentro de la red doméstica.
* **🛡️ Hardening:** Implementación de seguridad activa para proteger el acceso root y los datos de usuario.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
| :--- | :--- |
| **S.O.** | Debian (Minimal Install) |
| **Container Engine** | Docker & Docker Compose |
| **Media Server** | Jellyfin |
| **Database** | MariaDB / MySQL |
| **Seguridad** | Fail2Ban & UFW Firewall |
| **Backups** | Rclone + Google Drive (Automático) |

---

## 📁 Estructura del Repositorio

Para mantener el orden en este servidor, hemos dividido el proyecto en las siguientes secciones:

* **[app](./app)**: Código fuente del portal web de registro de usuarios.
* **[mysql_data](./mysql_data)**: Persistencia de datos para la gestión de usuarios.
* **📖 [Manuales](./Manuales)**: Guías paso a paso para la instalación del sistema base y Jellyfin.
* **📖 [Manuales-web](./Manuales-web)**: Documentación específica para el despliegue del portal web.
* **⚙️ [config](./config)**: Archivos de configuración, incluyendo filtros de **Fail2Ban** y reglas de **UFW**.
* **🛠️ [scripts](./scripts)**: Automatizaciones para backups diarios (05:00 AM) y mantenimiento del sistema.

---

## 🔹 Diferencias clave respecto a Jellyfin estándar
A diferencia de una instalación típica de Jellyfin, nuestro proyecto no se limita a servir contenido multimedia. Hemos optimizado la plataforma para ofrecer **mayor rendimiento, seguridad y gestión de usuarios**, además de integrar una comunidad organizada de películas, series y música. Mientras Jellyfin normalmente se usa solo como servidor multimedia, en nuestro proyecto se utiliza como **gestor central de contenido**, combinado con una base de datos ligera para clientes y un sistema de backups que garantiza resiliencia y continuidad del servicio.

* **⚡ Rendimiento**
El sistema está optimizado para responder rápidamente a las consultas y mantener un servidor equilibrado incluso con múltiples usuarios. La separación de servicios y la estructura ligera permiten un acceso fluido al contenido multimedia sin saturar el servidor.

* **🎬 Comunidad Multimedia**
El contenido se organiza en diferentes secciones: **películas, series y música**. Gracias a Jellyfin, cada categoría puede manejarse con metadatos, carátulas y descripciones, facilitando la navegación, la búsqueda y la exploración de la comunidad multimedia.

* **💾 Seguridad y Resiliencia**
Protegemos los datos del sistema mediante **backups automáticos** programados. Cada madrugada se respalda la base de datos de usuarios y la configuración de Jellyfin, lo que asegura que la plataforma pueda recuperarse rápidamente ante cualquier fallo.

---

## 🛠️ Infraestructura y Servicios Configuradas

El ecosistema de **OnlyUses** está gestionado mediante contenedores Docker, garantizando un despliegue escalable y automatizado de los siguientes servicios:

### 📺 Gestión de Contenido y Streaming

* **Jellyfin**: Nuestro núcleo multimedia. Un servidor de streaming de código abierto que organiza y reproduce toda nuestra biblioteca sin restricciones.
* **Jellyseerr**: La puerta de entrada para los usuarios. Interfaz elegante para que los miembros puedan descubrir y solicitar nuevo contenido de forma sencilla.

### 🤖 Automatización (The "Arr" Stack)

Hemos configurado el stack completo para la gestión automatizada de descargas:

* **Sonarr**: Gestión inteligente y seguimiento de series de TV.
* **Radarr**: Automatización y seguimiento de películas con calidad personalizada.
* **Lidarr**: Gestión y descarga automática de música y discografías.
* **Prowlarr**: Indexador centralizado que sincroniza y gestiona todos nuestros trackers y sitios de descarga con el resto de aplicaciones "Arr".

### ⚙️ Administración y Control

* **Portainer.io**: Interfaz gráfica avanzada para la gestión de Docker. Nos permite monitorizar logs, estados de salud de los contenedores y gestionar redes de forma visual y rápida.

### 🔐 Integración de Registro Personalizado

Se ha implementado una aplicación a medida (`ellyfin-app`) vinculada a una base de datos **MariaDB** que permite:

* Registro automático de usuarios en Jellyfin vía API.
* Base de datos persistente para el control de usuarios.
* Interfaz de éxito personalizada con redirección automática al portal de streaming.

---

### 🌐 Mapa de Conectividad (Puertos internos)

| Servicio | Puerto Local | Función |
| --- | --- | --- |
| **OnlyUses App** | `8000` | Portal de Registro |
| **Jellyfin** | `8096` | Streaming de Vídeo |
| **Jellyseerr** | `5055` | Peticiones de contenido |
| **Radarr/Sonarr** | `7878 / 8989` | Automatización de Cine/TV |
| **Prowlarr** | `9696` | Gestión de Indexers |
| **Portainer** | `9443` | Gestión de Docker |
| Lidarr | 8686 | Automatización de Música |
---
## 🔹 Diferencias clave respecto a Jellyfin estándar
A diferencia de una instalación típica, **OnlyUses** centraliza la gestión de usuarios y la automatización de contenido:

* **📦 Base de Datos Centralizada**
Utilizamos **MariaDB** para gestionar el registro de usuarios de forma persistente. Esto nos permite separar la lógica de acceso de la base de datos interna de Jellyfin, mejorando la seguridad y el control administrativo.

* **⚡ Flujo de Trabajo Automatizado**
Mientras que un Jellyfin estándar requiere que el administrador suba archivos manualmente, nuestro stack detecta peticiones de usuarios, busca el contenido, lo descarga y lo organiza automáticamente sin intervención humana.

* **🎬 Experiencia de Usuario "Netflix-Style"**
Hemos diseñado un portal de registro personalizado con estética Dark Mode que unifica la experiencia desde el momento en que un usuario crea su cuenta hasta que empieza a ver contenido.

## 🔒 Seguridad y Resiliencia

Este proyecto no solo sirve contenido, también lo protege:
1.  **Protección Anti-BruteForce:** Implementación de Fail2Ban con filtros personalizados para detectar y banear IPs tras 3 intentos fallidos en Jellyfin o SSH.
2.  **Firewall Estricto (UFW):** Configuración de políticas "Deny by Default", abriendo únicamente los puertos necesarios (8096, 80, 22).
3.  **Backups Automáticos:** Script programado en `crontab` que respalda la base de datos y la configuración de Jellyfin en Google Drive cada noche.

---

## 📝 Notas de Optimización

Para lograr que Jellyfin corra en pocos recursos:
* Desactivamos la transcodificación pesada cuando no es necesaria.
* Limitamos el uso de caché en disco para prolongar la vida de unidades antiguas.
* Priorizamos el **"Direct Play"** en los clientes locales para reducir el uso de CPU.

---

## 👥 Mantenedores

Mantenido con ❤️ por:
* **Eric-Alba** - [GitHub Profile](https://github.com/Eric-Alba)
* **Luis-Elena** - [GitHub Profile](https://github.com/luiselenaruiz)

---

