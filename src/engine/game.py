class Game:
    def __init__(self, dimensions="2D"):
        self.players = []
        self.npcs = []
        self.items = []
        self.terrain = None
        self.current_player = None
        self.dimensions = dimensions

    def add_player(self, player):
        self.players.append(player)

    def add_npc(self, npc):
        self.npcs.append(npc)

    def add_item(self, item):
        self.items.append(item)

    def set_terrain(self, terrain):
        self.terrain = terrain

    def start(self):
        print("Iniciando o jogo...")
        self.current_player = self.players[0]
        print("O jogador atual é", self.current_player)
        # Coloque aqui a lógica para distribuir itens e personagens
        # Coloque aqui a lógica para gerar o terreno do jogo

    def end(self):
        # Coloque aqui a lógica para encerrar o jogo
        pass

    def next_turn(self):
        # Coloque aqui a lógica para avançar para o próximo turno
        pass
