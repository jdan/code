SinOsc s => dac;

[4, 3, 0] @=> int steps[];

for (0 => int c; c < 100; c++) {
    Std.rand2(49, 65) => int k;
    for (0 => int i; i < 3; i++) {
        freq_from_key(k) => s.freq;
        k + steps[i] => k;
        20::ms => now;
    }
}

function float freq_from_key(int k) {
    return 440 * (Math.pow(2.0, (k - 49) / 12.0));
}