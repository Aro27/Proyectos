# Pokédex en Python usando PokéAPI

Este proyecto es una Pokédex en línea de comandos que utiliza la [PokéAPI](https://pokeapi.co/) para obtener información completa de cualquier Pokémon, incluyendo:

- Nombre, ID y nombres en español
- Evoluciones y condiciones para evolucionar
- Tipos con traducción al español
- Debilidades y resistencias
- Movimientos aprendidos por nivel (edición Sword & Shield)
- Habilidades y descripción
- Estadísticas base

---

## Requisitos

- Python 3.7+
- Módulo `requests` (instalable con pip)

---

## Instalación

Clona el repositorio y entra en la carpeta:

```bash
git clone https://github.com/tuusuario/pokedex-python.git
cd pokedex-python
```

## Uso

Hay dos formas de utilizarlo, si tienes Python instalado, abre una consola o terminal y ejecuta:

```bash
python pokedex.py
```

Si prefieres usar la Pokédex sin necesidad de instalar Python, puedes convertir el script en un archivo ejecutable usando PyInstaller

```bash
pyinstaller --onefile pokedex.py
```

Esto generará un archivo ejecutable dentro de la carpeta dist que podrás ejecutar directamente.

Nota: Si no tienes PyInstaller instalado, instálalo con:

```bash
pip install pyinstaller
```

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
