# Homework 6: Julia's Youtube Channel
1.  Where does Julia Cartwright work?  National Instruments
2.  What is PREEMPT_RT?  PREEMPT_RT makes Linux into a real-time system, and will be eventually incorporated into mainline Linux kernels.
3.  What is mixed criticality?  Interrupt requests that handle both critical and non-critical requests.
4.  How can drivers misbehave?  IRQ events are too long to interrupt the scheduler.
5.  What is delta?  It is the passage of time between start of event to trigger the launch of the application, and the application launching.
6.  What is cyclic tests?  A measuring test that repeatedly measures the difference between thread's intended wake-up time and the time at which it actually wakes up.
7.  What is Fig2?  An external event that is trying to launch in a Non-rt system after an IRQ request to launch the application.
8.  Dispatch latency is the latency between the trigger for an interrupt and the actual launching of the interrupt.
    Scheduling latency is the length of time beween when the scheduler is given a task and when it starts the task.
9.  What is mainline?  The main processor code execution that can be interrupted from by IRQ requests.
10.  What keeps external event from starting?  The non critical IRQ
11.  RT systems allows the interrupt requests to be interrupted themselves, so the external event begins on time, and then IRQ is finished afterwards.

# Homework 6: PREEMPT_RT
PREEMPT_RT had faster response time and finished the make load quicker.
### With load
Load was the repeated make of the linux exercise modules.
Module files were loaced in ~/exercises/linux/modules.
RT has a bounded latency of 10 microseconds.
Non-RT has a bounded latency of 25 microseconds.
![Tests with load](https://github.com/EricMorse/ECE434/tree/master/hw06/rt/cyclictestwload.png)

### Without load
No load.
RT has a bounded latency of 10 microseconds.
Non-RT has a bounded latency of 20 microseconds.
![Tests without load](https://github.com/EricMorse/ECE434/tree/master/hw06/rt/cyclictestnoload.png)

