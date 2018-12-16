# Micro:bit dice
# Throw a dice. Chances are 100% that you will get a number between 1 and 6.

input.onGesture(Gesture.Shake, () => {
    let roll = Math.randomRange(0, 6);
    if (roll == 5) {
        basic.showLeds(`
. # . # .
. . . . .
. # . # .
. . . . .
. # . # .`);
    }
    else if (roll == 4) {
        basic.showLeds(`
. . . . .
. # . # .
. . # . .
. # . # .
. . . . .`);
    }
    else if (roll == 3) {
        basic.showLeds(`
. . . . .
. # . # .
. . . . .
. # . # .
. . . . .`);
    }
    else if (roll == 2) {
        basic.showLeds(`
# . . . .
. . . . .
. . # . .
. . . . .
. . . . #`);
    }
    else if (roll == 1) {
        basic.showLeds(`
. . . . .
. # . . .
. . . . .
. . . # .
. . . . .`);
    }
    else {
        basic.showLeds(`
. . . . .
. . . . .
. . # . .
. . . . .
. . . . .`);
    }
});
