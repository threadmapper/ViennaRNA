Bootstrap: localimage
From: ../biopython.simg

%labels
    maintainer Jitender(CSB)
    application MASTlite
    applicationversion 0.1
    institute JIC
    provides Mastlite

%environment
    export LANG=C
    export PATH=/opt/miniconda3/bin:$PATH

%files
     ./ViennaRNA-2.4.18.1.tar.gz  /opt/miniconda3/


%post
    apt-get install -y pkg-config
    apt-get install -y autoconf
    apt-get install -y libtool
    apt-get install -y gengetopt 
    apt-get install -y help2man
    apt-get install -y flex
    apt-get install -y bison 
    apt-get install -y xxd
    apt-get install -y texinfo 
#    apt-get install -y yacc 
    apt-get install -y bison++
    apt-get install -y byacc  

    export MINICONDA_PATH=/opt/miniconda3/bin
    export PATH=/opt/miniconda3/bin:/opt/software/jitu_jelly/bin:$PATH

  
    mkdir -p /opt/software


    cd /opt/miniconda3/
    #wget https://github.com/threadmapper/ViennaRNA/archive/refs/tags/2.4.18.1.tar.gz  .

    tar -xzvf ViennaRNA-2.4.18.1.tar.gz
    cd ViennaRNA-2.4.18.1/

    cd src
    tar -xzf libsvm-3.24.tar.gz
    cd ..
 
    autoreconf -fi

    ./configure --without-swig --without-forester
    make && make install && make clean


%environment
    export PATH=/opt/miniconda3/bin:$PATH
    export LC_ALL=C


%runscript
    alias python3='python3.7'
    eval ${@}     

