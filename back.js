class Model {
    calculatePushForce(density, volume, gravity) {
        return density * volume * gravity;
    }

    calculateVolume(density, push, gravity) {
        return push / (density * gravity);
    }

    calculateDensityForce(push, volume, gravity) {
        return push / (volume * gravity);
    }

    calculateGravityForce(density, volume, push) {
        return push / (volume * density);
    }

    calculatePushWeightForce(weight, apparentWeight) {
        return weight - apparentWeight;
    }

    calculateWeight(push, apparentWeight) {
        return push + apparentWeight;
    }

    calculateApparentWeight(push, weight) {
        return weight - push;
    }
}
