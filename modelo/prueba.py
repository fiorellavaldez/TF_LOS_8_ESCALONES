from preguntaDesempate import preguntaDesempate 
from preguntaRonda import preguntaRonda
import random
from Escalon import Escalon
from Partida import Partida
from Jugador import Jugador
from Tema import Tema

################################################# boceto de lo queseria una partida

#iniciaria el juego nuevo pidiendo a la base de datos una lista con los temas disponibles para jugar

jugador1 = Jugador("j1","1")
jugador2 = Jugador("j2","2")
jugador3 = Jugador("j3","3")
jugador4 = Jugador("j4","4")
jugador5 = Jugador("j5","5")
jugador6 = Jugador("j6","6")
jugador7 = Jugador("j7","7")
jugador8 = Jugador("j8","8")
jugador9 = Jugador("j9","9")

listaJugadores = [jugador1,jugador2, jugador3,jugador4,jugador5,jugador6,jugador7,jugador8,jugador9] #lista de jugadores completa


listaTemas = []

# listaTemas.cargarTemas() #este "cargarTemas " baja todos los temas disponibles con todas sus preguntas <------- LOCOMENTAMOS

#Seleccionamos 8 temas para cada escalon

#tema1 = Tema(1,1)
#tema2 = Tema(2,2)
#tema3 = Tema(3,3)
#tema4 = Tema(4,4)
#tema5 = Tema(5,5)
#tema6 = Tema(6,6)
#tema7 = Tema(7,7)
#tema8 = Tema(8,8)
#tema9 = Tema(9,9)

# Instanciamos el tema Historia
tema_historia = Tema(1, "Historia")

# Creamos las preguntas de ronda
preguntas_ronda = [
    preguntaRonda("Historia", "¿En qué año comenzó la Segunda Guerra Mundial?", "1935", "1939", "1941", "1945", "B"),
    preguntaRonda("Historia", "¿Quién fue el primer presidente de los Estados Unidos?", "Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams", "B"),
    preguntaRonda("Historia", "¿En qué año cayó el Muro de Berlín?", "1985", "1987", "1989", "1991", "C"),
    preguntaRonda("Historia", "¿Quién descubrió América?", "Cristóbal Colón", "Hernán Cortés", "Fernando de Magallanes", "Américo Vespucio", "A"),
    preguntaRonda("Historia", "¿En qué año fue la Revolución Francesa?", "1787", "1789", "1791", "1793", "B"),
    preguntaRonda("Historia", "¿Cuál fue el país que inició la Primera Guerra Mundial?", "Alemania", "Austria-Hungría", "Francia", "Rusia", "B"),
    preguntaRonda("Historia", "¿Quién escribió 'El Príncipe'?", "Platón", "Aristóteles", "Maquiavelo", "Sócrates", "C"),
    preguntaRonda("Historia", "¿En qué año se firmó la Constitución de los Estados Unidos?", "1776", "1787", "1791", "1801", "B"),
    preguntaRonda("Historia", "¿Quién fue el líder de la revolución bolchevique en Rusia?", "Stalin", "Trotsky", "Lenin", "Kruschev", "C"),
    preguntaRonda("Historia", "¿Qué país fue invadido por Alemania para iniciar la Segunda Guerra Mundial?", "Francia", "Polonia", "Bélgica", "Noruega", "B"),
    preguntaRonda("Historia", "¿En qué siglo se produjo la Revolución Industrial?", "XV", "XVI", "XVIII", "XIX", "D"),
    preguntaRonda("Historia", "¿En qué año se independizó Estados Unidos?", "1776", "1789", "1812", "1865", "A"),
    preguntaRonda("Historia", "¿Quién fue el emperador romano cuando comenzó la construcción del Coliseo?", "Nerón", "Vespasiano", "Tito", "Trajano", "B"),
    preguntaRonda("Historia", "¿Qué conflicto fue conocido como 'La Guerra Fría'?", "Guerra Civil Española", "Conflicto entre la URSS y EE.UU.", "Primera Guerra Mundial", "Guerra de Vietnam", "B"),
    preguntaRonda("Historia", "¿En qué año comenzó la Revolución Rusa?", "1914", "1917", "1921", "1939", "B"),
    preguntaRonda("Historia", "¿Quién fue el líder del Movimiento de Independencia de la India?", "Mahatma Gandhi", "Jawaharlal Nehru", "Bhagat Singh", "Subhas Chandra Bose", "A"),
    preguntaRonda("Historia", "¿En qué batalla fue derrotado Napoleón Bonaparte?", "Batalla de Trafalgar", "Batalla de Austerlitz", "Batalla de Leipzig", "Batalla de Waterloo", "D"),
    preguntaRonda("Historia", "¿En qué año terminó la Guerra de Vietnam?", "1965", "1970", "1973", "1975", "D")
]

# Añadimos las preguntas de ronda al tema historia
tema_historia.set_preguntasRonda(preguntas_ronda)

# Creamos una pregunta de desempate
pregunta_desempate = preguntaDesempate("Historia", "¿En qué año se firmó el Tratado de Versalles?", 1919)

# Añadimos la pregunta de desempate al tema historia
tema_historia.set_preguntasDesempate([pregunta_desempate])

# Marcamos el tema como disponible ya que tiene preguntas
tema_historia.set_disponible(True)

#-------------------------------------------------------------------------------------------------------------------------

# Instanciamos el tema Deportes
tema_deportes = Tema(2, "Deportes")

