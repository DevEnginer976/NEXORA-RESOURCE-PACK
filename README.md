# NEXORA STUDIOS — HYPERMC RPG RESOURCE PACK

Paquete de recursos independiente para **Minecraft Java 1.12.2**, con Modern Client como cliente objetivo.

## Identidad visual
- Estética RPG de fantasía oscura, oro antiguo y acentos mágicos.
- Ocho lanzas con siluetas y paletas diferenciadas: Divina, Glacial, Infernal, Natural, Trueno, Vacío, Marina y Ancestral.
- Arco Astral.
- Próxima fase: cuatro conjuntos de armadura (Divina, Infernal, Glacial y Vacío), materiales, fragmentos, interfaz y menú principal NEXORA STUDIOS.

## Compatibilidad
- `pack_format: 3` para Minecraft 1.12.2.
- No utiliza CustomModelData (no existe en 1.12.2).
- Los modelos de armas se asignarán mediante predicados de daño/durabilidad en modelos JSON y requieren que el plugin NEXORA asigne los valores correspondientes.
- La compatibilidad exacta de modelos, panorama y pantallas de menú debe probarse dentro de la compilación concreta de Modern Client.
- Las texturas de icono no garantizan por sí solas una apariencia de armadura distinta al equiparla. Esa parte necesita una estrategia de armadura compatible con el renderizador del cliente.

## Estructura
- `assets/nexora/textures/items/`: texturas de armas.
- `assets/nexora/models/item/`: modelos de objetos.
- `assets/minecraft/models/item/`: overrides del objeto base.
- `docs/ITEM-MAPPING.md`: asignación que debe coincidir con el plugin.

## Instalación de prueba
1. Descarga el ZIP del paquete desde GitHub.
2. En Modern Client abre Resource Packs.
3. Importa o selecciona el ZIP, según las opciones disponibles en esa compilación.
4. Actívalo y entra a un mundo de pruebas.

**Estado:** base inicial de desarrollo. No es todavía la versión final completa.
