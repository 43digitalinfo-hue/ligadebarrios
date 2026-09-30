# Sprites necesarios · Liga de Barrios de Barakaldo

He revisado el código entero de `liga-barrios-barakaldo.html` para ver qué se dibuja con imágenes y qué sigue dibujado a mano, píxel a píxel, con `fillRect`. La lista compara ese inventario con lo que suele llevar un juego de este tipo: un RPG de criaturas con vista cenital, al estilo Pokémon, más partidos de fútbol arcade.

Leyenda de prioridad:
- **P1**: imprescindible.
- **P2**: mejora mucho el acabado.
- **P3**: extra.

Los tamaños son los del motor. Las casillas del mundo miden 16×16, las criaturas 32×32 (se reducen a 24 en el partido) y las personas 16×28.

## 1. Lo que ya está hecho con PixelLab

| Grupo | Cantidad | Estado |
|---|---|---|
| Criaturas: formas base y evoluciones | 87 | ✅ 32×32 |
| Objetos del mapa: balón, escalera, grafiti, pieza, cofre, oveja, txoko, brillo | 8 | ✅ 16×16 |
| Personas: plantilla recoloreable, 4 direcciones y pasos | 1 plantilla (12 fotogramas) | ✅ 16×28 |
| Ramiro y el Capataz | 2 × 4 direcciones | ✅ 16×28 |
| Efectos especiales animados (sección 7) | 10 × 7 fotogramas | ✅ 32×32 |

## 2. Mundo: casillas del suelo (hoy son 100 % código)

El mapa mide 90×90 casillas: 8 barrios y Lasesarre en el centro. `ground()` dibuja los tipos de casilla siguientes.

| Código | Qué es | Variantes necesarias | Prioridad |
|---|---|---|---|
| `,` | Hierba | 8 variantes por paleta de barrio (4 paletas: urbano, monte, ría, industrial) y con flores | P1 |
| `.` | Acera o baldosa | Autotile de 16 bordes (junto a carretera) | P1 |
| `=` | Carretera | Asfalto, línea discontinua horizontal y vertical, paso de cebra, cruce. En el monte es camino de tierra | P1 |
| `~` | Agua de la ría | 4 fotogramas animados más bordes de espuma (arriba, izquierda, derecha) | P1 |
| `_` | Arena u orilla | 4 variantes, con conchas y con borde mojado | P1 |
| `B` | Puente de madera | Tramo horizontal y vertical, barandilla | P1 |
| `"` `^` | Hierba alta y helecho (zonas de encuentro) | 2 fotogramas de viento, más la capa frontal que tapa los pies | P1 |
| `%` | Solar industrial con chatarra | 6 variantes | P2 |
| `F` | Campo de fútbol del barrio | Autotile de césped con líneas (bordes, centro, área) | P1 |
| `R` | Roca | 2 variantes | P2 |
| `P` | Cumbre con bandera | 2 fotogramas | P2 |
| `V` | Valla o barrera entre barrios | Cerrada y abierta | P1 |
| `S` | Cartel de madera | 1 | P2 |
| `O` | Obra de Ramiro (hormigonera y conos) | 1, mejor animada | P2 |
| `Y` | Seto o arbusto (entrada al rincón secreto) | 1 | P2 |

## 3. Mundo: árboles, edificios y mobiliario

| Elemento | Detalle | Prioridad |
|---|---|---|
| Árbol | Tronco de 16×16 y copa de 20×20 encima. 3 frondosos y 1 pino de monte. Versión en otoño opcional | P1 |
| Edificio «pisos» (urbano) | Kit modular: tejado, pared con ventanas, esquina izquierda y derecha, base, portal. 2 paletas | P1 |
| Edificio «nave» (industrial) | Tejado de chapa, pared ondulada, persiana metálica, chimenea con humo animado | P1 |
| Edificio «caserío» (monte) | Tejado de teja, entramado de madera, balcón, contraventanas verdes | P1 |
| Estadio de Lasesarre | Fachada, gradas vistas desde fuera, entrada `E` | P1 |
| Bar del barrio | Toldo de rayas, puerta, letrero «BAR» | P1 |
| Casa del jugador | Puerta distinta, felpudo | P2 |
| Farola `l` | Día y noche (halo de luz) | P1 |
| Banco `n` | 1 | P2 |
| Contenedores `c` | Verde, amarillo y azul | P2 |
| Maceta o planta `p` | 1 | P3 |
| Detalles de ambiente | Buzón, fuente, bolardo, bicicleta aparcada, tendedero, pintxos en la barra | P3 |

