#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>

int main()
{
  char hostname[256];
  char *IPbuffer;
  struct hostent *hostStruct;
  int h;

  h = gethostname(hostname, sizeof(hostname));

  hostStruct = gethostbyname(hostname);

  IPbuffer = inet_ntoa(*((struct in_addr*) hostStruct->h_addr_list[0]));

  printf("Using IP: %s\n", IPbuffer);

  return 0;
}