# Creamos las preguntas de ronda
preguntas_ronda_deportes = [
    preguntaRonda("Deportes", "¿Cuántos jugadores hay en un equipo de fútbol?", "9", "10", "11", "12", "C"),
    preguntaRonda("Deportes", "¿En qué año se celebraron los primeros Juegos Olímpicos modernos?", "1892", "1896", "1900", "1904", "B"),
    preguntaRonda("Deportes", "¿Quién tiene el récord de más goles en la historia del fútbol?", "Pelé", "Lionel Messi", "Cristiano Ronaldo", "Diego Maradona", "C"),
    preguntaRonda("Deportes", "¿En qué deporte se usa una raqueta y una pelota pequeña?", "Béisbol", "Fútbol", "Tenis", "Golf", "C"),
    preguntaRonda("Deportes", "¿En qué país se celebró la Copa Mundial de Fútbol de 2018?", "Alemania", "Brasil", "Rusia", "Qatar", "C"),
    preguntaRonda("Deportes", "¿Cuál es la carrera de atletismo más corta en los Juegos Olímpicos?", "400 metros", "200 metros", "100 metros", "1500 metros", "C"),
    preguntaRonda("Deportes", "¿Cuántos puntos vale un triple en baloncesto?", "2", "3", "4", "5", "B"),
    preguntaRonda("Deportes", "¿En qué año ganó Argentina su primer Mundial de Fútbol?", "1974", "1978", "1982", "1986", "B"),
    preguntaRonda("Deportes", "¿Qué deporte practican Rafael Nadal y Roger Federer?", "Golf", "Tenis", "Atletismo", "Natación", "B"),
    preguntaRonda("Deportes", "¿En qué país se originó el baloncesto?", "Reino Unido", "Estados Unidos", "Francia", "Canadá", "D"),
    preguntaRonda("Deportes", "¿Cuántos sets hay en un partido de tenis masculino en Grand Slam?", "3", "4", "5", "6", "C"),
    preguntaRonda("Deportes", "¿Cuántos jugadores hay en un equipo de baloncesto?", "5", "7", "9", "11", "A"),
    preguntaRonda("Deportes", "¿En qué año se realizaron los primeros Juegos Olímpicos?", "1892", "1896", "1900", "1904", "B"),
    preguntaRonda("Deportes", "¿Cuál es el deporte más popular en el mundo?", "Baloncesto", "Fútbol", "Críquet", "Atletismo", "B"),
    preguntaRonda("Deportes", "¿Quién es el nadador con más medallas olímpicas?", "Michael Phelps", "Ian Thorpe", "Mark Spitz", "Ryan Lochte", "A"),
    preguntaRonda("Deportes", "¿Cuántos tiempos tiene un partido de balonmano?", "1", "2", "3", "4", "B"),
    preguntaRonda("Deportes", "¿En qué país se celebró la Copa Mundial de Rugby 2019?", "Inglaterra", "Francia", "Japón", "Australia", "C"),
    preguntaRonda("Deportes", "¿Cuánto mide una pista de atletismo en una vuelta completa?", "200 metros", "300 metros", "400 metros", "500 metros", "C")
]

# Añadimos las preguntas de ronda al tema deportes
tema_deportes.set_preguntasRonda(preguntas_ronda_deportes)

# Creamos una pregunta de desempate
pregunta_desempate_deportes = preguntaDesempate("Deportes", "¿En qué año se celebró el primer Super Bowl?", 1967)

# Añadimos la pregunta de desempate al tema deportes
tema_deportes.set_preguntasDesempate([pregunta_desempate_deportes])

# Marcamos el tema como disponible ya que tiene preguntas
tema_deportes.set_disponible(True)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# Instanciamos el tema Arte
tema_arte = Tema(3, "Arte")

