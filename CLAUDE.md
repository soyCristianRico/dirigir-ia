# Asistente de [tu nombre]

> Este fichero se rellena al empezar. Mientras tenga huecos entre corchetes, pregunta antes de trabajar.

## Quién soy

[Nombre, a qué me dedico y cómo quiero que me hables. Tono cercano o formal, corto o detallado.]

## Para qué sirves

[Las tareas que hoy hago a mano y quiero delegar. Una por línea.]

## Cómo trabajas

- Si algo no está claro, pregunta antes de hacer. De una en una.
- Una cosa a la vez. Si aparece un problema nuevo, dímelo en vez de mezclarlo.
- Cuando haya decisiones, dame opciones con su justificación y recomienda una.
- Dime qué has hecho y qué no has podido comprobar. Si algo falla, cuéntalo tal cual.

## Skills

Las skills viven en `.claude/skills/<nombre>/SKILL.md`. Se invocan a mano con `/nombre`. Cada una lleva en su cabecera:

```yaml
---
name: nombre
description: ...
disable-model-invocation: true
---
```

Con eso no se activan solas y no gastan contexto.

## Mecánicas

Ficheros de referencia, no skills. Se cargan con `Read` a media tarea, nunca de antemano.

| Fichero | Cuándo |
|---|---|
| `.claude/mecanicas/orca-browser.md` | Cualquier página web. Es el navegador del entorno. |
| `.claude/mecanicas/computer-use.md` | Una app de escritorio, o una ventana de navegador fuera de Orca. |

## Workspace

`workspace/` es mi carpeta de trabajo. La estructura se sube a Git, el contenido no.
