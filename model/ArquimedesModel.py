class Arquimedesodel:
    def calculate_push_force(self, density, volume, gravity):
        return density * volume * gravity

    def calculate_volume(self, density, push, gravity):
        return push / (density * gravity)

    def calculate_density_force(self, push, volume, gravity):
        return push / (volume * gravity)

    def calculate_gravity_force(self, density, volume, push):
        return push / (volume * density)

    def calculate_push_weight_force(self, weight, apparent_weight):
        return weight - apparent_weight

    def calculate_weight(self, push, apparent_weight):
        return push + apparent_weight

    def calculate_apparent_weight(self, push, weight):
        return weight - push
