# Revisión de liga-barrios-barakaldo.html

He revisado el archivo entero, de la línea 1 a la 2.681. La versión corregida es `liga-barrios-barakaldo.html`, en esta carpeta. El original sigue sin tocar en `Descargas`. Las líneas citadas (Lnnn) son las del original.

## Errores corregidos: graves

| # | Dónde | Problema | Arreglo |
|---|---|---|---|
| 1 | L1231 `panel()` | Al pasar de 200 manejadores, se vaciaba `OVH` justo después de crear los botones nuevos. Esos botones quedaban muertos y el juego se bloqueaba en fichajes, partidos y minijuegos. Lo he reproducido: los 3 botones del fichaje apuntaban a `OVH[201..203]`, que ya no existían. | Los paneles tienen ahora su propio registro (`PNH`). Al abrir un panel solo se borran los manejadores de los anteriores, y `OV()` ya no toca los del panel. |
| 2 | L2638 `keydown` | Con teclado físico no se podían escribir `a`, `s`, `d`, `w`, `z` ni espacios en el nombre, porque el juego se quedaba esas teclas con `preventDefault`. Lo he reproducido: al teclear "Patxi asdw" salía "txim". | Se ignoran las teclas mientras se escribe en un campo. Además, Enter y Espacio pulsan el botón del menú que tenga el foco. |
| 3 | L1976 / L1981 | Si el juego se cerraba durante la escena de Ramiro que cierra el prólogo, la partida quedaba guardada en acto 0 / tut 5. Desde ahí el jugador se quedaba encerrado para siempre: vallas cerradas y el mentor sin nada que decir. | Al continuar la partida, se repite la escena y se pasa a la liga. |
| 4 | L2620 / L2641 | En la pantalla de criatura "repetida", B o Escape cerraban el menú y se perdía la criatura recién fichada, sin recompensa. En los créditos se saltaban la insignia final y el aviso del post-juego. | Cada pantalla define ahora qué hace B (`OVB`). En "repetido" hay que elegir una opción, y en los créditos B equivale a Continuar. |
| 5 | L1602-1605 | Se podía hacer trampa: empezar un partido y abandonarlo al instante daba la experiencia y las fichas de consolación de una derrota. | Abandonar ya no da ni experiencia ni fichas. |
| 6 | L2058 | Si una página del álbum se completaba fuera del mapa (lo normal: al fichar), el juego lo apuntaba en `S.pendPage` pero no lo leía nunca. El premio de 300 fichas y 2 botas llegaba sin ningún aviso. | Las páginas pendientes van a una cola (`pendPages`) y se muestran al volver al mapa. Esto también rescata partidas antiguas que tuvieran `pendPage`. |
| 7 | L1893 | Si el inicial se había dejado en el txoko, la lista del entrenamiento gratis del prólogo salía vacía y no se podía avanzar. | El inicial se busca también en el txoko. |

## Errores corregidos: menores

- **Doble evolución de golpe** (L376, L1070): se mostraban el sprite y el nombre equivocados, por ejemplo "Fumon → Humareda" dos veces. Ahora cada evento guarda su etapa de destino.
- **Álbum** (L2071): la versión dorada no se veía, porque la imagen se guardaba en caché con la misma clave fuera dorada o no.
- **Criaturas visibles** (L1043): se pintaban siempre debajo de los NPCs y del jugador. Ahora se ordenan por altura (Y) como el resto.
- **"EXPERIENCIA" en Nv 50** (L1277): se ofrecía como opción principal y la experiencia se perdía. Ahora aparece desactivada.
- **Nombre** (L1103): un nombre hecho solo de espacios quedaba vacío, y los caracteres HTML se colaban en el menú y en los créditos. Ahora se filtran y, si queda vacío, se usa "Jon".
- **Ventana a 0×0** (L2647): con la pestaña en segundo plano, `drawImage` lanzaba `InvalidStateError` en cada frame. Visto en la consola.
- **Guardado:** el botón "Guardar" del bar y la casa decían "guardado" aunque hubiera fallado.
- **Audio:** si el navegador suspendía el audio, no se volvía a activar. Ahora se pausa al ocultar la pestaña y se reanuda al volver.
- **Autoguardado:** se guarda al ocultar la pestaña, solo si el jugador está libre en el mapa. En el móvil se suele cerrar sin pulsar Guardar.
- **Partidas antiguas:** si al objeto `items` le faltaban los contratos, se completa al cargar. `UID` pasa a ser siempre mayor que cualquier id existente.
- **Texto:** "¡A entrenar completado!" pasa a ser "¡Entrenamiento completado!".
- **Código muerto o incorrecto que he quitado o corregido:**
  - el bloque `if(false){…}` de `drawWorld`;
  - `z!==8||true`;
  - `baseSp`, que no se usaba;
  - un valor por defecto imposible en `zoneTeam`;
  - el comentario de cabecera duplicado;
  - el comentario de la lluvia, que decía "−25 % velocidad" y no es lo que hace el código;
  - `txLast||-9` pasa a `??`, porque con `||` el 0 se trataba como "vacío".

## Jugabilidad de los partidos (segunda tanda)

