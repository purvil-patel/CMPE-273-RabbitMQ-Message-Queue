**RabbitMQ Message Queue Testing**

**Introduction**
In this assignment, I installed RabbitMQ and ran Producer and Consumer applications to exchange 10,000 and 1,000,000 messages respectively. The primary goal was to ensure that no messages were lost during this process. Additionally, I captured video footage to provide visual evidence of the working model. In this report, I will present an overview of the assignment, the setup, the execution process, and the results obtained.

**Assignment Overview**
A message queue is a crucial component of messaging middleware solutions that facilitate communication between independent applications and services. Message queues ensure that messages are stored and processed in the order they are transmitted, even if the consuming application is not immediately ready. This asynchronous messaging model prevents data loss and enhances the reliability of distributed systems.

For this assignment, RabbitMQ, a popular message broker, was chosen as the messaging middleware solution. The primary objectives were as follows:

**Install RabbitMQ.**
Develop Producer and Consumer applications.
Exchange 10,000 messages using the Producer and Consumer applications.
Exchange 1,000,000 messages using the Producer and Consumer applications.
Capture video footage to document the processes.
Monitor the RabbitMQ message queue using a browser interface.

**Assignment Execution**
RabbitMQ Installation:
RabbitMQ was installed from: https://www.rabbitmq.com/install-homebrew.html

Producer and Consumer Applications:
Producer and Consumer applications were developed to interact with RabbitMQ. The Producer application was responsible for creating and sending messages to the RabbitMQ message queue, while the Consumer application consumed these messages.

Exchange of 10,000 Messages:
The Producer application was executed to send 10,000 messages to the RabbitMQ message queue. Simultaneously, the Consumer application was set up to consume these messages. This process was documented in the first video.


Exchange of 1,000,000 Messages:
Following the success of the initial test, the Producer application was executed again to send a more extensive batch of 1,000,000 messages to the RabbitMQ message queue. The Consumer application was configured to handle this higher message volume. This process was documented in the second video.

Message Queue Browser:
To ensure the reliability of message queuing, a browser interface for RabbitMQ was used to monitor the message queue. This interface allowed for real-time visualization of message counts and other queue-related statistics.

**Results**
Exchange of 10,000 Messages
The first video documented the successful exchange of 10,000 messages between the Producer and Consumer applications. At the end of the process, it was confirmed that all 10,000 messages were consumed without any loss.

Exchange of 1,000,000 Messages:
The second video documented the exchange of a more extensive batch of 1,000,000 messages. This test also concluded without any message loss, demonstrating the robustness and scalability of the RabbitMQ message queue.

Message Queue Browser:
The browser interface for RabbitMQ provided real-time monitoring of message counts and other queue statistics. It was observed that the message queue operated efficiently and reliably throughout both tests.

**Conclusion:**
The assignment successfully achieved its objectives of installing RabbitMQ, developing Producer and Consumer applications, and exchanging a significant number of messages without any data loss. The RabbitMQ message queue, with its asynchronous messaging model, proved to be a reliable solution for inter-application communication.

The use of video documentation further reinforced the reliability of the message queue system, as all 10,000 and 1,000,000 messages were accurately exchanged and consumed. The browser interface for monitoring the message queue provided additional assurance of the system's robustness.
