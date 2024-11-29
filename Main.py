def add_spell():
    print("\n🔮 Agregar nuevo hechizo 🔮")
    name = " de cuento de hadas"  # Nombre predeterminado
    level = "Nivel 1"  # Nivel predeterminado
    description = "Descripción de prueba"  # Descripción predeterminada
    spell = {"name": name, "level": level, "description": description}
    spell_library.append(spell)
    print(f"✨ Hechizo '{name}' agregado exitosamente!")
