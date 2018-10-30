# Linux Systems Troubleshooting

https://goo.gl/qc8rHw

## System Libraries

System Libraries contain the wrappers for system calls, the code for system calls is contained within the kernel.  The sytem library only contains the "shim" code, code to load registers with the correct values and then request the kernel perform the operation.

### List functions in a library

To list the functions compiled into a library, use `nm`.  Functions are called symbols in a compiled library.

```
# nm /lib64/libc.so.6 | less
```

## Linker

The linker is used to find dependencies.  Basically every binary gets a copy of the linker embedded, so they can use it to find everything else they need.

### List dependencies of a compiled program

```
# ldd /path/to/executable
``` 

There are environment variables which can be used to modify the behaviour of the linker.

### LD&#95;DEBUG

