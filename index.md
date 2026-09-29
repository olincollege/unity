# Welcome to Unity!

Olin has access to Unity, a supercomputer that is part of the [Massachusetts High Perfomance Computing Cluster](https://mghpcc.org/).


## Trainings

To use `pi_super_olin_edu` you must complete a training with a Supercomputer Assistant.

### Sign up 
Please sign up for a training here: 
https://docs.google.com/spreadsheets/d/1BDAYLLliPY7XcvwpESSEaG8keeRxzO_Yd16OdMRDPFE/edit?gid=0#gid=0


## Office Hours
Dhvan has office hours Wednesday 1-2 in the upper level of the library.
Evi will have regular office hours after trainings are complete.


## Things to know before a training!
If you've never used a command line to control a computer, welcome! We are so glad that you are learning new things with us. Please familiarize yourself with the command line following [this tutorial](https://labex.io/linuxjourney/courses/command-line) *before* your scheduled training. 

## What types of projects can I do on UNITY?
UNITY is great for anything that is tricky to run on your laptop. Use it for running 
- many instances of the same code (for example, 200 simulations with different parameters)
- tasks that take a long time (ex: 40 hours of API queries)
- projects that require heavy GPU processing (ex: [this project](https://mghpcc.org/olin-faculty-students-using-high-performance-computers-to-solve-big-challenges/)).
- live dashboards and interactive pages (ex: [Shiny](https://shiny.posit.co/py/gallery/))

UNITY is for open data projects! UNITY cannot be used for projects involving personally identifiable information, personal health information, controlled unclassified information, payment card information, FERPA-controlled information, etc. If we learn you have placed any sensitive data on UNITY, we will revoke your user account.

Make sure everything you do aligns with Unity’s terms of service: https://docs.unity.rc.umass.edu/about/terms-of-service/




### Unity Guidelines

We cover these points in the training. They are also here for your reference! 

- **This is a shared machine and your neighbors are real people at Olin!** An idle GPU you're sitting on can mean someone else is waiting. A full disk means your classmates can't do their homework. An excessive CPU request means that a professor can't do their research. 
- **Ask for what you need, not what you can get.** Over-requesting time, memory, or GPUs makes *you* wait longer in the queue and blocks other people. `seff [jobid]` after every job tells you what you actually used. You should never hesitate to request what you need. If you feel like your job is very big, please ask a supercomputer assistant for help! They can help you make it a more reasonable size while meeting your goals, and they can increase your usage limits if needed.
- **Don't run work on the login node.** It's for editing, moving files, and submitting jobs. Heavy compute there slows the front door for everyone. Most people should work in `/work/`
- **Don't hold resources you're not using.** Close interactive sessions when you walk away.
- **Learning matters more than the result.** Expect to make mistakes! Jobs will die in four seconds. You'll typo a path and request 200GB for something that needs 2. That's normal; right-size it next time.
- **No experience required, and no condescension tolerated** about anyone's code, tooling, or command-line comfort.
- **We really like questions.** "Is this a reasonable thing to run?" is a great one, and much better asked before you submit than after.
- **Report broken things.** Nodes fail and modules break. Post in channel `#supercomputer` on the Shop slack and report to Unity support instead of silently working around it.

### Data policy — the one rule with a penalty

No personally identifiable information, personal health information, controlled unclassified information, payment card information, or FERPA-controlled information. Unity is password-protected but is **not** a high-security environment, and Olin's account is for open-data projects.

This means no survey data with names attached, no interview recordings or transcripts with identifiable speakers, no scraped data with usernames, no medical or biometric datasets, no grades or student outcomes.

If you're unsure whether your data counts, **ask before you upload, not after** — deleting a file doesn't un-share it. 

Uploading personally identifiable information puts Olin at legal risk! In order for Olin to support this Unity account and allow everyone to use this resource, we need to ensure that this rule is followed. If it is not followed, we will revoke your access to Unity. 

If you have any questions about this, please reach out to Prof. Carrie Nugent.

### How to be a good neighbor

1. Do not store things on Unity that you're not using. If you're done with a project, move your files onto your personal computer and delete the Unity files. If your files are not used for a significant amount of time, we may delete them to create space.
2.  **Unity does not have backups.** Make sure you have your own backups of vital files! Don't let another user's mistake mess up your project.
3. Don't touch what isn't yours. Create your own directory to work in, and don't go in other people's directories.
4. Don't use excessive resoures. Roughly, most projects on `pi_super_olin_edu` should be less than 100 GB and not use more than 25 cores at a time. If your project needs more resources, that's great! We will work with you. Please reach out to a supercomputer assistant for guidance. 


## One backup is none, two backups are one
Always back up your files to your own computer! There are no automatic backups on Unity. We may be forced to delete extremely large files if our disk quota is exceeded. In addition, we may delete files that appear to be abandoned for long periods of time to free up space for active users.


## How to protect your files
The default on `pi_super_olin_edu` is that everyone can see and even delete everyone else's files. You can protect your files from accidental deletion by changing the permissions of the files [following this tutoria](https://labex.io/linuxjourney/courses/permissions). Don't hesitate to reach out for help if you're confused about this!

Changing the permisisons on your files will not prevent Carrie or the Supercomputer Assistants from reading or deleting your files. We try hard not to delete files, but will (for example) if your files are preventing others from using the resource, or if you do not seem to be actively using the files for a long period of time. 





### Getting help

There are so many ways to ask for help!

1. Ask on the `#supercomputer` channel of the Shop slack. Ask here for anything Olin-specific! Also a great, freindly place to ask general questions or get help if you're stuck. 
2. Attend Supercomputer Assistant office hours!
3. For specific technical questions, join the Unity slack and ask on their `#help-desk` channel: https://account.unityhpc.org/community-slack. Feel free to ask a question on the Olin `#supercomputer` slack first; we'll answer it if we can and direct you to `#help-desk` if we don't know the answer. 
4. Check out the Unity documentation (links below!)
5. Carrie Nugent is the faculty Supercomputer Liaison. Feel free to chat with her about PI (faculty/staff-level) accounts and specialized compute needs.


**Helpful Documentation**
- Table of contents: https://docs.unity.rc.umass.edu/documentation/toc/
- Quickstart: https://docs.unity.rc.umass.edu/documentation/get-started/quickstart/
- OnDemand: https://docs.unity.rc.umass.edu/documentation/connecting/ondemand/
- SSH: https://docs.unity.rc.umass.edu/documentation/connecting/ssh/
- Jobs: https://docs.unity.rc.umass.edu/documentation/jobs/
- Git: https://docs.unity.rc.umass.edu/documentation/get-started/git-guide/
- Terms of service: https://docs.unity.rc.umass.edu/about/terms-of-service/
- Partition list: https://docs.unity.rc.umass.edu/documentation/cluster_specs/partitions/
- Storage & quotas: https://docs.unity.rc.umass.edu/documentation/cluster_specs/storage/
- Scratch workspaces: https://docs.unity.rc.umass.edu/documentation/managing-files/hpc-workspace/
- Python venv: https://docs.unity.rc.umass.edu/documentation/software/venv/
- JupyterLab OnDemand: https://docs.unity.rc.umass.edu/documentation/software/ondemand/jupyterlab-ondemand/
- Unity helper scripts (`unity-slurm-*`): https://docs.unity.rc.umass.edu/documentation/jobs/helper_scripts/
