#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int gethostname (char *name, size_t len) {
  char newname[] = "getip_hostname";
  int name_len = strlen(newname) + 1;
  memcpy(name,newname, name_len < len ? name_len : len);
  return 0;
}
