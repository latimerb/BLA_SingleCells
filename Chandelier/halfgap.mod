NEURON {
        POINT_PROCESS HalfGap
		POINTER vgap
        ELECTRODE_CURRENT i
        RANGE r, i
}

PARAMETER {
        r = 1e10 (megohm)
}

ASSIGNED {
        v (millivolt)
        vgap (millivolt)
        i (nanoamp)
}

BREAKPOINT {
        i = (vgap - v)/r
}