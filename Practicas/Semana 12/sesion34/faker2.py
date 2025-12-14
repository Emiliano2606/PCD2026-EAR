from faker import Faker
import random
import csv

faker = Faker("es_MX")

canciones = [
    "Lluvia de Estrellas", "Sombras del Ayer", "Corazón Eléctrico", "Ritmo Urbano",
    "Noches de Neón", "Cicatrices", "Vértigo", "Latidos", "Desvelo", "Horizonte",
    "Fuego Interno", "Ecos", "Sin Mirar Atrás", "A Media Luz", "Punto Final",
    "Tiempo Muerto", "Renacer", "Mil Vidas", "Fragmentos", "Destino Cruzado",
    "Callejón", "Siluetas", "Alma Libre", "Oscuridad Total", "Instinto",
    "Despierta", "Laberinto", "Caos", "Voces", "Última Vez",
    "Entre Sombras", "Gravedad", "Mirada Fría", "Inercia", "Pálpito",
    "Marea Alta", "Desconexión", "Pulso", "Nostalgia", "Sin Control",
    "Ruido Blanco", "Lento Adiós", "Espiral", "A Contraluz", "Después de Ti",
    "Fantasmas", "Ciudad Rota", "Desorden", "Llama Azul", "Eterno",
    "Claroscuro", "Instante", "Recuerdos", "Niebla", "Contratiempo",
    "Reinicio", "Pecado", "Colisión", "Cenizas", "Punto Ciego",
    "Distancia", "Horizonte Rojo", "Latente", "Ausencia", "Tensión",
    "Sutil", "Último Latido", "Desfase", "Vértice", "Desvelo II",
    "Equilibrio", "Intermitente", "Al Límite", "Fragmentada", "Retroceso",
    "Antes del Silencio", "Despierto", "Sin Filtro", "Resonancia", "Pulso Final",
    "Sombras II", "Repetición", "Eco Final", "Caída Libre", "A Contrarreloj"
]

meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

anios = list(range(2015, 2026))


def generar_csv(n=100_000):
    with open("generar_canciones.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "nombre_cancion",
            "anio",
            "mes",
            "reproducciones",
            "likes"
        ])

        for _ in range(n):
            writer.writerow([
                random.choice(canciones),
                random.choice(anios),
                random.choice(meses),
                random.randint(1, 5000),
                random.randint(0, 5000)
            ])

    print("Archivo generar_canciones.csv generado con exito")


if __name__ == "__main__":
    generar_csv()
