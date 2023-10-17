**RabbitMQ Message Queue Testing**

**Introduction**

In this assignment, I installed RabbitMQ and ran Producer and Consumer applications to exchange 10,000 and 1,000,000 messages respectively. The primary goal was to ensure that no messages were lost during this process. Additionally, I captured video footage to provide visual evidence of the working model. In this report, I will present an overview of the assignment, the setup, the execution process, and the results obtained.

**Assignment Overview**

A message queue is a crucial component of messaging middleware solutions that facilitate communication between independent applications and services. Message queues ensure that messages are stored and processed in the order they are transmitted, even if the consuming application is not immediately ready. This asynchronous messaging model prevents data loss and enhances the reliability of distributed systems.

For this assignment, RabbitMQ, a popular message broker, was chosen as the messaging middleware solution. 

**The primary objectives were as follows:**

Install RabbitMQ.

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



https://github.com/purvil-patel/CMPE-273-RabbitMQ-Message-Queue/assets/67355397/4e6c8638-8c0e-44f8-b25e-04d1a5c921bd


Exchange of 1,000,000 Messages:

Following the success of the initial test, the Producer application was executed again to send a more extensive batch of 1,000,000 messages to the RabbitMQ message queue. The Consumer application was configured to handle this higher message volume. This process was documented in the second video.



https://github.com/purvil-patel/CMPE-273-RabbitMQ-Message-Queue/assets/67355397/554ab7e5-a8fc-4030-887b-110e51931592



Message Queue Browser:

To ensure the reliability of message queuing, a browser interface for RabbitMQ was used to monitor the message queue. This interface allowed for real-time visualization of message counts and other queue-related statistics.

**Results**

Exchange of 10,000 Messages:

The first video documented the successful exchange of 10,000 messages between the Producer and Consumer applications. At the end of the process, it was confirmed that all 10,000 messages were consumed without any loss.

Exchange of 1,000,000 Messages:

The second video documented the exchange of a more extensive batch of 1,000,000 messages. This test also concluded without any message loss, demonstrating the robustness and scalability of the RabbitMQ message queue.

Message Queue Browser:

The browser interface for RabbitMQ provided real-time monitoring of message counts and other queue statistics. It was observed that the message queue operated efficiently and reliably throughout both tests.

**Conclusion:**

The assignment successfully achieved its objectives of installing RabbitMQ, developing Producer and Consumer applications, and exchanging a significant number of messages without any data loss. The RabbitMQ message queue, with its asynchronous messaging model, proved to be a reliable solution for inter-application communication.

The use of video documentation further reinforced the reliability of the message queue system, as all 10,000 and 1,000,000 messages were accurately exchanged and consumed. The browser interface for monitoring the message queue provided additional assurance of the system's robustness.


**Additional Scenario: Asynchronous Messaging with 10,000 Messages**

**Scenario Overview:**

In addition to the initial objectives, an additional scenario was conducted to stress test the asynchronous messaging capabilities of RabbitMQ. This scenario aimed to run the Producer application 1,000,000 times and ensure that the Consumer application correctly processed the same count of messages.

**Execution:**

Running Producer 10,000 Times: To test the resilience and scalability of RabbitMQ's asynchronous messaging model, the Producer application was executed a total of 10,000 times. Each instance of the Producer application generated and sent a message to the RabbitMQ message queue. This process was automated and documented for accuracy.


https://github.com/purvil-patel/CMPE-273-RabbitMQ-Message-Queue/assets/67355397/6b73f70a-2acd-4eaa-9a75-f1dec52784e0




Consumer Application Verification: After all 10,000 messages were sent to the message queue, the Consumer application was run to consume these messages. The key objective was to verify that the Consumer application processed the same count of messages, ensuring that no data was lost in the asynchronous message exchange.

**Results:**

Upon completion of the additional scenario, it was confirmed that all 10,000 messages generated by the Producer applications were successfully consumed by the Consumer application. This test not only reaffirmed the reliability of RabbitMQ but also demonstrated its ability to handle a significant message load in an asynchronous manner.

**Conclusion:**

The additional scenario, where 10,000 messages were exchanged and processed without any data loss, further highlights the robustness and scalability of the RabbitMQ message queue for asynchronous messaging. This capability ensures that even in high-demand environments, messages are stored and processed reliably, and no data is lost during transmission.

This section adds the details of the additional scenario that you wanted to accommodate in the report, demonstrating the successful exchange of 10,000 messages in an asynchronous manner using RabbitMQ.

