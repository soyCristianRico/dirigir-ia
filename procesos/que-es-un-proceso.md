# Qué es un proceso

Un proceso, o SOP (procedimiento operativo estándar), es un documento con el saber hacer, el paso a paso y todo lo necesario para realizar una tarea que se repite. Así no depende solo de la cabeza de quien la hace hoy.

Se documenta cualquier tarea recurrente. Por ejemplo, el informe mensual de un cliente, dar de alta a un cliente nuevo o responder un tipo de correo.

## Reglas

- Todo proceso sigue la misma plantilla, `plantillas/proceso.md`. Mismas secciones, mismo orden.
- Todo proceso tiene su fila en el índice, `procesos/indice.md`.
- Nunca un nombre propio en el "Quién". Un rol, no una persona.
- Lo lee igual una persona que una IA. Escríbelo para alguien que nunca ha hecho la tarea.

## Cómo se crea con Claude

1. Cuéntale a Claude la tarea. Explícala hablando o pégale una transcripción de cómo la haces hoy.
2. Claude te hace las preguntas que falten, de una en una, antes de escribir nada.
3. Redacta el proceso con la plantilla y te lo enseña.
4. Con tu visto bueno, lo guarda en `procesos/` y añade su fila en el índice.
5. Actualiza el visor, para que puedas verlo en el navegador.

## Cómo duplicar un proceso

- **Uno nuevo.** Copia `plantillas/proceso.md` a `procesos/` con el nombre de la tarea, por ejemplo `procesos/informe-mensual.md`, y cuéntale a Claude la tarea para que lo rellene. O pídeselo directamente, "crea un proceso nuevo para esta tarea".
- **Uno parecido a otro que ya tienes.** Pídele a Claude que duplique ese proceso y lo adapte. Por ejemplo, el mismo informe para otro cliente.

## Cómo verlos

Abre `procesos/visor.html` con doble clic. Se abre en tu navegador y puedes buscar entre todos tus procesos. Si has añadido o cambiado alguno, pídele a Claude que actualice el visor, o ejecuta `python3 procesos/generar_visor.py`.

## Para trabajar con más gente

Si quieres que otras personas los vean y los comenten, copia los procesos a un Drive o a Google Docs.