## 4. Personajes y retratos

| Elemento | Detalle | Prioridad |
|---|---|---|
| Capitanes de los 8 barrios (Asier, Josu, Ainhoa, Koldo, Maite, Leire, Patxi, Edurne) | Hoy usan la plantilla recoloreada. Un sprite propio por capitán, en 4 direcciones y andando | P1 |
| Entrenador, Txema (comentarista), mentor | Sprite propio | P2 |
| Retratos para los diálogos (48×48 o 64×64) | Los 8 capitanes, Ramiro, el Capataz, Txema, el entrenador y el protagonista. Con 2 expresiones: normal y contento o enfadado | P1 |
| Protagonista | Animación de correr (tecla B), celebrar y quedarse quieto con respiración | P2 |
| Vecinos | 4 o 5 variantes de cuerpo (niño, aitona, amama, currela) además de la recoloración | P3 |
| Globos de emoción | «!», «?», corazón, enfado, sudor, nota musical, zzz | P1 |

## 5. Partido

| Elemento | Detalle | Prioridad |
|---|---|---|
| Balón | 16×16, 4 fotogramas de giro, sombra aparte | P1 |
| Portería | En horizontal (izquierda y derecha) y en vertical: postes, larguero y red con 2 fotogramas de «red movida» | P1 |
| Grada con público | Bloques de 16×16 animados: sentados, saltando y con bufandas, con los colores de cada equipo | P1 |
| Vallas publicitarias | Bar Txoko, Ferretería Iñaki, Pintxos Maite… (hoy son texto) | P2 |
| Banderín de córner | 2 fotogramas | P2 |
| Banquillo con suplentes | 1 | P2 |
| Criaturas en el campo | Además de la pose fija: andar (2 fotogramas), chutar, parar o estirarse, caer aturdido y celebrar. Se puede hacer con `animate_image` a partir del PNG actual | P1 |
| Peto o camiseta del equipo | Hoy se aplica por código sobre el sprite (sección 8). Opcional: un dorsal con número | P2 |
| Indicadores | Flecha del jugador controlado, anillo de equipo, icono de energía, icono de supertécnica | P1 |
| Marcador | Marco del marcador, reloj y escudo de cada barrio (8) | P1 |
| Árbitro | Opcional: silbato al empezar y en los goles | P3 |

## 6. Cinemáticas de supertécnicas

Hay 51 técnicas, contando las combinadas. Cada una es una animación dibujada a mano en `TFX` o `DFX`. Lo realista es crear sprites por elemento, no por técnica, y combinarlos:
- **Ya hechos:** humo, fuego, agua, rayo, hojas (madera), onda (golpe o metal), destello (magia), impacto, polvo y confeti.
- **Faltan:**
  - **P2:** viento o remolino, ola grande, gabarra, raíces, muro de hormigón, grúa o excavadora, pájaro (arrano o buitre), latxa embistiendo, rayo de tinta, flotador.
  - **P3:** txaranga, talo.
- **Fondos:** portería grande en primer plano, estadio de noche y cielo de tormenta (galerna). **P2**.

## 7. Efectos especiales (VFX)

Ya generados, 7 fotogramas de 32×32 cada uno:

| Efecto | Dónde se usa ya |
|---|---|
| polvo | Esprints, frenazos y entradas |
| impacto | Duelos, chuts y paradas |
| fuego | Técnicas de fuego |
| humo | Técnicas de humo |
| agua | Técnicas de agua y charcos con lluvia |
| rayo | Técnicas eléctricas |
| hojas | Técnicas de madera y monte |
| confeti | Goles y victorias |
| destello | Criaturas doradas, subidas de nivel, magia y paradas |
| onda | Golpes y bloqueos |

