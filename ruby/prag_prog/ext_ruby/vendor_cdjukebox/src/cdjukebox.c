#include <stdlib.h>
#include "cdjukebox.h"

CDJukebox *new_jukebox() {
  CDJukebox *jb = (CDJukebox *)malloc(sizeof(CDJukebox));
  jb->pending = 'P';
  return jb;
}

void assign_jukebox(CDJukebox *jb, int unit_id) {
  jb->unit_id = unit_id;
}

void free_jukebox(CDJukebox *jb) {
  free(jb);
}

void jukebox_seek(CDJukebox *jb, 
		  int disc, 
		  int track,
		  void (*done)(CDJukebox *jb, int percent)) {
  done(jb, 26);
  done(jb, 79);
  done(jb, 100);
}


double get_avg_seek_time(CDJukebox *jb) {
  return 1.2;
}
