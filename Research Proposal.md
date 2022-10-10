# Research Proposal

## Title
Recognizing fencing positions and actions using computer vision

## Motivation
The statistics on a fencer's performance, particularly the frequency and type of attacks initiated, are an valuable source of data and feedback that is frequently used for coaching and performance improvement[1]. However, all statistics are generated through human annotation where experts use basic video play and pause functionality to collect raw statics. Vision-based approaches have the potential to detect these actions automatically, and to provide a high-level analysis of the action without the use of attached sensors on the athletes, which is forbidden by the rules of competition.

## Objective
The research aims to analyze the information through a video by recognize the athlete’s actions and positions.
Based on the analysis results, people are able to get the statistics of the athlete’s performance.

## Related Work
1. Object detection method

    Object detection consists of various approaches and have solved the challenges of data limitation and modeling in object detection. However, they are not able to detect objects in a single algorithm run. You Only Look at Once(YOLO) algorithm has gained popularity because of its superior performance.

2. Pose estimation method
   
   Their are two main types of approaches for pose estimation: bottom-up and top-down. The top-down approaches first obtain human candidates by a human detector, and then perform single-person pose estimation. While the bottom-up approaches directly predict the keypoints all at once, and then assemble them into the full poses for all persons.
   
   Although the bottom up approach are more suitable for multi-person pose estimation because of the speed, the top-down approach is more suitable for our senario because there is at most two person to estiamte. Moreover, single-person pose estimation have higher the accuracy.[2]

## Methodology
1. In ordered to train and validate our methods, we will collect fencer actions frames from videos. Than cropped the fencer out by using object detection models such as YOLOv4[3]. 
2. Implement a simple service to make experts easily to label the frames. 
3. To get a deeper feature of the actions of the fencer, we can use the method from BlazePose[4] to extract the keypoints of the fencer in specific frames. 
4. We than able to train our models by combining fencers keypoints and annotated frames. The models will be used to recognize the fencer actions and positions.
5. We will use the models to analyze the video and get the statistics of the fencer’s performance.

## Expectded Results
It is expected that through our framework, we are able to have an easier way to get an athlet insight of performance. Also, raise people's awareness of the potential of combination of technology and sport. 

## References
[1]L.R.T. Williams, A Walmsley, "Response timing and muscular coordination in fencing: A comparison of elite and novice fencers", 2000

[2]Sarah Mroz, Natalie Baddour, Connor J C McGuirk, Pascale Juneau, "Comparing the Quality of Human Pose Estimation with BlazePose or OpenPose", 2021

[3]Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi, "You Only Look Once: Unified, Real-Time Object Detection", 2015

[4]Valentin Bazarevsky, Ivan Grishchenko, Karthik Raveendran, Tyler Zhu, Fan Zhang, Matthias Grundmann, "BlazePose: On-device Real-time Body Pose tracking", 2020

[5]Zhe Cao, Gines Hidalgo, Tomas Simon, Shih-En Wei, Yaser Sheikh, "OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields", 2018