Faltan:
- **P2:** gotas de lluvia y salpicadura en el suelo, brillo de evolución (columna de luz), pisadas en la hierba alta, humo de chimenea, estrellas de aturdimiento.
- **P3:** fuegos artificiales para el campeón.

## 8. Interfaz

| Elemento | Detalle | Prioridad |
|---|---|---|
| Iconos de tipo | Callejero, Currela, Ría y Monte (16×16) | P1 |
| Insignias de los 8 barrios | Oveja, remo, spray, cangrejo, grúa, sidra, chimenea y balón. Hoy se dibujan por código | P1 |
| Objetos de la tienda | Pintxo de tortilla, caña, botas nuevas y fichas (moneda) | P1 |
| Rareza | Común, poco común, rara, épica, legendaria, exclusiva y dorada | P2 |
| Mapa del mundo ilustrado (pantalla de mapa) | 180×200 | P2 |
| Logotipo del título | «LIGA DE BARRIOS» en píxel | P2 |
| Marco de diálogo, botones y cursor | 9-slice | P3 |

## 9. Minijuegos (28)

Todos se dibujan con rectángulos. Por minijuego, los sprites mínimos:

| Minijuego | Sprites |
|---|---|
| Pastoreo de latxas | Latxa (ya existe «oveja»), perro pastor, redil |
| Manzanas para la sidra | Manzano, manzana, cesta |
| Bajada del monte | Bici, piedras, charcos |
| Balones en la ría | Balón flotando, gancho, orilla |
| Regata | Trainera con remeros, boyas |
| Tiro al muelle | Diana, muelle |
| Pintadas | Botes de spray y pared |
| Los vecinos cotillas | Ventana con vecino asomado, cono de visión |
| Trucos de patinete | Patinete, rampa |
| Cangrejos en la orilla | Cangrejo, cubo |
| Parejas de mus | Cartas de la baraja española (reverso y 10 figuras) |
| Tanda de penaltis | Ya usa la portería del partido |
| La grúa | Grúa, contenedor, gancho |
| Atasco en el puente | 3 coches, camión |
| Sabotaje a la hormigonera | Tuberías: recta, codo y T |
| Escanciar sidra | Botella, vaso, chorro |
| Subida a la cumbre | Montañero, rocas |
| Aizkolari | Tronco, hacha, astillas |
| Soldadura | Soplete, chispas, chapa |
| Cadena de montaje | Cinta transportadora, piezas |
| Alto horno | Horno, termómetro |
| Toques de barrio | Balón, pie |
| Pintxo-pote | Pintxos (tortilla, gilda, jamón, pimiento), barra, clientes |
| El 1 contra 1 | Usa jugadores y balón |
| Capturas (calle, currela, ría y monte) | Fondos por tipo, caña de pescar, arbusto |

## 10. Orden recomendado

1. **Tileset por barrio:** hierba, acera, carretera, agua, arena y puente. Es lo que más se ve y da el salto de calidad del mapa. En PixelLab: `create_topdown_tileset` (autotiles) por paleta.
2. **Edificios modulares** (4 estilos), **árboles** y **farolas**.
3. **Partido:** balón animado, porterías, grada con público y escudos.
4. **Capitanes con sprite propio y retratos** de diálogo.
5. **Animaciones de criatura en el partido** (andar, chutar, parar, celebrar) con `animate_image` a partir de los 87 PNG.
6. **Interfaz:** iconos de tipo, insignias y objetos de la tienda.
7. **Minijuegos**, uno a uno.

**Coste aproximado** en PixelLab. Quedan unas 4.400 generaciones.

| Paso | Generaciones |
|---|---|
| 1 | 150-250 |
| 2 | 100-150 |
| 3 | 40 |
| 4 | 150 |
| 5 | Unas 350 (87 × 4 animaciones, 1 generación cada una) |
| 6 | 60 |
| 7 | Entre 300 y 500 |
| **Total** | **Unas 1.300** |
