# FireRed Image Edit Fast

**Identidad del paquete:** `influent.firered-imgedit-1-0.v1.0-26.08-21.56`
**Autor:** `JesusQuijada34`
**Plataforma:** `AlphaCube`
**Descripción:** Estructura reparada por MoonFix

## Estructura PackageMaker 3.2.7

Este repositorio fue normalizado mediante **MoonFix**, usando la estructura de PackageMaker 3.2.7. El paquete público debe conservar `details.xml`, `version.res`, `autorun`, `autorun.bat`, `.storedetail`, `updater.py`, `config/settings.json`, los marcadores `.container` y los archivos de documentación correspondientes. El publisher oficial es `influent` y la versión pública no contiene sufijo de plataforma.

## Instalación y ejecución

Instala las dependencias declaradas en `lib/requirements.txt` cuando exista y ejecuta el entrypoint real del proyecto. En Linux, los comandos privilegiados son específicos de Danenone y no deben trasladarse a Windows. En proyectos AlphaCube, la validación Windows debe realizarse con el `buildthis` oficial de PackageMaker.

## Validación

La fuente debe pasar compilación sintáctica, pruebas funcionales disponibles, comprobación de identidad XML, protección contra traversal en ZIP y llamadas seguras a subprocess. Los artefactos `.iflapp` deben ser generados por PackageMaker; los paquetes Debian deben usar el nombre canónico `influent.firered-imgedit-1-0.v1.0-26.08-21.56_ARCH.deb`.

## Release

El tag y el título del release deben ser exactamente `v1.0-26.08-21.56`. Los assets deben usar el nombre canónico del paquete y una extensión objetiva. No se permite publicar un release AlphaCube que contenga únicamente el build Linux.

## Referencia original

# FireRed Image Edit Fast

FireRed Image Edit Fast es una interfaz web Gradio para edición de imágenes guiada por prompts. Utiliza los módulos FireRed/Qwen y Diffusers, descarga los pesos bajo demanda y se clasifica como **AlphaCube** porque el repositorio contiene código fuente y no un paquete Debian autocontenido.

## Instalación

Crea un entorno virtual e instala las dependencias:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

Las dependencias incluyen PyTorch, Diffusers, Transformers, Gradio y los componentes de atención/modelo requeridos. La instalación de PyTorch debe elegirse según la plataforma y la versión de CUDA disponibles; no se debe asumir que una máquina CPU puede ejecutar inferencia de forma práctica.

## Ejecución

```bash
python app.py
```

El servidor Gradio queda disponible en la URL local que muestre la terminal. El modelo pesado se carga **solo cuando llega la primera solicitud de inferencia**, no durante la importación de `app.py`. CUDA se usa si está disponible; en CPU se utiliza `float32` y una ruta de carga compatible, aunque la inferencia puede requerir mucha memoria y tiempo.

## Cambios de estabilidad

Se añadió el import faltante de `os`, se incorporó un fallback cuando el paquete `spaces` no está instalado y se hizo diferida la carga de Diffusers/Qwen. La interfaz conserva la selección de imágenes, prompt, semilla, escala de guía y pasos. Las comprobaciones locales validan la sintaxis y que el servidor pueda importar su código sin descargar automáticamente los pesos.

## Estructura y licencia

`app.py` contiene la interfaz Gradio y la inferencia; `qwenimage/` contiene los módulos de transformación y atención; `requirements.txt` declara las dependencias. Los pesos se descargan de los repositorios configurados por el código y no se incluyen en el artefacto fuente. Revisa las licencias de los modelos y dependencias antes de redistribuirlos.

El artefacto universal debe conservar el formato:

```text
JesusQuijada34.firered-imgedit-1-0.v1.0-26.08-23.43-AlphaCube.iflapp
```
