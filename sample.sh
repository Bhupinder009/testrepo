#!/bin/sh
Top_Dir=//home/sshuser/JUPITER/DEEP_LOGS
Latest_Logs=$(ls -td $Top_Dir/*/ | grep API.Test.Ecosystem | head -1)
Latest_test=$(ls -td $Latest_Logs*/ | grep TC_ | head -1)
cat ${Latest_test}Summary.txt
