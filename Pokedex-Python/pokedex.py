from collections import Counter
import requests

# Función para traducir tipos al español usando la PokéAPI
def traducir_tipo(tipo_name):
    url = f"https://pokeapi.co/api/v2/type/{tipo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        tipo_data = response.json()
        for name in tipo_data["names"]:
            if name["language"]["name"] == "es":
                return name["name"]
    return tipo_name.capitalize()

# Función para obtener datos completos de tipos
def obtener_datos_tipos(pokemon_data):
    tipos_completos = []
    for tipo in pokemon_data["types"]:
        tipo_url = tipo["type"]["url"]
        response = requests.get(tipo_url)
        if response.status_code == 200:
            tipo_data = response.json()
            tipos_completos.append(tipo_data)
        else:
            print(f"Error al obtener datos del tipo: {tipo_url}")
    return tipos_completos

# Funciones de evolución
def explicar_condiciones(evo_detalle):
    condiciones = []
    for clave, valor in evo_detalle.items():
        if valor is None or valor == "" or valor is False:
            continue
        if isinstance(valor, dict) and "name" in valor:
            valor = valor["name"]
        condiciones.append(f"{clave.replace('_', ' ')}: {valor}")
    return condiciones

def buscar_evolucion(cadena, nombre_pokemon):
    if cadena["species"]["name"] == nombre_pokemon:
        return cadena["evolves_to"]
    for evo in cadena["evolves_to"]:
        resultado = buscar_evolucion(evo, nombre_pokemon)
        if resultado is not None:
            return resultado
    return None

