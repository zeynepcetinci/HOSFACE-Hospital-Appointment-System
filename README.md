# HOSFACE-Hospital-Appointment-System
Project used in hospitals created thanks to Python language

# HOSFACE-Hospital-Appointment-System
In our design, we include the following diagrams to illustrate the flow .
Use Case diagram
Face Recognition diagram
Data Flow diagram
SQLite Database diagram

It is necessary to say the specified command in order to make the first registration in the project we will do. Later, the application started with this command will open the camera, find the face object with the Haar-Cascade classification and try to determine who it belongs to by using the "OpenCv" library. The determined name will be scanned in the database of "Sqlite3" and it will check whether it exists in the patients table. The determined name will be scanned in the database of "Sqlite3" and it will check whether it exists in the patients table. At this stage, two possibilities arise. 

As a result of finding the existing face on my system, the only thing that should be done by the patient is to select the hospital department where he / she wants to make an appointment, while the patient makes this stage, the system puts the selected appointment on the table of the department where the patient wants to go and returns a sequence number to the patient according to the order in the table. 

As a result of not finding the existing face in the system, an interface with the information that the patient needs to enter will appear. Pictures are taken to be added to the "OpenCv" library, which will be useful in face matching. After the registration to the system is completed, the hospital department selection screen will appear before the patient, while the patient makes this stage, the system puts the selected appointment on the table of the department the patient wants to go to and returns a sequence number to the patient according to the order in the table.
