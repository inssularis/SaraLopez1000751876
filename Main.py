def show_menu():
    print("\n📜 Biblioteca de Hechizos 📜")
    print("1. Agregar un nuevo hechizo")
    print("2. Ver todos los hechizos")
    print("3. Buscar un hechizo por nombre")
    print("4. Actualizar un hechizo existente")
    print("5. Eliminar un hechizo por nombre")
    print("6. Salir")

# Base de datos ficticia de hechizos
spell_library = []

def add_spell():
    print("\n🔮 Agregar nuevo hechizo 🔮")
    name = input("Nombre del hechizo: ")
    level = input("Nivel del hechizo: ")
    description = input("Descripción del hechizo: ")
    spell = {"name": name, "level": level, "description": description}
    spell_library.append(spell)
    print(f"✨ Hechizo '{name}' agregado exitosamente!")

def view_spells():
    print("\n📚 Lista de Hechizos 📚")
    if not spell_library:
        print("Aún no hay hechizos en la biblioteca.")
    else:
        for spell in spell_library:
            print(f"- {spell['name']} (Nivel {spell['level']}): {spell['description']}")

def search_spell():
    print("\n🔍 Buscar Hechizo 🔍")
    name = input("Ingrese el nombre del hechizo que desea buscar: ")
    spell = next((s for s in spell_library if s['name'].lower() == name.lower()), None)
    if spell:
        print(f"✨ Hechizo encontrado: {spell['name']} (Nivel {spell['level']}): {spell['description']}")
    else:
        print("⚠️ Hechizo no encontrado.")

def update_spell():
    print("\n✏️ Actualizar Hechizo ✏️")
    name = input("Ingrese el nombre del hechizo que desea actualizar: ")
    spell = next((s for s in spell_library if s['name'].lower() == name.lower()), None)
    if spell:
        print(f"Editando '{spell['name']}'")
        spell['level'] = input("Nuevo nivel (actual: {0}): ".format(spell['level'])) or spell['level']
        spell['description'] = input("Nueva descripción (actual: {0}): ".format(spell['description'])) or spell['description']
        print(f"✨ Hechizo '{spell['name']}' actualizado exitosamente!")
    else:
        print("⚠️ Hechizo no encontrado.")

def delete_spell():
    print("\n❌ Eliminar Hechizo ❌")
    name = input("Ingrese el nombre del hechizo que desea eliminar: ")
    global spell_library
    spell_library = [s for s in spell_library if s['name'].lower() != name.lower()]
    print(f"✨ Hechizo '{name}' eliminado (si existía en la biblioteca).")

def main():
    while True:
        show_menu()
        choice = input("\nSeleccione una opción (1-6): ")
        if choice == "1":
            add_spell()
        elif choice == "2":
            view_spells()
        elif choice == "3":
            search_spell()
        elif choice == "4":
            update_spell()
        elif choice == "5":
            delete_spell()
        elif choice == "6":
            print("🪄 ¡Hasta pronto, mago!")
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
