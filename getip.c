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

  gethostname(hostname, sizeof(hostname));

  hostStruct = gethostbyname(hostname);

  if (hostStruct) {
    IPbuffer = inet_ntoa(*((struct in_addr*) hostStruct->h_addr_list[0]));
    printf("Using IP: %s\n", IPbuffer);
    return 0;
  } else {
    printf("Couldn't find IP for %s\n", hostname);
    return 1;
  }

}
