# Chapter 3 Review Questions
Name: Sravani Dyawara
Course: 5143 Operating Systems
Date: 01 Mar 2016

## What does it mean to preempt a process?

When a higher priority process becomes dispatchable, the kernel interrupts its computation and forces the context switch, preempting the currently running process. A process can be preempted at any time if the kernel finds that a higher-priority process is now dispatchable.

## What is swapping and what is its purpose?

Swapping enables a computer to execute programs and manipulate data files larger than main memory. The operating system copies as much as data possible into main memory, and leaves the rest on the disk. When the operating system needs data from the disk, it exchanges a portion of data in main memory with a portion of data on the disk.
The purpose of swapping is to access data being stored in hard disk and to bring it into the RAM so that it can be used by the application program.

## List three general categories of information in a process control block.

a)Process identification.

b)Processor state information.

c)Process control information.

## Why are two modes (user and kernel) needed?

In kernel mode, the CPU has instructions to manage memory and how it can be accessed, and the ability to access peripheral devices like disks and network cards. The CPU can also switch itself from one running program to another.

In user mode, access to memory is limited to only some memory locations, and access to peripheral devices is denied. The ability to keep the CPU is removed, and the CPU can be taken away from a program at any time.

## What is the difference between an interrupt and a trap?

 A trap will occur at exactly the same point of the program execution, each time a program runs.

 An interrupt is dependent on the relative timing between the interrupting device and the CPU.
## Give three examples of an interrupt.
 
 Example-1:, pressing a key on the keyboard or moving the mouse triggers hardware interrupts that cause the processor to read the keystroke or mouse position.
 
  Example-2:, if the processor's arithmetic logic unit is commanded to divide a number by zero, this impossible demand will cause a divide-by-zero exception, perhaps causing the computer to abandon the calculation or display an error message. 
  
  Example-3:, computers often use software interrupt instructions to communicate with the disk controller to request data be read or written to the disk.
  
## What is the difference between a mode switch and a process switch?

 A process switch is what it is called when the processor switches from one thread/process to another. This causes the contents of the cpu registers and instruction pointer to be saved. 
 
 A mode switch is what is referred to when the cpu changes privilege levels.The currently executing process does NOT change during a mode switch.
