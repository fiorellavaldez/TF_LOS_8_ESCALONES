import pygame
import os

class Sonido:
    def __init__(self, archivo=None):
        """Inicializa el sistema de sonido y configura la música."""
        # Inicializamos pygame.mixer si no ha sido inicializado
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        self.music_on = True  # Inicialmente la música está encendida
        self.volume = 1.0  # Volumen inicial al máximo
        self.file_path = None  # Ruta del archivo actual

        if archivo:
            self.cambiar_musica(archivo)  # Establecer música si se proporciona un archivo

    def cambiar_musica(self, nueva_ruta):
        """Permite cambiar la música actual a una nueva."""
        if os.path.exists(nueva_ruta):
            self.file_path = nueva_ruta
            self.__cargar_musica()
        else:
            print(f"Error: El archivo de música '{nueva_ruta}' no se encuentra.")

    def __cargar_musica(self):
        """Carga y reproduce la música actual desde el archivo configurado."""
        try:
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.set_volume(self.volume)  # Ajustar volumen al actual
            if self.music_on:
                pygame.mixer.music.play(-1)  # Reproducir música en bucle
        except pygame.error as e:
            print(f"Error al cargar la música: {str(e)}")

    def toggle_music(self):
        """Activa o desactiva la música."""
        if self.music_on:
            pygame.mixer.music.stop()
        else:
            try:
                pygame.mixer.music.play(-1)  # Reproducir en bucle
            except pygame.error as e:
                print(f"Error al reproducir la música: {str(e)}")
        self.music_on = not self.music_on

    def set_volume(self, volume):
        """Establece el volumen de la música."""
        self.volume = volume
        pygame.mixer.music.set_volume(volume)

    def stop_music(self):
        """Detiene la música actual."""
        pygame.mixer.music.stop()

    def cambiar_musica(self, nueva_ruta):
        """Permite cambiar la música actual a una nueva."""
        if os.path.exists(nueva_ruta):
            self.file_path = nueva_ruta
            self.__cargar_musica()
        else:
            print(f"Error: El archivo de música '{nueva_ruta}' no se encuentra.")


# import pygame
# import os

# class Sonido:
#     def __init__(self, archivo=None):
#         """Inicializa el sistema de sonido y configura la música."""
#         # Inicializamos pygame.mixer si no ha sido inicializado
#         if not pygame.mixer.get_init():
#             pygame.mixer.init()

#         self.music_on = True  # Inicialmente la música está encendida
#         self.volume = 1.0  # Volumen inicial al máximo

#         if archivo:
#             self.cambiar_musica(archivo)  # Establecer música si se proporciona un archivo

    
#     def cambiar_musica(self, nueva_ruta):
#         """Permite cambiar la música actual a una nueva."""
#         self.music_file = nueva_ruta  # Establecer nueva ruta de música
#         self.__cargar_musica(self.music_file)  # Cargar y reproducir la nueva música

#     def __cargar_musica(self, archivo):
#         """Carga y reproduce una nueva canción."""
#         if os.path.exists(archivo):
#             try:
#                 pygame.mixer.music.load(archivo)
#                 pygame.mixer.music.set_volume(self.volume)  # Ajustar volumen al actual
#                 if self.music_on:
#                     pygame.mixer.music.play(-1)  # Reproducir música en bucle
#             except pygame.error as e:
#                 print(f"Error al cargar la música: {str(e)}")
#         else:
#             print(f"Error: El archivo de música {archivo} no se encuentra en la ruta especificada.")

#     def toggle_music(self):
#         """Activa o desactiva la música."""
#         if self.music_on:
#             pygame.mixer.music.stop()
#         else:
#             try:
#                 pygame.mixer.music.play(-1)  # Reproducir en bucle
#             except pygame.error as e:
#                 print(f"Error al reproducir la música: {str(e)}")
#         self.music_on = not self.music_on