# Creamos las preguntas de ronda
preguntas_ronda_arte = [
    preguntaRonda("Arte", "¿Quién pintó la Mona Lisa?", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet", "B"),
    preguntaRonda("Arte", "¿En qué ciudad se encuentra el museo del Louvre?", "Roma", "Madrid", "París", "Londres", "C"),
    preguntaRonda("Arte", "¿Qué pintor es conocido por su período azul?", "Pablo Picasso", "Salvador Dalí", "Andy Warhol", "Frida Kahlo", "A"),
    preguntaRonda("Arte", "¿Cuál es el estilo artístico de Vincent van Gogh?", "Renacimiento", "Impresionismo", "Postimpresionismo", "Surrealismo", "C"),
    preguntaRonda("Arte", "¿En qué siglo vivió el escultor Miguel Ángel?", "Siglo XIV", "Siglo XV", "Siglo XVI", "Siglo XVII", "C"),
    preguntaRonda("Arte", "¿Qué famoso pintor cortó parte de su oreja?", "Claude Monet", "Vincent van Gogh", "Edgar Degas", "Paul Cézanne", "B"),
    preguntaRonda("Arte", "¿Qué técnica utilizó Georges Seurat en su obra más famosa?", "Cubismo", "Surrealismo", "Puntillismo", "Realismo", "C"),
    preguntaRonda("Arte", "¿Qué artista es conocido por sus pinturas del ballet?", "Pablo Picasso", "Edgar Degas", "Jackson Pollock", "Gustav Klimt", "B"),
    preguntaRonda("Arte", "¿Quién pintó 'La última cena'?", "Leonardo da Vinci", "Miguel Ángel", "Rafael", "Botticelli", "A"),
    preguntaRonda("Arte", "¿Qué corriente artística sigue Salvador Dalí?", "Impresionismo", "Surrealismo", "Romanticismo", "Barroco", "B"),
    preguntaRonda("Arte", "¿Qué famoso muralista mexicano pintó 'Sueño de una tarde dominical en la Alameda Central'?", "David Alfaro Siqueiros", "Diego Rivera", "Frida Kahlo", "José Clemente Orozco", "B"),
    preguntaRonda("Arte", "¿Quién es el autor de la obra 'El Grito'?", "Edvard Munch", "Paul Gauguin", "Henri Matisse", "Claude Monet", "A"),
    preguntaRonda("Arte", "¿Qué técnica de arte utiliza tiras de papel para formar imágenes?", "Collage", "Acuarela", "Grabado", "Escultura", "A"),
    preguntaRonda("Arte", "¿Cuál de estos artistas es conocido por el uso de latas de sopa en su obra?", "Pablo Picasso", "Salvador Dalí", "Andy Warhol", "Jackson Pollock", "C"),
    preguntaRonda("Arte", "¿En qué país nació el pintor surrealista René Magritte?", "Francia", "Bélgica", "España", "Países Bajos", "B"),
    preguntaRonda("Arte", "¿Qué pintor impresionista francés es conocido por sus pinturas de nenúfares?", "Claude Monet", "Pierre-Auguste Renoir", "Edgar Degas", "Paul Cézanne", "A"),
    preguntaRonda("Arte", "¿Qué artista pintó el mural 'Guernica'?", "Diego Rivera", "Joan Miró", "Pablo Picasso", "Francisco Goya", "C"),
    preguntaRonda("Arte", "¿Cuál es el nombre del famoso cuadro de Johannes Vermeer que muestra a una joven con un pendiente de perla?", "La joven de la perla", "La rendición de Breda", "La ronda de noche", "La dama de Armiño", "A")
]

# Añadimos las preguntas de ronda al tema arte
tema_arte.set_preguntasRonda(preguntas_ronda_arte)

# Creamos una pregunta de desempate
pregunta_desempate_arte = preguntaDesempate("Arte", "¿En qué año nació el pintor Pablo Picasso?", 1881)

# Añadimos la pregunta de desempate al tema arte
tema_arte.set_preguntasDesempate([pregunta_desempate_arte])

# Marcamos el tema como disponible ya que tiene preguntas
tema_arte.set_disponible(True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Instanciamos el tema Geografía
tema_geografia = Tema(4, "Geografía")

# Creamos las preguntas de ronda
preguntas_ronda_geografia = [
    preguntaRonda("Geografía", "¿Cuál es el río más largo del mundo?", "Nilo", "Amazonas", "Yangtsé", "Misisipi", "B"),
    preguntaRonda("Geografía", "¿En qué continente se encuentra el desierto del Sahara?", "Asia", "América", "África", "Oceanía", "C"),
    preguntaRonda("Geografía", "¿Cuál es la capital de Australia?", "Sídney", "Melbourne", "Canberra", "Brisbane", "C"),
    preguntaRonda("Geografía", "¿Cuál es el país más grande del mundo?", "Canadá", "China", "Rusia", "Estados Unidos", "C"),
    preguntaRonda("Geografía", "¿Cuántos océanos existen en el planeta?", "3", "4", "5", "6", "C"),
    preguntaRonda("Geografía", "¿En qué país se encuentra la Torre Eiffel?", "Alemania", "Italia", "España", "Francia", "D"),
    preguntaRonda("Geografía", "¿Cuál es la capital de Japón?", "Kioto", "Tokio", "Osaka", "Nagasaki", "B"),
    preguntaRonda("Geografía", "¿Qué cordillera separa Europa de Asia?", "Himalaya", "Alpes", "Andes", "Urales", "D"),
    preguntaRonda("Geografía", "¿Cuál es el país con más población en el mundo?", "Estados Unidos", "India", "China", "Brasil", "C"),
    preguntaRonda("Geografía", "¿Qué país tiene la forma de una bota?", "Grecia", "Italia", "España", "Portugal", "B"),
    preguntaRonda("Geografía", "¿Cuál es el mar más grande del mundo?", "Mar Mediterráneo", "Mar Rojo", "Mar Caribe", "Mar de Filipinas", "D"),
    preguntaRonda("Geografía", "¿En qué país se encuentra el monte Kilimanjaro?", "Kenia", "Tanzania", "Sudáfrica", "Zimbabue", "B"),
    preguntaRonda("Geografía", "¿Cuál es la capital de Canadá?", "Toronto", "Montreal", "Ottawa", "Vancouver", "C"),
    preguntaRonda("Geografía", "¿En qué país se encuentra la ciudad de Estambul?", "Grecia", "Turquía", "Egipto", "Israel", "B"),
    preguntaRonda("Geografía", "¿Cuál es la montaña más alta del mundo?", "Monte Everest", "K2", "Mont Blanc", "Monte McKinley", "A"),
    preguntaRonda("Geografía", "¿Cuál es el país más pequeño del mundo?", "Liechtenstein", "San Marino", "Mónaco", "Vaticano", "D"),
    preguntaRonda("Geografía", "¿Qué país tiene más islas?", "Noruega", "Indonesia", "Suecia", "Filipinas", "C"),
    preguntaRonda("Geografía", "¿Cuál es el río más largo de Europa?", "Danubio", "Rin", "Volga", "Támesis", "C")
]

# Añadimos las preguntas de ronda al tema geografía
tema_geografia.set_preguntasRonda(preguntas_ronda_geografia)

# Creamos una pregunta de desempate
pregunta_desempate_geografia = preguntaDesempate("Geografía", "¿En qué año fue fundada la ciudad de Roma?", 753)

# Añadimos la pregunta de desempate al tema geografía
tema_geografia.set_preguntasDesempate([pregunta_desempate_geografia])

# Marcamos el tema como disponible ya que tiene preguntas
tema_geografia.set_disponible(True)

#------------------------------------------------------------------------------------------------------------------------------------------------

# Instanciamos el tema Ciencia
tema_ciencia = Tema(5, "Ciencia")

# Creamos las preguntas de ronda
preguntas_ronda_ciencia = [
    preguntaRonda("Ciencia", "¿Qué planeta es conocido como el planeta rojo?", "Marte", "Venus", "Júpiter", "Saturno", "A"),
    preguntaRonda("Ciencia", "¿Cuál es la sustancia química principal en los huesos?", "Oxígeno", "Hierro", "Calcio", "Potasio", "C"),
    preguntaRonda("Ciencia", "¿Qué tipo de animal es una ballena?", "Pez", "Mamífero", "Anfibio", "Reptil", "B"),
    preguntaRonda("Ciencia", "¿Cuál es el elemento más abundante en la Tierra?", "Hierro", "Nitrógeno", "Oxígeno", "Silicio", "C"),
    preguntaRonda("Ciencia", "¿Qué gas es necesario para que las células respiren?", "Oxígeno", "Nitrógeno", "Hidrógeno", "Dióxido de carbono", "A"),
    preguntaRonda("Ciencia", "¿Cuál es el órgano más grande del cuerpo humano?", "Corazón", "Cerebro", "Piel", "Hígado", "C"),
    preguntaRonda("Ciencia", "¿Cuál es la unidad básica de la vida?", "Átomo", "Tejido", "Célula", "Molécula", "C"),
    preguntaRonda("Ciencia", "¿Qué científico propuso la teoría de la relatividad?", "Newton", "Einstein", "Tesla", "Darwin", "B"),
    preguntaRonda("Ciencia", "¿Qué sustancia se obtiene al combinar sodio y cloro?", "Agua", "Sal", "Amoníaco", "Bicarbonato", "B"),
    preguntaRonda("Ciencia", "¿Cuál es el proceso por el cual las plantas producen su alimento?", "Digestión", "Fotosíntesis", "Respiración", "Transpiración", "B"),
    preguntaRonda("Ciencia", "¿Qué partícula subatómica tiene carga positiva?", "Electrón", "Neutrón", "Protón", "Positrón", "C"),
    preguntaRonda("Ciencia", "¿Cuál es el metal más liviano?", "Plata", "Litio", "Mercurio", "Hierro", "B"),
    preguntaRonda("Ciencia", "¿Qué tipo de animal es un tiburón?", "Pez", "Mamífero", "Anfibio", "Reptil", "A"),
    preguntaRonda("Ciencia", "¿Cuál es la distancia de la Tierra al Sol?", "93 millones de millas", "120 millones de millas", "80 millones de millas", "100 millones de millas", "A"),
    preguntaRonda("Ciencia", "¿Cuál es el gas más abundante en la atmósfera terrestre?", "Oxígeno", "Dióxido de carbono", "Nitrógeno", "Hidrógeno", "C"),
    preguntaRonda("Ciencia", "¿Quién es conocido como el padre de la genética?", "Einstein", "Newton", "Mendel", "Darwin", "C"),
    preguntaRonda("Ciencia", "¿Qué tipo de roca se forma por el enfriamiento del magma?", "Sedimentaria", "Ígnea", "Metamórfica", "Volcánica", "B"),
    preguntaRonda("Ciencia", "¿Cuál es el compuesto químico del agua?", "H2O2", "CO2", "H2O", "CH4", "C")
]

# Añadimos las preguntas de ronda al tema ciencia
tema_ciencia.set_preguntasRonda(preguntas_ronda_ciencia)

# Creamos una pregunta de desempate
pregunta_desempate_ciencia = preguntaDesempate("Ciencia", "¿En qué año se descubrió el electrón?", 1897)

# Añadimos la pregunta de desempate al tema ciencia
tema_ciencia.set_preguntasDesempate([pregunta_desempate_ciencia])

# Marcamos el tema como disponible ya que tiene preguntas
tema_ciencia.set_disponible(True)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Instanciamos el tema Entretenimiento
tema_entretenimiento = Tema(6, "Entretenimiento")

# Creamos las preguntas de ronda
preguntas_ronda_entretenimiento = [
    preguntaRonda("Entretenimiento", "¿Cuál es el nombre del mago en 'El Señor de los Anillos'?", "Gandalf", "Saruman", "Radagast", "Sauron", "A"),
    preguntaRonda("Entretenimiento", "¿Qué actor interpretó a Jack Sparrow en 'Piratas del Caribe'?", "Johnny Depp", "Orlando Bloom", "Brad Pitt", "Tom Cruise", "A"),
    preguntaRonda("Entretenimiento", "¿Cómo se llama el país ficticio en 'Pantera Negra'?", "Gondor", "Wakanda", "Narnia", "Zamunda", "B"),
    preguntaRonda("Entretenimiento", "¿En qué película aparece el personaje 'Buzz Lightyear'?", "Monsters Inc.", "Toy Story", "Buscando a Nemo", "Cars", "B"),
    preguntaRonda("Entretenimiento", "¿Qué director es famoso por la película 'Inception'?", "Steven Spielberg", "Martin Scorsese", "Christopher Nolan", "Quentin Tarantino", "C"),
    preguntaRonda("Entretenimiento", "¿Cuál es el nombre del parque en 'Jurassic Park'?", "Jurassic Land", "Dinosaur World", "Jurassic Park", "Prehistoric Park", "C"),
    preguntaRonda("Entretenimiento", "¿Qué instrumento toca Lisa Simpson?", "Guitarra", "Saxofón", "Piano", "Trompeta", "B"),
    preguntaRonda("Entretenimiento", "¿Cuál es el nombre del superhéroe interpretado por Robert Downey Jr.?", "Hulk", "Iron Man", "Capitán América", "Thor", "B"),
    preguntaRonda("Entretenimiento", "¿Quién dirigió la película 'Titanic'?", "Steven Spielberg", "James Cameron", "Ridley Scott", "Peter Jackson", "B"),
    preguntaRonda("Entretenimiento", "¿Qué saga de películas cuenta la historia de un grupo de amigos que viajan a Mordor?", "Star Wars", "Harry Potter", "El Señor de los Anillos", "Narnia", "C"),
    preguntaRonda("Entretenimiento", "¿Qué personaje de dibujos animados vive en una piña bajo el mar?", "SpongeBob", "Mickey Mouse", "Bugs Bunny", "Scooby-Doo", "A"),
    preguntaRonda("Entretenimiento", "¿Qué película popular incluye una secuencia de baile de Tom Cruise en calcetines?", "Top Gun", "Cocktail", "Risky Business", "Jerry Maguire", "C"),
    preguntaRonda("Entretenimiento", "¿Cuál es el nombre de la canción principal de la película 'Frozen'?", "Let It Be", "Let It Go", "Into the Unknown", "Do You Want to Build a Snowman?", "B"),
    preguntaRonda("Entretenimiento", "¿Qué película incluye al personaje de un payaso llamado Pennywise?", "Scream", "It", "Saw", "The Conjuring", "B"),
    preguntaRonda("Entretenimiento", "¿Quién es el protagonista de la serie 'Breaking Bad'?", "Walter White", "Jesse Pinkman", "Saul Goodman", "Hank Schrader", "A"),
    preguntaRonda("Entretenimiento", "¿Qué película tiene la frase 'Hasta la vista, baby'?", "RoboCop", "Terminator 2", "The Matrix", "Mad Max", "B"),
    preguntaRonda("Entretenimiento", "¿Qué película de Disney presenta a un elefante volador?", "Bambi", "Dumbo", "El Rey León", "Tarzán", "B"),
    preguntaRonda("Entretenimiento", "¿Qué serie de televisión presenta un trono hecho de espadas?", "Game of Thrones", "Vikings", "The Witcher", "Lord of the Rings", "A")
]

# Añadimos las preguntas de ronda al tema entretenimiento
tema_entretenimiento.set_preguntasRonda(preguntas_ronda_entretenimiento)

# Creamos una pregunta de desempate
pregunta_desempate_entretenimiento = preguntaDesempate("Entretenimiento", "¿En qué año se lanzó la primera película de 'Star Wars'?", 1977)

# Añadimos la pregunta de desempate al tema entretenimiento
tema_entretenimiento.set_preguntasDesempate([pregunta_desempate_entretenimiento])

# Marcamos el tema como disponible ya que tiene preguntas
tema_entretenimiento.set_disponible(True)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Instanciamos el tema Programación
tema_programacion = Tema(7, "Programación")

# Creamos las preguntas de ronda
preguntas_ronda_programacion = [
    preguntaRonda("Programación", "¿Qué estructura de control se usa para repetir un bloque de código?", "If", "For", "Switch", "Try", "B"),
    preguntaRonda("Programación", "¿Qué lenguaje de programación es conocido por su uso en desarrollo web y scripts del lado del servidor?", "Python", "Java", "JavaScript", "C#", "C"),
    preguntaRonda("Programación", "¿Cómo se denomina una función que se llama a sí misma?", "Iterativa", "Privada", "Recursiva", "Anónima", "C"),
    preguntaRonda("Programación", "¿Cuál es el tipo de dato que representa verdadero o falso?", "Boolean", "String", "Float", "Array", "A"),
    preguntaRonda("Programación", "¿Qué significa OOP en programación?", "Optimized Operations Protocol", "Object-Oriented Programming", "Output-Oriented Process", "Option of Parameters", "B"),
    preguntaRonda("Programación", "¿Qué palabra clave en Python se utiliza para definir una función?", "def", "func", "lambda", "function", "A"),
    preguntaRonda("Programación", "¿Cuál de los siguientes es un lenguaje de programación funcional?", "Python", "JavaScript", "Haskell", "Java", "C"),
    preguntaRonda("Programación", "¿Qué símbolo se utiliza para los comentarios en Python?", "#", "//", "/* */", "<!-- -->", "A"),
    preguntaRonda("Programación", "¿Cuál es el valor que retorna una función sin una declaración de retorno explícita en Python?", "None", "0", "False", "True", "A"),
    preguntaRonda("Programación", "¿Cómo se llama el algoritmo utilizado comúnmente para ordenar una lista?", "Heap Sort", "Quick Sort", "Bubble Sort", "Merge Sort", "C"),
    preguntaRonda("Programación", "¿Qué estructura de datos sigue el principio FIFO?", "Stack", "Queue", "Array", "Tree", "B"),
    preguntaRonda("Programación", "¿En qué lenguaje está basado TypeScript?", "Python", "C++", "Java", "JavaScript", "D"),
    preguntaRonda("Programación", "¿Qué operador lógico se usa para la conjunción lógica (AND) en muchos lenguajes de programación?", "&", "||", "&&", "==", "C"),
    preguntaRonda("Programación", "¿Qué significa IDE?", "Internet Development Environment", "Integrated Debugging Emulator", "Integrated Development Environment", "Interface Design Editor", "C"),
    preguntaRonda("Programación", "¿Cuál es el tipo de error en Python que ocurre cuando se llama a una función con menos argumentos de los esperados?", "SyntaxError", "TypeError", "ValueError", "IndexError", "B"),
    preguntaRonda("Programación", "¿Qué tecnología es popular para gestionar bases de datos relacionales?", "SQL", "HTML", "JSON", "XML", "A"),
    preguntaRonda("Programación", "¿Cómo se llama el mecanismo que permite ejecutar varias tareas concurrentemente en un programa?", "Multitasking", "Multithreading", "Parallelism", "Asynchronous", "B"),
    preguntaRonda("Programación", "¿Qué paradigma de programación enfatiza el uso de funciones puras y evita los efectos secundarios?", "Imperativo", "Funcional", "Orientado a Objetos", "Declarativo", "B")
]

# Añadimos las preguntas de ronda al tema Programación
tema_programacion.set_preguntasRonda(preguntas_ronda_programacion)

# Creamos una pregunta de desempate
pregunta_desempate_programacion = preguntaDesempate("Programación", "¿En qué año se lanzó Python?", 1991)

# Añadimos la pregunta de desempate al tema Programación
tema_programacion.set_preguntasDesempate([pregunta_desempate_programacion])

# Marcamos el tema como disponible ya que tiene preguntas
tema_programacion.set_disponible(True)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Instanciamos el tema Gastronomía
tema_gastronomia = Tema(8, "Gastronomía")

# Creamos las preguntas de ronda
preguntas_ronda_gastronomia = [
    preguntaRonda("Gastronomía", "¿Qué tipo de pasta tiene forma de lazos o mariposas?", "Penne", "Fusilli", "Farfalle", "Linguini", "C"),
    preguntaRonda("Gastronomía", "¿Qué país es conocido por el platillo 'paella'?", "Italia", "España", "Francia", "Portugal", "B"),
    preguntaRonda("Gastronomía", "¿Cuál de los siguientes ingredientes es esencial para hacer un gazpacho?", "Tomate", "Pepino", "Zanahoria", "Papa", "A"),
    preguntaRonda("Gastronomía", "¿Qué tipo de queso se utiliza comúnmente en una pizza margarita?", "Cheddar", "Parmesano", "Mozzarella", "Provolone", "C"),
    preguntaRonda("Gastronomía", "¿Cuál es la principal especia utilizada en el curry?", "Canela", "Comino", "Cúrcuma", "Pimienta", "C"),
    preguntaRonda("Gastronomía", "¿De qué animal se obtiene el 'prosciutto'?", "Cerdo", "Vaca", "Cordero", "Cabra", "A"),
    preguntaRonda("Gastronomía", "¿Qué tipo de harina se usa comúnmente para hacer pasta?", "Harina de arroz", "Harina de trigo", "Harina de maíz", "Harina de garbanzo", "B"),
    preguntaRonda("Gastronomía", "¿Qué tipo de cocción implica sumergir los alimentos en agua hirviendo?", "Asar", "Freír", "Hervir", "Grillar", "C"),
    preguntaRonda("Gastronomía", "¿Cuál es el ingrediente principal del hummus?", "Lentejas", "Garbanzos", "Frijoles", "Maíz", "B"),
    preguntaRonda("Gastronomía", "¿En qué país es tradicional el sushi?", "China", "Corea del Sur", "Japón", "Tailandia", "C"),
    preguntaRonda("Gastronomía", "¿Cuál es el nombre del proceso de cocción lenta al fuego bajo con humedad?", "Asar", "Guisar", "Hornear", "Freír", "B"),
    preguntaRonda("Gastronomía", "¿Qué bebida alcohólica se utiliza en la preparación de tiramisú?", "Vino tinto", "Cerveza", "Amaretto", "Ron", "C"),
    preguntaRonda("Gastronomía", "¿Cuál es el ingrediente base de la bebida conocida como 'sake'?", "Cebada", "Arroz", "Uvas", "Maíz", "B"),
    preguntaRonda("Gastronomía", "¿Cómo se llama el plato de cordero asado típico de la Patagonia argentina?", "Empanada", "Cazuela", "Asado al palo", "Matambre", "C"),
    preguntaRonda("Gastronomía", "¿Qué tipo de vinagre es común en la cocina japonesa?", "Vinagre balsámico", "Vinagre de sidra de manzana", "Vinagre de arroz", "Vinagre de vino tinto", "C"),
    preguntaRonda("Gastronomía", "¿Cuál es el término francés para cocinar con vino?", "Gratinar", "Flambear", "Pochar", "Brasear", "D"),
    preguntaRonda("Gastronomía", "¿Qué fruta es el ingrediente principal de un guacamole?", "Mango", "Tomate", "Aguacate", "Plátano", "C"),
    preguntaRonda("Gastronomía", "¿Cuál es el término culinario para cortar en tiras finas?", "Rebanar", "Brunoise", "Juliana", "Ciselar", "C")
]

# Añadimos las preguntas de ronda al tema Gastronomía
tema_gastronomia.set_preguntasRonda(preguntas_ronda_gastronomia)

# Creamos una pregunta de desempate
pregunta_desempate_gastronomia = preguntaDesempate("Gastronomía", "¿En qué año se inventó la hamburguesa moderna?", 1900)

# Añadimos la pregunta de desempate al tema Gastronomía
tema_gastronomia.set_preguntasDesempate([pregunta_desempate_gastronomia])

# Marcamos el tema como disponible ya que tiene preguntas
tema_gastronomia.set_disponible(True)

#-------------------------------------------------------------------------------------------------------------------------------

#random.shuffle(listaTemas)
lista8Temas=[tema_deportes, tema_ciencia, tema_arte, tema_entretenimiento, tema_gastronomia, tema_geografia, tema_historia, tema_programacion]

#for i in range(8):
#    lista8Temas.append(listaTemas(i))

# El escalon seria una clase en si, tendria datos como: participantes activos o eliminados, tema
escalon1 = Escalon()
escalon2 = Escalon()
escalon3 = Escalon()
escalon4 = Escalon()
escalon5 = Escalon()
escalon6 = Escalon()
escalon7 = Escalon()
escalon8 = Escalon()

#escalon1.set_jugadores(listaJugadores) # le doy la lista de jugadoes completa al primer escalon

listaEscalones = [escalon1, escalon2, escalon3, escalon4, escalon5, escalon6, escalon7, escalon8]

for i in range(8):
    listaEscalones[i].set_tema(lista8Temas[i]) # Con esto ya tengo un tema para cada escalón

partida = Partida(listaEscalones) #instanciamos el objeto partida con los 8 escalones


#for i in range (listaEscalones):
    
    #iniciamos una ronda
    #ronda1
    
    #le hacemos una pregunta a un jugador, obtenemos si acertó o no 
    #le hacemos una pregunta al siguiente y así hasta completar una pregunta a cada jugador
    
    #ronda2
    #le hacemos una pregunta a un jugador, obtenemos si acertó o no 
    #le hacemos una pregunta al siguiente y así hasta completar una pregunta a cada jugador

    #evaluamos los errores de todos los jugadores y puede suceder lo siguiente

        # TODOS BIEN: Empatan todos los jugadores contenstando bien todas las preguntas de las 2 rondas --> los jugadores van a ronda de pregutna de desempate
        
        # 2 O MAS EMPATADOS: Empatan 2 o mas jugadores en mayor cantidad de errores --> los jugadores empatados van a ronda de pregunta de desempate
        
        # Hay solo un jugador que tiene mas erradas que los demas --> se elimina ese jugador de la lista de jugadores
        
    # se hace un desempate si es necesario entre los jugadores empatados
    
    #en cualquiera de los 3 casos anteriores, se elimina un solo jugador

    # i = escalon

def hacer_pregunta(jugador, preguntas):
    """
    Simula hacer una pregunta al jugador y devuelve si acertó o no.
    :param jugador: Jugador, objeto de la clase Jugador
    :param preguntas: list, lista de preguntas disponibles
    :return: int, 1 si acertó, 2 si falló
    """
    # Aquí puedes hacer la lógica para elegir una pregunta y obtener una respuesta del jugador
    # Por ahora, simulamos respuestas aleatorias:
    import random
    resultado = random.choice([1, 2])  # 1: acertó, 2: falló
    print(f"{jugador.get_nombre()} responde {'bien' if resultado == 1 else 'mal'} en la ronda.")
    return resultado

def evaluar_jugadores(jugadores):
    """
    Evalúa los resultados de las dos rondas para determinar quiénes van a desempate o quién será eliminado.
    :param jugadores: list, lista de objetos de la clase Jugador
    :return: list, lista de jugadores que deben ir a desempate o el jugador que será eliminado
    """
    jugadores_errados = {}
    
    # Contar los errores de cada jugador (ronda 1 + ronda 2)
    for jugador in jugadores:
        errores = (jugador.get_ronda1() == 2) + (jugador.get_ronda2() == 2)
        jugadores_errados[jugador] = errores
    
    # Buscamos los jugadores con el máximo número de errores
    max_errores = max(jugadores_errados.values())
    jugadores_con_max_errores = [jugador for jugador, errores in jugadores_errados.items() if errores == max_errores]
    
    # Si todos acertaron todas las preguntas
    if max_errores == 0:
        print("Todos los jugadores acertaron, van a desempate.")
        return jugadores
    
    # Si hay empate entre dos o más jugadores con el máximo de errores
    if len(jugadores_con_max_errores) > 1:
        print(f"Empate entre {len(jugadores_con_max_errores)} jugadores con más errores.")
        return jugadores_con_max_errores
    
    # Si hay un único jugador con más errores
    print(f"{jugadores_con_max_errores[0].get_nombre()} tiene más errores y será eliminado.")
    return jugadores_con_max_errores

def hacer_desempate(jugadores, preguntas_desempate):
    """
    Simula la ronda de desempate entre los jugadores empatados.
    :param jugadores: list, lista de objetos de la clase Jugador que irán al desempate
    :param preguntas_desempate: list, lista de preguntas de desempate disponibles
    :return: list, lista de un solo jugador que será eliminado
    """
    import random

    # Hacemos preguntas de desempate a los jugadores
    respuestas = {}
    for jugador in jugadores:
        respuesta = random.randint(1, 100)  # Simulamos una respuesta numérica para la pregunta de desempate
        respuestas[jugador] = respuesta
        print(f"{jugador.get_nombre()} responde {respuesta} en la pregunta de desempate.")

    # La respuesta correcta simulada
    respuesta_correcta = random.randint(1, 100)
    print(f"La respuesta correcta era: {respuesta_correcta}")

    # Evaluamos quién estuvo más cerca
    jugador_eliminado = max(jugadores, key=lambda j: abs(respuestas[j] - respuesta_correcta))
    
    print(f"{jugador_eliminado.get_nombre()} estuvo más lejos y será eliminado.")
    return [jugador_eliminado]


#def iniciar_partida(partida):
    """
    Procedimiento que recorre los escalones de la partida, ejecutando las rondas y manejando las eliminaciones.
    :param partida: Partida, objeto que contiene los escalones y jugadores
    """
    for escalon in partida.get_escalones():
        print(f"\n--- Comenzando Escalón con tema {(escalon.get_tema()).get_nombreTema()} ---")

        # Ronda 1
        for jugador in escalon.get_jugadores():
            # Simulamos hacerle una pregunta y obtener si acertó (0: no contestó, 1: acertó, 2: falló)
            jugador.set_ronda1(hacer_pregunta(jugador, (escalon.get_tema()).get_preguntasRonda()))  # <------------------ACA NOS QUEDAMOS!!!
        
        # Ronda 2
        for jugador in escalon.get_jugadores():
            jugador.ronda2 = hacer_pregunta(jugador, (escalon.get_tema()).get_preguntasRonda())

        # Evaluamos los resultados de las dos rondas
        jugadores_a_desempatar = evaluar_jugadores(escalon.get_jugadores())
        
        # Si hay jugadores empatados (o todos acertaron), hacemos un desempate
        if len(jugadores_a_desempatar) > 1:
            print("Empate detectado. Comenzando ronda de desempate...")
            jugadores_a_eliminar = hacer_desempate(jugadores_a_desempatar, ((escalon.get_tema()).get_preguntasDesempate()))
        else:
            # Si solo hay un jugador con más errores, lo eliminamos directamente
            jugadores_a_eliminar = jugadores_a_desempatar
            
        # Eliminamos al jugador correspondiente
        for jugador in jugadores_a_eliminar:
            escalon.eliminar_jugador(jugador)

#--------------------------------------------------------
"""
for escalon in partida.get_escalones():
    print(f"\n--- Comenzando Escalón con tema {(escalon.get_tema()).get_nombreTema()} ---")
    
    for jugador in escalon.get_jugadores():
        jugador.set_ronda1(0)
        jugador.set_ronda2(0)
        
    # Ronda 1
    for jugador in escalon.get_jugadores():
        # Simulamos hacerle una pregunta y obtener si acertó (0: no contestó, 1: acertó, 2: falló)
        jugador.set_ronda1(hacer_pregunta(jugador, (escalon.get_tema()).get_preguntasRonda()))  # <------------------ACA NOS QUEDAMOS!!!
    
    # Ronda 2
    for jugador in escalon.get_jugadores():
        jugador.set_ronda2(hacer_pregunta(jugador, (escalon.get_tema()).get_preguntasRonda()))

    # Evaluamos los resultados de las dos rondas
    jugadores_a_desempatar = evaluar_jugadores(escalon.get_jugadores())
    
    # Si hay jugadores empatados (o todos acertaron), hacemos un desempate
    if len(jugadores_a_desempatar) > 1:
        print("Empate detectado. Comenzando ronda de desempate...")
        jugadores_a_eliminar = hacer_desempate(jugadores_a_desempatar, ((escalon.get_tema()).get_preguntasDesempate()))
    else:
        # Si solo hay un jugador con más errores, lo eliminamos directamente
        jugadores_a_eliminar = jugadores_a_desempatar
        
    # Eliminamos al jugador correspondiente
    for jugador in jugadores_a_eliminar:
        escalon.eliminar_jugador(jugador)
        """
for escalon in partida.get_escalones():
    escalon.set_jugadores(listaJugadores)
    print(f"\n--- Comenzando Escalón con tema {(escalon.get_tema()).get_nombreTema()} ---")
    jugadores_a_desempatar=[0]
    jugadores_a_eliminar=[0]
    for jugador in escalon.get_jugadores():
        jugador.set_ronda1(0)
        jugador.set_ronda2(0)
        
    # Ronda 1
    for jugador in escalon.get_jugadores():
        # Simulamos hacerle una pregunta y obtener si acertó (0: no contestó, 1: acertó, 2: falló)
        jugador.set_ronda1(hacer_pregunta(jugador, (escalon.get_tema()).get_preguntasRonda()))  # <------------------ACA NOS QUEDAMOS!!!
    
    # Ronda 2
    for jugador in escalon.get_jugadores():
        jugador.set_ronda2(hacer_pregunta(jugador, (escalon.get_tema()).get_preguntasRonda()))

    # Evaluamos los resultados de las dos rondas
    jugadores_a_desempatar = evaluar_jugadores(escalon.get_jugadores())
    
    # Si hay jugadores empatados (o todos acertaron), hacemos un desempate
    if len(jugadores_a_desempatar) > 1:
        print("Empate detectado. Comenzando ronda de desempate...")
        jugadores_a_eliminar = hacer_desempate(jugadores_a_desempatar, ((escalon.get_tema()).get_preguntasDesempate()))
    else:
        # Si solo hay un jugador con más errores, lo eliminamos directamente
        jugadores_a_eliminar = jugadores_a_desempatar
        
    # Eliminamos al jugador correspondiente
    for jugador in jugadores_a_eliminar:
        escalon.eliminar_jugador(jugador)
    
    lista_jugadores= escalon.get_jugadores()