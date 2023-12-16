inpu = [i.strip().split('  ')[1] for i in '''  7  sudo
   8  adduser
   9  sudo adduser
   10  sudo adduser HraskoJ
   11  sudo adduser hraskoj
   12  users
   13  sudo groups bodorf
   14  sudo groups hraskoj
   15  audo addgroup spse
   16  sudo addgroup spse
   17  sudo adduser hraskoj
   18  sudo adduser hraskoj spse
   19  sudo groups hraskoj
   20  whoami
   21  exit
   22  sudo who
   23  sudo who -b
   24  sudo who -I
   25  sudo who -l
   26  sudo who -m
   27  sudo w
   28  sudo finger
   29  sudo finger -sl
   30  sudo finger -sl bodorf
   31  sudo finger -sl bodorf
   32  sudo finger bodorf
   33  finger -l
   34  sudo finger -l
   35  man finger
   36  sudo apt-get update
   37  sudo apt-get install finger
   38  sudo finger bodor
   39  finger hraskoj
   40  sudo apt-get update
   41  finger
   42  sudo finger bodorf
   43  su finger hraskoj
   44  wall upozornenie.txt
   45  ls
   46  ls la/home
   47  ls -la/home
   48  ls -la
   49  pws
   50  pwd
   51  cd dosuments
   52  cd documents
   53  cd /home
   54  cd
   55  ls
   56  cd documents
   57  cd //
   58  cd..
   59  cd ..
   60  cd ..
   61  cd documents
   62  cd /documents
   63  su
   64  cd ..
   65  cd ..
   66  cd /documents
   67  cd /home
   68  cd /dudascikd
   69  mkdir SPSE PRESOV
   70  edir PRESOV
   71  rdir PRESOV
   72  rmdir PRESOV
   73  cat upozornenie.txt
   74  cat test.txt
   75  touch PrazdnySubor.txt
   76  ls -l
   77  nano PrazdnySubor.txt
   78  rm PrazdnySubor.txt
   79  ls -l
   80  mv test.txt /Documents/test.txt
   81  mv /home/student/test.txt /home/student/archiv/test.txt
   82  mv /home/student/test.txt /home/documents/test.txt
   83  ls
   84  ls -l
   85  mv /home/student/test.txt /home/dokumenty/test.txt
   86  ls -l
   87  sudo chmod 4 test.txt
   88  ls -l
   89  sudo nano test.txt
   90  apt-cache
   91  apt-cache search mc
   92  pstree student
   93  sudo pstree student
   94  sudo pstree bodorf
   95  ps -l
   96  ps
   97  kill 1 PID
   98  ls -la
   99  history
  100  history >>4sa1_sxt4_history_bodor_filip.txt'''.split('\n')]


for i in inpu:
    print(i)