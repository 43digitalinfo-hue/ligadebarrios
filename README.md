# Liga de Barrios de Barakaldo

Juego de navegador: RPG de criaturas con vista cenital y partidos de fútbol arcade, ambientado en los barrios de Barakaldo.

## Cómo jugar

Abre `liga-barrios-barakaldo.html` en el navegador. Es un único archivo autocontenido (sprites incluidos); solo la fuente Pixelify Sans se descarga de Google Fonts.

En el móvil, el partido se juega con un joystick flotante en la mitad izquierda y botones a la derecha. Si el teléfono lo permite (Android), vibra; se quita en el título, el Menú o la Pausa.

Defendiendo, ★ busca un corte con la supertécnica del defensor. Cerca de tu área, a veces salta solo un "¡CORTE VALOR GOL!" para elegir técnica. Las opciones salen como cartas abajo: toca una (o pulsa 1-9 y Enter).

### Parámetros de la URL

- `?debug`: activa el Modo prueba (toca 5 veces el título) y expone `window.G` para depurar. Sin este parámetro no están disponibles.
- `?hora=N`: fuerza la hora del día (0-23) para probar la luz, el cielo y los focos.
- `?hd`: dibuja los minijuegos, el fichaje y la feria en alta resolución en vez de en píxeles.
- `?nofx`: desactiva el postproceso WebGL. En móviles lentos se desactiva solo ("Modo fluido").

## Entrenamientos

Cada entrenamiento (penaltis, regate o paradas) son 3 intentos con tu criatura: 3 aciertos = oro, 2 = plata, 1 = bronce y 0 = sin experiencia.

## La Feria

Desde el mapa se entra a la Feria, con juegos de azar, habilidad y estrategia que dan fichas y criaturas (con tope diario y rara asegurada):
tragaperras de bar, mus con órdago, dados del mentiroso, gancho de feria, sokatira, frontón y chapas en la acera.

## Minijuegos

Los 24 minijuegos de los barrios comparten una capa común: cuenta atrás 3-2-1, puntos flotantes, rachas, sacudida al fallar,
medalla en directo y aviso en los últimos segundos. Todos tienen escenario y animaciones propias.
Todo el juego tiene la estética de píxeles de las portátiles clásicas:
- Se dibuja en un lienzo pequeño que se amplía sin suavizar, con degradados en franjas y sombras duras.
- La letra de píxeles va incrustada.
- Los fichajes se presentan como un combate clásico.

La música es de chip y generativa (Web Audio): ondas de pulso, bajo triangular y percusión de ruido. Cambia según el momento:
calma en el barrio, curiosidad al fichar, tensión creciente en el partido, tristeza en la derrota y euforia en la victoria.
Suena baja para acompañar sin tapar.

## Contenido

- `liga-barrios-barakaldo.html`: el juego.
- `INFORME_REVISION.md`: errores corregidos, cambios de jugabilidad en los partidos y temas pendientes.
- `SPRITES_NECESARIOS.md`: inventario de sprites hechos y por hacer, con prioridades.
- `*.png`, `*.jpg`: hojas de sprites y capturas del juego.
