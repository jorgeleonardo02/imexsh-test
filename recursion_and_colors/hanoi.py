def otro_metodo():
    pass

""" def hanoi():
    print("hanoi implementation") """

def hanoi():
    def hanoi_with_colors(n, disks, source='A', target='C', auxiliary='B', moves=None):
        if moves is None:
            moves = []

        if n == 0:
            return moves

        if n == 1:
            moves.append((disks[0][0], source, target))
            return moves

        # Restricción: discos del mismo color seguidos no se permiten
        if n >= 2 and disks[0][1] == disks[1][1]:
            return -1

        # Paso recursivo: mueve n-1 discos arriba al auxiliar
        left = hanoi_with_colors(n - 1, disks[1:], source, auxiliary, target, moves)
        if left == -1:
            return -1

        # Mueve el disco más grande al destino
        moves.append((disks[0][0], source, target))

        # Mueve n-1 discos desde auxiliar al destino
        right = hanoi_with_colors(n - 1, disks[1:], auxiliary, target, source, moves)
        if right == -1:
            return -1

        return moves

    # Ejemplo válido
    disks = [(3, "red"), (2, "blue"), (1, "red")]
    result = hanoi_with_colors(len(disks), disks)
    print("Resultado válido:", result)

    # Ejemplo inválido
    disks_invalid = [(3, "red"), (2, "red"), (1, "blue")]
    result_invalid = hanoi_with_colors(len(disks_invalid), disks_invalid)
    print("Resultado inválido:", result_invalid)


if __name__ == "__main__":
    hanoi()



