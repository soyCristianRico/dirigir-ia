# Dirigir IA

Repo de partida del taller **El trabajo que antes me llevaba una semana**. Una carpeta de trabajo para [Claude Code](https://claude.com/claude-code), lista para que empieces a dirigir la IA en vez de hacerlo todo tú.

## Qué necesitas

- Una suscripción de Claude.
- Una cuenta gratuita de [GitHub](https://github.com).
- [Orca](https://www.onorca.dev/), donde vas a trabajar.

## Empezar

1. Arriba a la derecha de esta página pulsa **Use this template** y luego **Create a new repository**. Ponle el nombre que quieras y elígelo privado. Es tu copia, este repo original no se toca.
2. Instala Orca y clona tu copia desde ahí.
3. Abre la copia en Orca y lanza Claude Code como agente.
4. Pega esto en el chat, tal cual:

```
Lee README.md y CLAUDE.md. Hazme, de una en una, las preguntas que necesites para rellenar mi CLAUDE.md. Cuando tengas las respuestas, rellénalo.
```

Puedes contestarle hablando en vez de escribiendo. Va más rápido.

## Qué hay dentro

```
CLAUDE.md             tus instrucciones para Claude, corto y a rellenar
plantillas/proceso.md   para documentar una tarea a mano antes de dársela a la IA
.claude/mecanicas/    ficheros de referencia que Claude carga solo cuando hacen falta
.claude/skills/       aquí irán tus skills, de momento vacía
workspace/            tu carpeta de trabajo. Su contenido no se sube a GitHub
```

Las **mecánicas** no son skills. Son notas sobre cómo hacer algo que se repite, y Claude las lee a media tarea, solo cuando le hacen falta.

## El navegador de Orca

Para que Claude lea o use páginas web con tus sesiones ya iniciadas, en Orca haces tres cosas, una sola vez.

1. **Enable Orca CLI.** Registra el comando para que los agentes manejen el navegador.
2. **Browser Use skill.** Instálala. Es lo que le da a Claude la capacidad de navegar.
3. **Import Browser Cookies.** Trae tus sesiones ya iniciadas al navegador de Orca.

Si alguna cuenta no entra por cookies (pasa con la verificación en dos pasos), la alternativa dentro de Orca es **Computer Use**. En macOS necesita permisos de privacidad extra.

Cómo lo usa Claude está en `.claude/mecanicas/orca-browser.md` y `.claude/mecanicas/computer-use.md`.

## Conectar tus aplicaciones

Para que Claude trabaje con una app (correo, calendario, tu CRM), pregúntale a Claude cómo instalar su MCP. Suele resolverlo él solo.

La configuración se guarda en `.mcp.json`, que está en `.gitignore`. No se sube a GitHub, y así debe seguir. Nunca pegues contraseñas o claves en un fichero que sí se suba.

## Git, lo mínimo

- **Clonar** (traerte el repo a tu ordenador, solo la primera vez). `git clone <url>`.
- **Actualizar** (traer los cambios que haya). `git pull`.
- **Guardar un cambio**, después de editar algo.
  1. `git add .` marca todo lo que has tocado.
  2. `git commit -m "qué has cambiado, en una frase"` lo guarda en tu historial.
  3. `git push` lo sube a GitHub.
- Si `git push` te pide hacer `git pull` primero, es que se subió algo antes. Haz `git pull` y repite `git push`.

Para que Claude Code pueda crear cosas en GitHub por ti, ejecuta `gh auth login` y sigue las instrucciones.
