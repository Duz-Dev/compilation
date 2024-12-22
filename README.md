# Lista de Tareas - Proyecto de Práctica

Este es un proyecto simple de lista de tareas desarrollado utilizando Python y el framework Flet. El objetivo principal de este proyecto es proporcionar una interfaz gráfica simple para gestionar tareas mediante una aplicación que se puede ejecutar en diferentes plataformas, incluyendo dispositivos Android, Windows y navegadores web.

## Tecnologías utilizadas

- **Python** 3.12.3
- **Flet** 0.25.2
- **Flutter** 3.24.5
- **Visual Studio Community 2022** (para el desarrollo en Windows)
- **Android Studio** (para compilar y ejecutar la versión APK) y **Command-line tools**

- **C++ Desktop Development** (en Visual Studio para la creación de la versión de Windows)

## Advertencia importante

Este proyecto fue creado y probado con **Flet 0.25.2**, **Flutter 3.24.5** y **Python 3.12.3**. Las versiones más recientes de Flutter de momento no son compatibles con **flet 0.25.0**. Además, algunos entornos de desarrollo, como Visual Studio Community 2022 y las herramientas de Android Studio, son necesarios para compilar ciertas versiones (como la de Windows o APK).

## Estructura de Directorios

La estructura del proyecto es la siguiente:

```
compilation/
├── build
│   ├── apk           # Paquete APK para dispositivos Android
│   ├── web           # Archivos para ejecutar en el navegador
│   └── windows       # Paquete EXE para Windows
├── src               # Código fuente del proyecto
└── storage           # Carpeta para almacenar datos o archivos temporales
```

## Cómo ejecutar el proyecto

Dependiendo de la plataforma en la que quieras ejecutar la aplicación, hay diferentes métodos para hacerlo:

### Versión Android (APK)

1. En la carpeta [compilation/buld/apk](./build/apk/), encontrarás el archivo APK listo para instalar en tu dispositivo Android. Simplemente transfiérelo a tu dispositivo y ejecútalo como cualquier otra aplicación Android.

### Versión Windows (Ejecutable)

1. En la carpeta [compilation/buld/windows](./build/windows/), encontrarás el archivo `to_do.exe`. Puedes ejecutarlo directamente en tu máquina con Windows sin necesidad de ningún software adicional.

   <center><img src="https://i.postimg.cc/wBxMDqVx/Animation2.gif" alt="alt" width="500"/></center>

### Versión Web

Para esta version es necesario tener alguna forma de crear un servidor local para llamar a nuestra aplicación web. En este caso se puede utilizar **python**. A continuación te mostrare los pasos para ello (teniendo en cuenta que tienes python instalado previamente):

1. En la carpeta `compilation/buld/web`, abre una terminal y navega a la ubicación del directorio:

   ```bash
   cd compilation/buld/web
   ```

2. Inicia un servidor local con el siguiente comando:

   ```bash
   python -m http.server --directory .
   ```

3. Abre tu navegador y escribe la siguiente URL para ver la aplicación:

   ```text
   http://localhost:8000/
   ```

   <center><img src="https://i.postimg.cc/L4kdFtS7/web.gif" alt="alt" width="500"/></center>
   

---

## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu característica o corrección de errores: `git checkout -b feature/nueva-funcionalidad`.
3. Realiza los cambios necesarios y asegúrate de que el código sigue funcionando correctamente.
4. Envía un pull request describiendo los cambios realizados.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

---

Este proyecto fue creado con fines educativos y de práctica, y tiene como propósito demostrar la capacidad de integrar múltiples tecnologías en una sola aplicación funcional de lista de tareas.