while True:
    pokemon = input("¿Qué Pokémon quieres buscar? ").strip()
    if not pokemon:
        print("\n No has introducido ningún nombre. Intenta nuevamente.")
        continuar = input("\n¿Quieres buscar otro Pokémon? (s/n): ").lower()
        if continuar != "s":
            print("¡Hasta luego!")
            break
        else:
            continue

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"\n El Pokémon '{pokemon}' no ha sido encontrado en la Pokédex. Intenta con otro nombre.")
        continuar = input("\n¿Quieres buscar otro Pokémon? (s/n): ").lower()
        if continuar != "s":
            print("¡Hasta luego!")
            break
        else:
            continue

    data = response.json()

    # Obtener especie
    species_url = data["species"]["url"]
    species_response = requests.get(species_url)
    species_data = species_response.json()

    # Nombre en español
    nombre_es = None
    for name in species_data["names"]:
        if name["language"]["name"] == "es":
            nombre_es = name["name"]
            break

    print("\nInformación del Pokémon")
    print("Nombre:", nombre_es or data["name"])
    print("ID:", data["id"])

    # Evoluciones
    print("Cómo evoluciona:")
    ev_url = species_data["evolution_chain"]["url"]
    ev_response = requests.get(ev_url)
    ev_data = ev_response.json()
    cadena = ev_data["chain"]
    nombre_actual = data["name"]
    evoluciones = buscar_evolucion(cadena, nombre_actual)

    if evoluciones:
        for evo in evoluciones:
            nombre_evo = evo["species"]["name"]
            print(f" - Evoluciona a {nombre_evo} con estas condiciones:")
            for detalle in evo["evolution_details"]:
                condiciones = explicar_condiciones(detalle)
                for c in condiciones:
                    print(f"    * {c}")
    else:
        print(" - Este Pokémon no tiene evoluciones posteriores.")

    # Tipos
    print("Tipo(s):")
    tipos = obtener_datos_tipos(data)
    for tipo in tipos:
        for name in tipo["names"]:
            if name["language"]["name"] == "es":
                print(" -", name["name"])
                break

    # Debilidades
    ventajas = input("¿Quieres saber a qué tipos eres débil? (s/n): ").lower()
    if ventajas == "s":
        debilidades = []
        for tipo in tipos:
            relaciones = tipo["damage_relations"]
            for tipo_doble in relaciones["double_damage_from"]:
                debilidades.append(tipo_doble["name"])
        contador = Counter(debilidades)
        x2 = [tipo for tipo, cantidad in contador.items() if cantidad == 1]
        x4 = [tipo for tipo, cantidad in contador.items() if cantidad == 2]

        if x4:
            print("\nEste Pokémon recibe **x4** de daño de:")
            for tipo in x4:
                print(" -", traducir_tipo(tipo))
        if x2:
            print("\nEste Pokémon recibe **x2** de daño de:")
            for tipo in x2:
                print(" -", traducir_tipo(tipo))
        if not x2 and not x4:
            print("Este Pokémon no tiene debilidades x2 ni x4.")

    # Resistencias
    ventajas = input("¿Quieres saber a qué tipos eres resistente? (s/n): ").lower()
    if ventajas == "s":
        fortalezas = []
        for tipo in tipos:
            relaciones = tipo["damage_relations"]
            for tipo_doble in relaciones["half_damage_from"]:
                fortalezas.append(tipo_doble["name"])
        contador = Counter(fortalezas)
        x05 = [tipo for tipo, cantidad in contador.items() if cantidad == 1]
        x025 = [tipo for tipo, cantidad in contador.items() if cantidad == 2]

        if x025:
            print("\nEste Pokémon recibe **x0,25** de daño de:")
            for tipo in x025:
                print(" -", traducir_tipo(tipo))
        if x05:
            print("\nEste Pokémon recibe **x0,50** de daño de:")
            for tipo in x05:
                print(" -", traducir_tipo(tipo))
        if not x025 and not x05:
            print("Este Pokémon no tiene resistencias a ningún tipo.")

    # Movimientos por nivel
    movs = input("¿Quieres saber qué movimientos aprende por nivel? (s/n): ").lower()
    if movs == "s":
        print("\nMovimientos por nivel (Español):")
        print(f"{'Nivel':<10} {'Movimiento':<30}")
        print("-" * 40)
        movimientos_ordenados = []

        for movimiento in data["moves"]:
            url_mov = movimiento["move"]["url"]
            nombre_ing = movimiento["move"]["name"]
            mov_response = requests.get(url_mov)
            if mov_response.status_code != 200:
                continue
            mov_data = mov_response.json()
            nombre_es = next((n["name"] for n in mov_data["names"] if n["language"]["name"] == "es"), nombre_ing)

            for detalle in movimiento["version_group_details"]:
                if (detalle["move_learn_method"]["name"] == "level-up" and
                    detalle["version_group"]["name"] == "sword-shield" and
                    detalle["level_learned_at"] > 0):
                    nivel = detalle["level_learned_at"]
                    movimientos_ordenados.append((nivel, nombre_es))
                    break

        movimientos_ordenados.sort(key=lambda x: x[0])
        for nivel, nombre in movimientos_ordenados:
            print(f"{nivel:<10} {nombre:<30}")

    # Habilidades
    print("\nHabilidades:")
    for habilidad in data["abilities"]:
        habilidad_url = habilidad["ability"]["url"]
        habilidad_response = requests.get(habilidad_url)
        habilidad_data = habilidad_response.json()
        for name in habilidad_data["names"]:
            if name["language"]["name"] == "es":
                print(" -", name["name"])
                break

    # Descripción de habilidades
    info = input("¿Quieres saber más sobre las habilidades? (s/n): ").lower()
    if info == "s":
        for habilidad in data["abilities"]:
            habilidad_url = habilidad["ability"]["url"]
            habilidad_response = requests.get(habilidad_url)
            habilidad_data = habilidad_response.json()
            for entry in habilidad_data["flavor_text_entries"]:
                if entry["language"]["name"] == "es":
                    print(" -", entry["flavor_text"].replace("\n", " "))
                    break

    # Estadísticas
    print("\nEstadísticas base:")
    for stat in data["stats"]:
        nstat = stat["stat"]["name"]
        valor = stat["base_stat"]
        traduccion = {
            "hp": "PS",
            "attack": "Ataque",
            "defense": "Defensa",
            "special-attack": "Ataque Especial",
            "special-defense": "Defensa Especial",
            "speed": "Velocidad"
        }
        print(f" - {traduccion.get(nstat, nstat)}: {valor}")

    continuar = input("\n¿Quieres buscar otro Pokémon? (s/n): ").lower()
    if continuar != "s":
        print("¡Hasta luego!")
        break