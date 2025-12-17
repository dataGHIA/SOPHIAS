![Sin titulo](https://github.com/dataGHIA/SOPHIAS/blob/main/Images/sophias.png)
***
# About
Oral presentation skills are a critical component of higher education, yet comprehensive datasets capturing real-world student performance across multiple modalities remain scarce. To address this gap, we present **SOPHIAS** (*Student Oral Presentation monitoring for Holistic Insights & Analytics using Sensors*), a multimodal dataset containing recordings of **50 oral presentations** (10-minute presentation followed by 5-minute Q&A) delivered by **65 undergraduate and master’s students** at the Universidad Autónoma de Madrid.

SOPHIAS integrates **nine synchronized sensor streams**, including high-definition webcams, ambient and webcam audio, eye-tracking glasses, smartwatch physiological sensors, and clicker, keyboard, and mouse interactions. In addition, the dataset includes **slides** and **rubric-based evaluations** from teachers, peers, and self-assessments, along with **timestamped contextual annotations**.

The dataset captures presentations conducted in **real classroom settings**, preserving authentic student behaviors, interactions, and physiological responses. SOPHIAS enables the exploration of relationships between multimodal behavioral and physiological signals and presentation performance, supports the study of peer assessment, and provides a **benchmark for developing automated feedback and Multimodal Learning Analytics tools**.

The dataset is **publicly available for research** through GitHub and Science Data Bank.


# Motivation
Oral presentation skills constitute a core academic and professional competence for university students. The ability to communicate ideas clearly, confidently, and persuasively is essential for students’ future careers across disciplines. Despite their importance, many higher-education learners continue to struggle with structuring their messages, maintaining audience engagement, and managing anxiety during public speaking. **Structured instruction, guided practice, and explicit rubric-based feedback** are necessary for developing strong presentation skills.

Recent advances in **Multimodal Learning Analytics (MMLA)** highlight the importance of integrating multiple data streams such as video, audio, or interaction logs to obtain a richer and more holistic understanding of students’ performance [1]. These developments have led to the emergence of **automated feedback systems** designed to support learners during oral presentations. For example, MMLA-based tools integrate video, audio, posture, and interaction logs to generate real-time feedback on delivery, engagement, and slide usage, illustrating a growing trend toward **data-driven support for communication skills**. However, most existing systems are still evaluated with very small samples, often involving few presenters and tested in controlled laboratory environments rather than real classrooms, which limits their **external validity** and applicability to real educational settings.

To address this gap, we introduce **SOPHIAS** (*Student Oral Presentation monitoring for Holistic Insights & Analytics using Sensors*), a multimodal dataset capturing real-world oral presentations from **65 undergraduate and master’s students** at the Universidad Autónoma de Madrid. The dataset integrates **synchronized streams** from multiple platforms and sensors, including high-definition webcams, ambient audio, eye-tracking glasses, smartwatch physiological signals, PDF slides, clicker/keyboard/mouse interactions, rubric-based evaluations from teachers, peers, and self-assessments, as well as **timestamped contextual annotations**.

The dataset offers several unique contributions:  
1. **Real classroom recordings**: SOPHIAS preserves the spontaneity, pressure, and interaction patterns inherent to real presentations, elements typically absent in lab-based studies.  
2. **Multimodal synchronization**: Allows fine-grained exploration of relationships between biometric and behavioral signals.  
3. **Multiple evaluative perspectives**: Teacher, peer, and self-assessments create opportunities to study reliability, bias, and convergence across assessment sources, extending prior work on peer assessment reliability in oral communication settings.

In total, the dataset comprises **more than 380 GB of data**, making it one of the most extensive multimodal datasets available. It includes **50 presentations** in total (46 individual presentations and 4 group presentations), offering substantial variability in topics, delivery styles, group coordination patterns, and audience interaction.


# Sensors
The SOPHIAS dataset use a wide range of sensors, as shown in the acquisition setup during the data capture using the AICoFe system [2] and the edBB platform [3]:

![Sin titulo](https://github.com/dataGHIA/SOPHIAS/blob/main/Images/acquisition_setup.png)

- **Cameras:** Two external webcams were used to record the classroom:
  - **Presenter Camera (external):** A Logitech C920 PRO HD webcam was positioned in front of the presenter to capture a frontal RGB view of the entire presentation, operating at 20 Hz with a resolution of 1920 × 1080.
  - **Evaluators/Observer Camera (external):** A second Logitech C920 PRO HD webcam was oriented towards the audience area where the evaluators and the external observer were seated, operating at 20 Hz with a resolution of 1920 × 1080.  

  All video streams were encoded in standard MP4 format using the H.264 codec, and edBB recorded the exact capture timestamp of every frame, storing both UNIX and local time to enable synchronization across all sensors. The audio captured by the Logitech C920 PRO HD webcams was recorded at a sampling rate of 8 kHz.

- **Ambient microphone:** A Poly SYNC 40 omnidirectional speakerphone was positioned on the table, close to the presenter, and was connected to Microsoft Teams as the main audio input device. This non-intrusive microphone records the complete audio of the session at a 16 kHz sampling rate.

- **Fitbit Sense Smartwatches:** The presenter, the peer evaluators, and the external observer wore a Fitbit Sense smartwatch during each presentation. This device includes a photoplethysmography (PPG) sensor to estimate heart rate, a 3-axis accelerometer and 3-axis gyroscope to capture linear and rotational motion, and an orientation sensor that reports device position. Using Watch-DMLT, all smartwatch signals were recorded at 1 Hz and exported as structured, timestamped files, enabling reliable alignment and synchronization with other sensors. Heart rate is an important physiological marker that reflects the body's response to various emotional and cognitive states. Elevated heart rates are often observed during periods of stress, anxiety, or physical exertion, while lower heart rates are typically associated with relaxation and calmness.

- **Eye-tracking glasses:** One student acted as an external observer and wore Tobii Pro Glasses 3, a lightweight, head-mounted eye-tracking system designed for real-world research scenarios. The glasses use a binocular corneal-reflection, dark-pupil technique with stereo geometry to estimate gaze and eye orientation. The device captures binocular eye-tracking data at 50 Hz, including 3D gaze direction vectors, pupil diameter measurements, and eye-blink detection. In addition to the eye-tracking data, the glasses record a first-person scene video from a front-mounted camera at a resolution of 1920 × 1080 pixels and 25 fps, accompanied by 16-bit mono audio captured by the integrated microphone.

- **Slides:** The original presentation materials were collected in PDF format, corresponding to the slides used by each presenter. From these files, structural and design features can be extracted.

- **Clicker, mouse, and keyboard events:** Presenters advanced their slides using a wireless clicker, the mouse, or keyboard shortcuts. Since the clicker simply sent its commands in the form of keyboard-like keystroke events, both keyboard and clicker interactions were captured through the same logging mechanism. All interaction events were recorded with precise timestamps, including mouse movements, mouse clicks, and any keypress generated either by the physical keyboard or by the clicker (e.g., arrow keys, spacebar, PageUp/PageDown).

- **Assessment Data:** The AICoFe platform was used by teachers, peer evaluators, and presenters (for self-assessment) to complete a standardized rubric. For each presentation, AICoFe stores the score assigned to each rubric item and the free-text comments provided for that item by each assessment source (teacher, peer, and self). In addition, the platform records keystroke events generated during the assessment process, preserving the exact timestamps of each typed character. These keystroke logs provide fine-grained temporal information about evaluators’ commenting activity.

- **Contextual Event Annotations:** During each presentation, a research assistant used a dedicated annotation interface to mark contextual events in real time. The annotated events include nervous movements, episodes of reading directly from the slides or from written notes, explicit moments of eye contact with the audience, filler words, or the start and end timestamps of each individual question from the audience and each corresponding response from the presenter.  

  These annotations are stored with exact timestamps and later aligned with the sensor streams, providing high-quality labels for supervised learning and for validating automatic detections derived from video, audio, heart rate, or gaze data.

    
# Presentations
The dataset consists of recordings from **65 students** enrolled in face-to-face education at the **Universidad Autónoma de Madrid (UAM)**, who delivered oral presentations either individually or in groups.

- **Undergraduate students:**  
  - **Number:** 46 (40 male, 6 female)  
  - **Degree:** Final year of Telecommunication Technology and Service Engineering  
  - **Course:** Engineering and Society, which requires students to prepare and deliver a presentation on engineering-related topics  
  - **Presentation format:** Individual presentations  
  - **Duration:** 10 minutes, followed by 5 minutes of questions  

- **Master’s students:**  
  - **Number:** 19 (14 male, 5 female)  
  - **Degree:** Master in Data Science  
  - **Course:** Research Project in Data Science, where students write an academic paper and present it  
  - **Presentation format:** Group presentations (groups of 4–5 students)  
  - **Duration:** 15 minutes, plus 5 minutes for questions


# Code
Some data from the SOPHIAS dataset were preprocessed and included in the dataset along with the raw files:

- Smartwatch data were filtered to eliminate minor fluctuations and smooth the signals using Python scripts. [[Example of code for Heart Rate](https://github.com/dataGHIA/SOPHIAS/blob/main/Code/Heart_Rate_filtered_Example.py)] [[Example of code for Accelerometer](https://github.com/dataGHIA/SOPHIAS/blob/main/Code/Acc_filtered_Example.py)]
 

# Download Data
1) Download license agreement, send by email one signed and scanned copy to ghia.uam@gmail.com according to the instructions given.


2) Send an email to ghia.uam@gmail.com, as follows:

    Subject: [DATASET: SOPHIAS]


    Body: Your name, e-mail, telephone number, organization, postal mail, purpose for which you will use the dataset, time and date at which you sent the email with the signed license agreement.


3) Once the email copy of the license agreement has been received at ghia.uam@gmail.com, you will receive a link to download the dataset.


For more information, please contact: ghia.uam@gmail.com

 [Download license agreement](https://github.com/dataGHIA/SOPHIAS/blob/main/License/SOPHIAS_License_Agreement.pdf)

 # References
+ [1] Becerra, A., Cobos, R., & Lang, C. (2025). **Enhancing online learning by integrating biosensors and multimodal learning analytics for detecting and predicting student behaviour: a review**. Behaviour & Information Technology, 1–26. https://doi.org/10.1080/0144929X.2025.2562322 [[pdf](https://www.tandfonline.com/doi/epdf/10.1080/0144929X.2025.2562322?needAccess=true)]
+ [2] Becerra, A., & Cobos, R. (2025). **Enhancing the professional development of engineering students through an AI-based collaborative feedback system**. In 2025 IEEE Global Engineering Education Conference (EDUCON) (pp. 1–9). IEEE. https://doi.org/10.1109/EDUCON62633.2025.11016499 [[pdf] (https://ieeexplore.ieee.org/document/11016499)]
+ [3] Daza, R., Morales, A., Tolosana, R., Gomez, L. F., Fierrez, J., & Ortega-Garcia, J. **edBB-Demo: Biometrics and Behavior Analysis for Online Educational Platforms.** In Proceedings of the *AAAI Conference on Artificial Intelligence*, Vol. 37, No. 13, pp. 16422–16424, June 2023. [[pdf](https://arxiv.org/pdf/2211.09210)]

# Related works
- Daza, R., Becerra, A., Cobos, R. et al. **A multimodal dataset for understanding the impact of mobile phones on remote online virtual education**. Sci Data 12, 1332 (2025). https://doi.org/10.1038/s41597-025-05681-7 [[pdf](https://www.nature.com/articles/s41597-025-05681-7.pdf)]

- Becerra, A., Daza, R., Cobos, R., Morales, A., Cukurova, M., Fierrez, J. (2026). **AI-Based Multimodal Biometrics for Detecting Smartphone Distractions: Application to Online Learning**. In: Tammets, K., Sosnovsky, S., Ferreira Mello, R., Pishtari, G., Nazaretsky, T. (eds) Two Decades of TEL. From Lessons Learnt to Challenges Ahead. EC-TEL 2025. Lecture Notes in Computer Science, vol 16063. Springer, Cham. https://doi.org/10.1007/978-3-032-03870-8_3 [[pdf](https://doi.org/10.1007/978-3-032-03870-8_3)]

- Becerra, A., Mohseni, Z., Sanz, J., & Cobos, R. (2024). A generative AI-based personalized guidance tool for enhancing the feedback to MOOC learners. In 2024 IEEE Global Engineering Education Conference (EDUCON) (pp. 1–8). IEEE. https://doi.org/10.1109/EDUCON60312.2024.10578809 [[pdf]](https://doi.org/10.1109/EDUCON60312.2024.10578809)

- Becerra, A., Andres, D., Villegas, P., Daza, R., & Cobos, R. (2025). MOSAIC-F: A framework for enhancing students' oral presentation skills through personalized feedback. LASI-Spain 2025, Vitoria-Gasteiz, Spain. [[pdf]](https://arxiv.org/abs/2506.08634)