Queja: los partidos se hacían largos, difíciles, aburridos y "raros". Lo que se medía antes:
- **Duelos:** unos 80 por partido, y cada uno abría la pantalla de elegir acción.
- **Duración:** unos 7 minutos sin tocar nada, porque cada parte duraba 180 s.
- **Tu jugador con balón:** se quedaba quieto hasta que se lo robaban.
- **Tiros:** en una partida de prueba, 17 tiros desde fuera del área y 0 goles.

| Cambio | Antes | Ahora |
|---|---|---|
| Duración de cada parte | 180 s | 100 s. El partido completo, sin tocar nada, pasa de ~7 min a ~4 min. |
| Duelos | Siempre con pantalla (~10 pantallas por partido sin tocar nada) | Se resuelven solos en el campo con la mejor acción (mismas stats y tipos) y un texto flotante, p. ej. "Regate 64 %". La pantalla de elegir solo sale cerca de un área y como mucho una vez cada 15 s (2-6 por partido). |
| Jugador con balón | Quieto si no dibujas una ruta | Avanza solo hasta dentro del área rival y se abre en diagonal si tiene un rival delante. Arrastrar sigue marcando la ruta. |
| Saque inicial | Te podían robar nada más sacar | El que saca es intocable 2 s. |
| Pases | Tocar el campo pasaba al punto exacto | Si tocas cerca de un compañero, el pase va a él. |
| Tiro | Zona de toque pequeña y sin aviso | Zona más grande, y la portería parpadea con "¡TOCA LA PORTERÍA PARA TIRAR!" cuando estás a tiro. |
| Pantalla de tiro | Siempre había que pulsar "Tiro normal" | Si no tienes supertécnicas, se tira directamente. La animación de un tiro normal es más corta. |
| Ritmo | Velocidad 0,75 y pase 105 | Velocidad 0,9 y pase 125 |
| Probabilidad de tiro | base 28 | base 29, recalibrada para la nueva duración |

Simulación IA contra IA (100 partidos por nivel, pantalla de móvil): 1,6 / 2,2 / 2,1 goles por partido en los niveles de IA 1 / 2 / 3. El objetivo es 2-3.

Arreglos que salieron al probar:
- **Duelos en pantallas grandes:** el radio de duelo no crecía con el campo. En pantallas grandes, los defensores de la IA agresiva presionaban desde fuera del radio y no llegaba a haber duelos. Ahora el radio crece con el tamaño del campo.
- **Modo prueba:** fallaba si se abría sin partida guardada (`computeUnlocked` se ejecutaba antes de generar el mundo).
- **Bucle de dibujo:** un paso de tiempo negativo podía romper el dibujo del balón. Ahora se limita a 0.

## Detectado pero sin cambiar: decides tú

- **Balance:** simulé 200 partidos IA contra IA y salen 3,35 goles y 15,6 tiros por partido. El comentario de `BALANCE` dice que está calibrado en unos 2,6 goles y 13 tiros, con un objetivo de 2-3 goles. Para volver a ese rango, se podría bajar `shot.base` de 28 a unos 24 y volver a simular (Modo prueba → "Simular 50 partidos").
- **Datos que no usa nadie**, restos del sistema de actos anterior:
  - `DATA.missions` (17 misiones);
  - `zones[].missions`;
  - `teams.kuadrillachula` y `teams.remeros`;
  - `story.act1End`, `story.firmasDone` y `story.unlock`;
  - los campos de estado `a1`, `a2`, `a1Targets`, `firmas`, `ms` y `capDone`.
- **Herramientas de prueba a la vista:** el Modo prueba se abre tocando 5 veces el título (da +1000 fichas, permite saltar actos…) y `window.G` queda accesible. Son útiles para depurar, pero conviene quitarlos antes de publicar.
- **Desierto sin rara especial:** es el único barrio sin entrada en `DATA.specialRare`, porque ninguna de sus criaturas nuevas es rara.
- **Estadística "fuera":** en la simulación sale siempre 0; los saques de banda prácticamente no ocurren.
- **Zoom bloqueado:** `user-scalable=no` impide ampliar la página, lo que afecta a la accesibilidad.
- **Fuente:** Pixelify Sans se descarga de Google Fonts; sin conexión se usa una monoespaciada.

## Pruebas hechas en el navegador (servidor local)

- La página carga sin errores en la consola.
- El nombre se escribe con teclado físico.
- Se pueden abrir 400 paneles seguidos y después hacer un fichaje: los botones responden y `OV()` ya no los rompe.
- En la pantalla "repetido", B y Escape ya no la cierran. La experiencia aparece desactivada en Nv 50. Traspasar y quedársela funcionan.
- Abandonar un partido da 0 fichas y 0 de experiencia.
- El aviso de página del álbum sale al volver al mapa.
- Una doble evolución muestra los mensajes correctos.
- Una partida guardada en acto 0 / tut 5 se recupera y pasa a la liga (acto 3).
- El entrenamiento del prólogo funciona con el inicial en el txoko.
- El fichaje completo del prólogo funciona: hablar, invitar y firmar el contrato.
- 200 partidos simulados, en los tres niveles de IA, sin errores.
- Los 28 minijuegos aguantan 300 frames con toques aleatorios sin errores.
- El mapa se dibuja en los 8 barrios y en Lasesarre, con criaturas visibles.
- Con la ventana a 0×0 ya no hay errores.

No he hecho una partida humana completa de principio a fin, ni he probado en un móvil real.
