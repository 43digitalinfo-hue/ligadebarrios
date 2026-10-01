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

## Tercera tanda: Feria, minijuegos y limpieza

- **Feria nueva:** tragaperras, mus, dados del mentiroso, gancho, sokatira, frontón y chapas. Premios en fichas y criaturas, con tope diario y rara asegurada.
- **Minijuegos:** capa común de "sensación de juego" (cuenta atrás, puntos flotantes, rachas, medalla en vivo, temblor y destello al fallar) y rediseño visual de los 24.
  Cambios de jugabilidad: cotillas con límite de 60 s; parejas de mus con unos segundos para memorizar; cangrejo dorado (+3); grúa con bonus de PERFECTO;
  atasco con arrastre suave; cumbre con suelo de salida, muelles y tablas que se rompen; primer toque más fácil en toques.
- **Supertécnicas:** tiras de VFX nuevas generadas en el propio juego (ola, tinta, sombra, chispas, rayas, spray, roca, acero, hormigón, sonido, madera, lana, viento y ruedas). Cada tema usa ya la suya.
- **Poses en el partido:** balanceo al andar, inclinación al chutar o pasar, saltos con giro al celebrar, tambaleo con estrellas al quedar aturdido y estela en la estirada del portero.
- **Herramientas de prueba:** el Modo prueba y `window.G` solo existen con `?debug` en la URL.
- **Datos sin uso borrados:** `DATA.missions`, `zones[].missions`, `teams.kuadrillachula` y `teams.remeros`, `story.act1End`, `story.firmasDone` y `story.unlock`, y los campos de estado `a1`, `a2`, `a1Targets`, `firmas` y `ms`. También las funciones `duelScreen`, `shootR` y `winsCount`, que nadie llamaba.

## Cuarta tanda: joystick del partido y vibración

- **Joystick que se quedaba pegado:** si soltabas el dedo fuera del partido (pantalla de tiro, pausa), el joystick viejo seguía vivo. Tu jugador seguía corriendo y no podías coger otro. Ahora el juego sabe qué dedos siguen en la pantalla: al soltar se libera siempre, y un joystick huérfano se descarta al volver a tocar. Si el navegador cancela un toque, solo se suelta ese dedo y no el del joystick.
- **Joystick más fino:** zona muerta más pequeña, a media carrera ya vas a tope, y si arrastras más allá del borde la base sigue al dedo, así que no hay que volver atrás para cambiar de dirección.
- **Vibración** (Android; iOS no la permite): al coger el joystick, al llegar al borde, en pases, tiros, goles, entradas ganadas o perdidas, postes, supertécnicas y botones del partido. En los minijuegos vibra con cada golpe o fallo. Se activa o desactiva en el título, en el Menú y en la Pausa ("Vibración: sí/no").

## Quinta tanda: entrenamientos, partido más lejos, supertécnicas y rendimiento (móvil)

- **Entrenamientos como minijuegos de 3 intentos:** penaltis (eliges lado y paras la barra de potencia; en la zona verde es gol salvo que el portero adivine, y a la escuadra entra siempre), regate (amagas y sales por el lado libre a tiempo) y paradas (el rival mira a un lado, a veces de farol; si te lanzas antes de tiempo, cambia de lado). Juegas con tu propia criatura y sus estadísticas influyen. 3 aciertos = oro, 2 = plata, 1 = bronce, 0 = nada y 0 de experiencia. La dificultad sube con el nivel. Se ha quitado el entrenamiento antiguo.
- **Partido más lejos en el móvil:** la cámara del partido se aleja (más campo, jugadores más pequeños); la pantalla de tiro vuelve a acercarse para verla bien.
- **Supertécnicas con más detalle:** presentación con rayos giratorios, franja diagonal, la criatura entrando con contorno de color, partículas de energía y cartel con el nombre y estrellas por nivel. En la ejecución: viñeta del color de la técnica, estela del balón, ondas expansivas, sacudida y vibración; en el resultado, estallido de rayos.
- **Rendimiento:** el mapa se pinta por bloques ya dibujados (solo se redibujan las baldosas animadas); la capa de texto solo borra la zona usada; el postproceso reutiliza memoria. Si el móvil va por debajo de ~25 fps durante 3 s en el mapa o el partido, se desactiva solo el postproceso ("Modo fluido"). Con la CPU frenada ×4, el mapa pasa de 8,7 a 18,5 fps y el partido de 12 a 28 fps.
- **Prealineación en horizontal:** tarjetas más compactas; los cinco titulares caben sin desplazar.

