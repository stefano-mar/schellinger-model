class SchellingAgent(Agent):
    # Initialization
    def __init__(self, pos, model, agent_type):
        super().__init__(pos, model)
        self.pos = pos
        self.type = agent_type

    # Step function
    def step(self):
        similar = 0
        # Calculate the number of similar neighbours
        for neighbor in self.model.grid.neighbor_iter(self.pos):
            if neighbor.type == self.type:
                similar += 1

        # Move to a random empty location if unhappy
        if similar < self.model.homophily:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1
