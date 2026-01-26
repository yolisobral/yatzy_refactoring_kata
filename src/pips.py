from enum import Enum, unique


@unique
class Pips(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]

    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())

    @classmethod
    def minus(cls, pip):
        return set(cls.values()) - {pip.value}
    
    
if __name__ == "__main__":
    print("\n" + "="*70)
    print("DEMOSTRACIÓN DE LA CLASE ENUM PIPS - MÉTODOS Y PROPIEDADES")
    print("="*70)
    
    print("\n📋 1. CONVERTIR ENUM A LISTA (iterable)")
    print("-" * 70)
    print("   Descripción: Convierte el enum en una lista con todos sus miembros")
    print(f"   Resultado: {list(Pips)}\n")
    
    print("🔍 2. ACCESO A MIEMBROS DEL ENUM - 3 FORMAS DIFERENTES")
    print("-" * 70)
    print("   a) Pips(1) - Accede por VALOR (busca el miembro con valor 1)")
    print(f"      Resultado: {Pips(1)}")
    print("   b) Pips['ONE'] - Accede por NOMBRE (busca el miembro llamado 'ONE')")
    print(f"      Resultado: {Pips['ONE']}")
    print("   c) Pips.ONE - Acceso directo al miembro por atributo")
    print(f"      Resultado: {Pips.ONE}\n")
    
    print("📝 3. PROPIEDADES .name Y .value DE UN MIEMBRO")
    print("-" * 70)
    print("   Descripción: Obtienen el nombre y valor de un miembro del enum")
    print(f"   Pips.ONE.name  → Devuelve el nombre: '{Pips.ONE.name}'")
    print(f"   Pips.ONE.value → Devuelve el valor: {Pips.ONE.value}\n")
    
    print("🔄 4. ITERAR SOBRE __members__ (diccionario interno)")
    print("-" * 70)
    print("   Descripción: __members__ es un diccionario con todos los miembros")
    print("   Formato: {nombre: miembro_enum}")
    for number in Pips.__members__.values():
        print(f"      {number.name}: {number._value_}")
    print()
    
    print("⚙️  5. MÉTODOS DE CLASE PERSONALIZADOS")
    print("-" * 70)
    
    print("   a) values()")
    print("      Descripción: Devuelve una lista con todos los valores (1 a 6)")
    print(f"      Resultado: {Pips.values()}")
    print()
    
    print("   b) reversedValues()")
    print("      Descripción: Devuelve un iterador con valores en orden inverso (6 a 1)")
    print(f"      Resultado: {list(Pips.reversedValues())}")
    print()
    
    print("   c) minus(pip)")
    print("      Descripción: Devuelve un conjunto de valores excluyendo el pip pasado")
    print(f"      Resultado minus(Pips.FIVE): {Pips.minus(Pips.FIVE)}")
    print("      (Retorna todos los valores excepto el 5)")
    print()
    
    print("="*70 + "\n") 