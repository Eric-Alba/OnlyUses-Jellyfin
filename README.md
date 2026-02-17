# 🎬 OnlyUses - Jellyfin

¡Bienvenido a **OnlyUses**! Este proyecto nace con la misión de dar una **segunda vida** a equipos antiguos o de muy bajos recursos, transformándolos en un servidor de medios local eficiente y estable.

Utilizamos **Debian** como base por su ligereza y estabilidad, optimizando **Jellyfin** para que funcione con fluidez incluso en hardware limitado.

---

## 🚀 Objetivo del Proyecto
* **Reutilización:** Optimizar hardware antiguo que de otro modo sería desechado.
* **Eficiencia:** Configuración mínima de servicios para maximizar el rendimiento.
* **Uso Local:** Streaming de alta calidad dentro de la red doméstica.

---

## 📁 Estructura del Repositorio

Para mantener el orden en este servidor, hemos dividido el proyecto en las siguientes secciones:

* [**📖 Manuales**](./Manuales): Aquí encontrarás las guías paso a paso para la instalación del sistema base (Debian) y la puesta en marcha de Jellyfin.
* [**⚙️ Configuración**](./config): Contiene los archivos `docker-compose.yml` y otros ficheros necesarios para replicar este entorno de forma rápida.

---

## 🛠️ Stack Tecnológico
* **OS:** Debian (Minimal Install)
* **Engine:** Docker & Docker Compose
* **Media Server:** Jellyfin

---

## 📝 Notas de Optimización
Para lograr que Jellyfin corra en pocos recursos, en este proyecto:
1. Desactivamos la transcodificación pesada cuando no es necesaria.
2. Limitamos el uso de caché en disco.
3. Priorizamos el "Direct Play" en los clientes locales.

---

*Mantenido con ❤️ por [Eric-Alba](https://github.com/Eric-Alba)*

*Mantenido con ❤️ por [Luis-Elena](https://github.com/luiselenaruiz)*
