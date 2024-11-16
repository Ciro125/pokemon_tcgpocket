# Função para validar as posições
def validar_posicoes(posicoes):
    if len(set(posicoes.values())) != len(posicoes.values()):
        return False, "As posições não podem se repetir."
    if not all(1 <= pos <= 5 for pos in posicoes.values()):
        return False, "Todas as posições devem ser números entre 1 e 5."
    return True, ""