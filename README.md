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

### LD&#95;PRELOAD

## ltrace

library trace, show library calls

```
# ltrace ./getip
```

## Name Service Switch (nss)

System used in POSIX systems to enumerate subsystems with various backends.  The system allows greater flexibility than utilizing a single file such as /etc/hosts, /etc/group, /etc/passwd

Configured from /etc/nsswitch.conf

## Boot Process

Sector 0 loads stage 1 loader, stage 1 loads stage 2 (just a memory thing, stage 1 is limited to 512 bytes, the size of a sector).  Stage 2 loads the kernel and sets the root filesystem.

The kernel is then exec'd, taking over as the privileged process.

## Kernel File Systems

The kernel exposes parts of itself with special filesystems, `/proc`, `/sys`

### /proc

Process management.  Information about running processes is shown in the /proc mount.  You can see the cmdline used to boot the system with /proc/cmdline.

| file    | contents |
|---------|----------|
| cmdline | complete command line and arguments |
| cwd | current working directory |
| environ | environment variables |
| fd  | directory containing file descriptors open by the process |
| fd/0 | standard input |
| fd/1 | standard input |
| fd/2 | standard output |
| fd/3 | standard error |
| io | IO Used by Process |
| limits | PAM Limits (hard/soft) |
| map_files | memory regions with associated files |
| maps | mapped memory regions | 


## ELF

*Executable and Linkable Format*

https://en.wikipedia.org/wiki/Executable_and_Linkable_Format

## Tools

|Tool  | Usage |
|------|------|
| getent | lookup NSS mapped information |
| lsof | list open files |
| ltrace | library call trace |
| nc | Network Swiss Army Knife, connect to ports, listen on ports |
| strace | system call trace |


## Working with Processes

### doublefork.py

This will fork a process, which forks again and then the grandparent and parent both die.  The grandchild becomes an orphan of the system and is scooped up by init.

### fd.py

This demonstrates file descriptors, the process starts, opens a file and then immediately unlinks it.  The process continues to use the file that is deleted.

### fork.py

This demonstrates a process forking.

### thread.py

This will create a process which spawns a number of threads

### zombie.py

This will create a process that forks and waits for the child to send a signal.  The child dies without sending the signal.  The parent is left hanging waiting.  The kernel then hangs onto the child waiting for it to send the signal...it never will, it's dead.  The child is the walking dead, a zombie.

## Everything is a file

Use the `file` command to examine files on the system.  Use mkfifo to make named fifo's.


