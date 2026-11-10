# NEXORA STUDIOS — HYPERMC RPG Resource Pack

Resource pack objetivo: Minecraft Java 1.12.2 / Modern Client (compatibilidad por verificar en cada build).

## Estructura
- `assets/minecraft/models/item/`: overrides vanilla para armas, fragmentos y armaduras.
- `assets/minecraft/textures/items/`: texturas fallback para clientes que no apliquen overrides.
- `assets/nexora/models/item/`: modelos de los objetos RPG.
- `assets/nexora/textures/items/`: armas y fragmentos NEXORA.
- `assets/nexora/textures/armor/`: iconos de armaduras.
- `assets/minecraft/textures/gui/`: panorama, logo, botones e interfaces.

## Generación reproducible
Las imágenes se generan desde `scripts/generate_textures.py` y `scripts/generate_ui.py`.
El flujo crea primero todas las carpetas necesarias, genera PNG RGBA, valida dimensiones y empaqueta el ZIP.

## Importación
Descarga el archivo `NEXORA-HYPERMC-RPG-1.12.2.zip) del artefacto de GitHub Actions. Importa ese ZIP directamente en el cliente. No importes el ZIP exterior del artefacto si GitHub descargó un contenedor ZIP.

## Limitaciones conocidas
Los modelos por predicados de daño dependen de que el cliente implemente el sistema de modelos de Minecraft 1.12.2. Las texturas fallback solo prueban que el cliente lee rutas vanilla; hacen que todos los objetos vanilla de ese tipo compartan esa textura. La apariencia equipada de armadura requiere texturas de capa compatibles y debe probarse por separado.