## Sexta tanda: más espacio, ritmo más tranquilo, portero y cortes

- **Más espacio en el partido (móvil):** el campo ocupa más píxeles y los jugadores se dibujan a 24 px, así que se ven más pequeños respecto al campo (en un móvil de 844×390, el ancho del campo pasa de unas 8,5 a unas 12,5 veces la altura de un jugador). Además, las distancias del juego (presión, entradas, separación) se miden como si el campo fuera un 15 % mayor: hay más hueco entre jugadores.
- **Ritmo más lento:** los jugadores tardan alrededor de un 15 % más en recorrer el campo. Los pases van un 6 % más lentos, así que da tiempo a pensarlos sin que se los coman. En 100 partidos simulados salen unos 3,1 goles y 9,6 tiros por partido.
- **Portero:** ya no sale a hacer entradas ni entra en duelos. Se queda en su portería colocándose según el balón, solo recoge balones sueltos dentro del área pequeña y para los tiros.
- **Supertécnicas del portero y de los defensas:** al elegir la parada o el bloqueo se ve el % de parar con cada opción.
- **Corte:** cuando un defensor tuyo llega a un rival con balón cerca de tu área, a veces salta una transición "¡CORTE IMPORTANTE!" o, muy cerca de la portería, "¡CORTE VALOR GOL!". Eliges entre la entrada normal y las supertécnicas de bloqueo (cada una con su %). Después se ve la animación de la técnica y "¡CORTE!" o "¡SE ESCAPA!". Pulsando ★ al ir a robar, el defensor con técnica fuerza el corte. Como mucho sale uno cada 20 s.

## Séptima tanda: lo que salió al probar el partido en el móvil

Probado con un jugador automático que usa el joystick y los botones táctiles (6 partidos antes de los cambios y 2 después).

- **Botones fuera del campo (horizontal):** PASE, TIRO y ★ van en una columna a la derecha y el campo se desplaza a la izquierda. Antes tapaban la portería rival. El campo mide lo mismo en 844×390 y un 3 % menos en 740×360.
- **Presión en el área:** dentro de su área siempre presionan dos defensas al que lleva el balón. Antes podías quedarte quieto en la línea de gol más de 9 s sin que nadie te entrase, porque el portero ya no sale.
- **Eliges la parada más a menudo:** si tu portero puede pagar una supertécnica y el tiro rival viene de cerca, se abre su pantalla con el % de cada opción. Antes salía en 1 de cada 6 tiros rivales; ahora, en unos 7 por partido.
- **Pase asistido:** el pase busca compañero con un margen de ±55° (antes ±37°) y evita las líneas tapadas. Un aro amarillo marca a quién va el pase mientras apuntas. Pases perdidos: de ~50-70 % a ~20-25 %.
- **Entrada:** un aro naranja marca al rival con balón cuando está a tu alcance.
- **Tiro:** el botón TIRO lleva un aro verde, amarillo o rojo según la calidad de la posición, y el aviso "¡TIRO!" muestra el % aproximado. Dentro de rango, el tiro sale al pulsar y no al soltar.
- **Partes de 60 s** (antes 45): más jugadas ahora que el ritmo es más tranquilo. En 100 partidos simulados salen 4,1 goles y 14,6 tiros por partido.

## Detectado pero sin cambiar: decides tú

- **Balance:** simulé 200 partidos IA contra IA y salen 3,35 goles y 15,6 tiros por partido. El comentario de `BALANCE` dice que está calibrado en unos 2,6 goles y 13 tiros, con un objetivo de 2-3 goles. Para volver a ese rango, se podría bajar `shot.base` de 28 a unos 24 y volver a simular (Modo prueba → "Simular 50 partidos").
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

- Tercera tanda: carga sin errores con y sin `?debug`; 100 partidos simulados (3,98 goles y 12,4 tiros de media); los 24 minijuegos jugados hasta el final en tres dificultades con toques aleatorios, sin errores; atasco resuelto con arrastre; pruebas de interfaz de frontón (7), chapas (6) y sokatira (6) superadas en escritorio y móvil.

- Quinta tanda: carga sin errores; joystick, flujo de partida nueva en móvil, partido táctil, minijuegos (incluidos los 3 entrenamientos en tres dificultades), feria en móvil y escritorio, frontón, chapas y sokatira superados sin errores.

No he hecho una partida humana completa de principio a fin, ni he probado en un móvil real.
