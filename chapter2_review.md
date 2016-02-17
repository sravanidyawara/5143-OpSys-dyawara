# Chapter 2 Review Questions
Name: Sravani Dyawara

Course: 5143 Operating Systems

Date: 18 Feb 2016
## What are the three objectives of an operating system?
a)Convenience 

b)Efficiency

c)Maintainability
## What is the kernel of an OS?
The kernel is the central module of an operating system. It is the part of the operating system that loads first, and it remains in main memory. Because it stays in memory, it is important for the kernel to be as small as possible while still providing all the essential services required by other parts of the operating system and applications. The kernel code is usually loaded into a protected area of memory to prevent it from being overwritten by programs or other parts of the operating system.
## What is multiprogramming?
The multiprogramming is interleaved execution of multiple jobs by the same computer.In multiprogramming system, when one program is waiting for I/O transfer; there is another program ready to utilize the CPU. So it is possible for several jobs to share the time of the CPU. But it is important to note that multiprogramming is not defined to be the execution of jobs at the same instance of time. Rather it does mean that there are a number of jobs available to the CPU (placed in main memory) and a portion of one is executed then a segment of another and so on.
## What is a process?
A process is an instance of a computer program that is being executed. It contains the program code and its current activity. Depending on the operating system, a process may be made up of multiple threads of execution that execute instructions concurrently.A computer program is a passive collection of instructions; a process is the actual execution of those instructions. Several processes may be associated with the same program; for example, opening up several instances of the same program often means more than one process is being executed.
## How is the execution context of a process used by the OS?
The execution context, or process state, is the internal data by which the operating system is able to supervise and control the process. This internal information is separated from the process, because the operating system has information not permitted to the process. The context includes all of the information that the operating system needs to manage the process and that the processor needs to execute the process properly. The context includes the contents of the various processor registers, such as the program counter and data registers. It also includes informatoin of use to the operating system,such as priority of the process and whether the process is waiting for the completion of particular I/O event.
## List and briefly explain five storage management responsibilities of a typical OS.
Process isolation: The OS must prevent independent processes from interfering with eachother’s memory, both data and instructions.

Automatic allocation and management: Programs should be dynamically allocated across the memory hierarchy as required. Allocation should be transparent to the programmer. Thus, the programmer is relieved of concerns relating to memory limitations, and the OS can achieve efficiency by assigning memory to jobs only as needed. 

Support of modular programming: Programmers should be able to define program modules, and to create, destroy, and alter the size of modules dynamically. 

Protection and access control: Sharing of memory, at any level of the memory hierarchy, creates the potential for one program to address the memory space of another. This is desirable when sharing is needed by particular applications. At other times, it threatens the integrity of programs and even the OS itself. The OS must allow portions of memory to be accessible in various ways by various users. 

Long-term storage: Many applications programs require means for storing information for extended periods of time, after the computer has been powered down.
## Explain the distinction between a real address and a virtual address
Virtual vs Real Addresses
Physical addresses refer to hardware addresses of physical memory.
Virtual addresses refer to the virtual store viewed by the process.
• virtual addresses might be the same as physical addresses
• might be different, in which case virtual addresses must be mapped into physical
addresses.
• virtual space is limited by size of virtual addresses (not physical addresses)
• virtual space and physical memory space are independent.
## Describe the round-robin scheduling technique.
Round robin is a process used for network communication and operating system load balancing. A system that works in a round robin fashion distributes load based on the round robin algorithm.The round robin algorithm uses its scheduling techniques to assign processing time slices and transfer queued data packets. Network devices such as routers and switches implement special round robin algorithm buffer queues, which exist in device memory and store incoming and overloaded data for future processing.The term is also used in load balancing for servers. For example, a front-end load balancer on a webfarm could distribute Internet traffic among a group of webservers based on a round-robin process.
## Explain the difference between a monolithic kernel and a microkernel.
Monolithic kernel: The older approach is the monolithic kernel, of which Unix, MS-DOS and the early Mac OS are typical represents of. It runs every basic system service like process and memory management, interrupt handling and I/O communication, file system, etc. in kernel space. It is constructed in a layered fashion, built up from the fundamental process management up to the interfaces to the rest of the operating system (libraries and on top of them the applications). 
Microkernel: The concept  was to reduce the kernel to basic process communication and I/O control, and let the other system services reside in user space in form of normal processes (as so called servers). There is a server for managing memory issues, one server does process management, another one manages drivers, and so on. Because the servers do not run in kernel space anymore, so called ”con-text switches” are needed, to allow user processes to enter privileged mode (and to exit again). That way, the μ-kernel is not a block of system services anymore, but represents just several basic abstractions and primitives to control the communication between the processes and between a process and the underlying hardware. Because communication is not done in a direct way anymore, a message system is introduced, which allows independent communication and favors extensibility.
## What is multithreading?
Multithreading is the ability of a program or an operating system process to manage its use by more than one user at a time and to even manage multiple requests by the same user without having to have multiple copies of the programming running in the computer. Each user request for a program or system service (and here a user can also be another program) is kept track of as a thread with a separate identity. As programs work on behalf of the initial request for that thread and are interrupted by other requests, the status of work on behalf of that thread is kept track of until the work is completed.
## List the key design issues for an SMP operating system
a)concurrent process

b)scheduling

c)synchronization

d)memory management

e)reliability
