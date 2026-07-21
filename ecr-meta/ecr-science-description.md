# RGB Color Statistics Edge Application

This project demonstrates an edge computing application using the SAGE/Waggle platform. The application captures images from a camera and performs image analysis directly on an edge device instead of sending raw data to the cloud.

The goal of this application is to demonstrate how edge computing can reduce latency and enable real-time processing in environments where network connectivity may be limited. The application processes images locally and extracts useful information by calculating RGB color statistics.

For each captured image, the application computes the mean, minimum, and maximum values for the red, green, and blue color channels. These measurements provide a simple example of extracting scientific information from visual data. The calculated values are published through the Waggle plugin system, allowing other SAGE services to access and analyze the results.

This approach can be extended to many scientific applications, including environmental monitoring, wildlife observation, and remote sensing. Instead of transferring large amounts of image data, edge devices can analyze images near the data source and only transmit important results.

This project highlights the ability of edge AI and computing platforms like SAGE to support real-time scientific workflows.
