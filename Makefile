CFLAGS= -Wall -g -O -fPIC
LDFLAGS= -fPIC -Wl,-wrap,gethostname -shared

all: getip gethostname_wrap.so
clean:
	rm -f *.o *.so

getip:
	$(CC) -o getip getip.c

#gethostname_wrap.o:
#	$(CC) -Wl,-wrap,gethostname gethostname_wrap.c $< >$@

gethostname_wrap.so:
	$(CC) ${LDFLAGS} -o gethostname_wrap.so gethostname_wrap.c
# gcc gethostname_wrap.c -fPIC -shared -Wl,-wrap,gethostname -o gethostname_wrap.so
