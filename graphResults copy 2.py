#FcfsScheduler Test0 Output.out
FcfsT0OUT = """"""

#FcfsScheduler Test1 Output.out
FcfsT1OUT = """"""


#FcfsScheduler Test2 Output.out
FcfsT2OUT = """"""

################################################################################

#FeedbackRRScheduler Test0 Output.out
FbT0OUT = """"""

#FeedbackRRScheduler Test1 Output.out
FbT1OUT = """"""

#FeedbackRRScheduler Test2 Output.out
FbT2OUT = """"""

################################################################################

#IdealSJFScheduler Test0 Output.out
IdealT0OUT = """"""

#IdealSJFScheduler Test1 Output.out
IdealT1OUT = """"""

#IdealSJFScheduler Test2 Output.out
IdealT2OUT = """"""


################################################################################

#RRScheduler Test0 Output.out
RRT0OUT = """"""

#RRScheduler Test1 Output.out
RRT1OUT = """"""

#RRScheduler Test2 Output.out
RRT2OUT = """"""

################################################################################

#SJFScheduler Test0 Output.out
SJFT0OUT = """"""

#SJFScheduler Test1 Output.out
SJFT1OUT = """"""

#SJFScheduler Test2 Output.out
SJFT2OUT = """"""


################################################################################
# Turning Fcfs data into 2D matrix
#10 processes
FcfsT0matrix = [list(map(int, line.split())) for line in FcfsT0OUT.split("\n")]

#50 processes
FcfsT1matrix = [list(map(int, line.split())) for line in FcfsT1OUT.split("\n")]

#150 processes
FcfsT2matrix = [list(map(int, line.split())) for line in FcfsT2OUT.split("\n")]

################################################################################
# Turning FeedbackRR data into 2D matrix
#10 processes
FbT0matrix = [list(map(int, line.split())) for line in FbT0OUT.split("\n")]

#50 processes
FbT1matrix = [list(map(int, line.split())) for line in FbT1OUT.split("\n")]

#150 processes
FbT2matrix = [list(map(int, line.split())) for line in FbT2OUT.split("\n")]

################################################################################
# Turning IdealSJF data into 2D matrix
#10 processes
IdealT0matrix = [list(map(int, line.split())) for line in IdealT0OUT.split("\n")]

#50 processes
IdealT1matrix = [list(map(int, line.split())) for line in IdealT1OUT.split("\n")]

#150 processes
IdealT2matrix = [list(map(int, line.split())) for line in IdealT2OUT.split("\n")]


################################################################################
# Turning RoundRobiun data into 2D matrix
#10 processes
RRT0matrix = [list(map(int, line.split())) for line in RRT0OUT.split("\n")]

#50 processes
RRT1matrix = [list(map(int, line.split())) for line in RRT1OUT.split("\n")]

#150 processes
RRT2matrix = [list(map(int, line.split())) for line in RRT2OUT.split("\n")]


################################################################################
# Turning Shortest job first data into 2D matrix
#10 processes
SJFT0matrix = [list(map(int, line.split())) for line in SJFT0OUT.split("\n")]

#50 processes
SJFT1matrix = [list(map(int, line.split())) for line in SJFT1OUT.split("\n")]

#150 processes
SJFT2matrix = [list(map(int, line.split())) for line in SJFT2OUT.split("\n")]


##calculating cpu utilization
def experiment1():



   # Print the 2D array
   #for row in FcfsT0matrix:
      # print(row[5])


   #for row in FcfsT1matrix:
      # print(row[5])

   for row in FbT2matrix:
      print(row[5])


experiment1()