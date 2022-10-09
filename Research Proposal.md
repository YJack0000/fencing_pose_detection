# Research Proposal

## Title
Recognizing fencing positions and actions using computer vision
## Motivation
The statistics on a fencer's performance, particularly the frequency and type of attacks initiated, are an valuable source of data and feedback that is frequently used for coaching and performance improvement. However, all statistics are generated through human annotation where experts use basic video play and pause functionality to collect raw statics. Vision-based approaches have the potential to detect these actions automatically, and to provide a high-level analysis of the action without the use of attached sensors on the athletes, which is forbidden by the rules of competition.
## Objective
The research aims to analyze the information through a video by recognize the athlete’s actions and positions.
Based on the analysis results, prople are able to get the statistics of the athlete’s performance.
## Related Work

## Methodology
(1) In ordered to train and validate our methods, we will collect fencer actions frames from videos. Than implement a simple service to make experts easily to label the frames. 

(2) To get a deeper feature of the actions of the fencer, we can use the method from BlazePose[2] to extract the keypoints of the fencer in specific frames. 

(3) We than able to train our models by combining fencers keypoints and annotated frames. The models will be used to recognize the fencer actions and positions.

(4) We will use the models to analyze the video and get the statistics of the fencer’s performance.
## Expectded Results

## References
[1]Valentin Bazarevsky, Ivan Grishchenko, Karthik Raveendran, Tyler Zhu, Fan Zhang, Matthias Grundmann, "BlazePose: On-device Real-time Body Pose tracking", 2020
[2]L.R.T. Williams, A Walmsley, "Response timing and muscular coordination in fencing: A comparison of elite and novice fencers", 2000
