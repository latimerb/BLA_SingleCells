#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _kdrinter_reg();
extern void _leakinter_reg();
extern void _nainter_reg();
extern void _xtra_imemrec_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," kdrinter.mod");
fprintf(stderr," leakinter.mod");
fprintf(stderr," nainter.mod");
fprintf(stderr," xtra_imemrec.mod");
fprintf(stderr, "\n");
    }
_kdrinter_reg();
_leakinter_reg();
_nainter_reg();
_xtra_imemrec_reg();
}
