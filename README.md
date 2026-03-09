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

* **📦 Base de datos de clientes**
Utilizamos **SQLite** para almacenar la información de los usuarios y sus preferencias. Esto permite consultas rápidas, reduce el consumo de recursos y mantiene la administración de datos simple y eficiente, mejorando notablemente el rendimiento general del sistema.

* **⚡ Rendimiento**
El sistema está optimizado para responder rápidamente a las consultas y mantener un servidor equilibrado incluso con múltiples usuarios. La separación de servicios y la estructura ligera permiten un acceso fluido al contenido multimedia sin saturar el servidor.

* **🎬 Comunidad Multimedia**
El contenido se organiza en diferentes secciones: **películas, series y música**. Gracias a Jellyfin, cada categoría puede manejarse con metadatos, carátulas y descripciones, facilitando la navegación, la búsqueda y la exploración de la comunidad multimedia.

* **💾 Seguridad y Resiliencia**
Protegemos los datos del sistema mediante **backups automáticos** programados. Cada noche se respalda la base de datos de usuarios y la configuración de Jellyfin, lo que asegura que la plataforma pueda recuperarse rápidamente ante cualquier fallo.

---

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

