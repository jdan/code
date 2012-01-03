SinOsc s => Envelope e => dac;

440 => s.freq;
0.2 => e.value;

while ( true ) {
    if (Std.rand2f(0, 1) > 0.8) {
        for (440 => int i; i < 880; i + 5 => i) {
            i => s.freq;
            1::ms => now;
        }
    }
    
    440 => s.freq;
    50::ms => now;
}

fun float ntof (int k) {
    return 440 * Math.pow(2, (k - 49) / 12.0);
}