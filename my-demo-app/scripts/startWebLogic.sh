#!/bin/sh

# PROJDIR refers to the directory where you extracted the zip file
# JAVA_HOME set to JDK8 INSTALL
# MW_HOME SHOULD BE SET FOR RUNNING setWLSEnv.cmd from your WLS 12c (12.1.3) install (~wlserver/bin/setWLSEnv.cmd)


JAVA_HOME=/u01/java/jdk1.8.0_51
export JAVA_HOME

MW_HOME=/u01/fmw/wls12130
export MW_HOME

WL_HOME=$MW_HOME/wlserver
export WL_HOME

PROJDIR=`pwd`
export PROJDIR

CONFIG_SCRIPT=${1-basic}MCSDomain.py




TESTAPP=my-demo-app-ear-1.0-SNAPSHOT.ear

if [ ! -f my-demo-app-gar-1.0-SNAPSHOT.gar ]; then
# PREPARE EAR FILE
 mkdir lib

 cp $MW_HOME/coherence/lib/coherence-rest.jar lib
 cp $MW_HOME/oracle_common/modules/oracle.toplink_12.1.3/toplink-grid.jar lib

 $JAVA_HOME/bin/jar xvf $TESTAPP my-demo-app-gar-1.0-SNAPSHOT.gar

 $JAVA_HOME/bin/jar uvf my-demo-app-gar-1.0-SNAPSHOT.gar lib

 $JAVA_HOME/bin/jar uvf $TESTAPP my-demo-app-gar-1.0-SNAPSHOT.gar 

 # CLEANUP

 rm -rf lib

fi

.  $WL_HOME/server/bin/setWLSEnv.sh


DOMAIN_HOME=$PROJDIR/mydomain
export DOMAIN_HOME

JAVA_OPTIONS="-XX:+UnlockCommercialFeatures -XX:+FlightRecorder"

USER_MEM_ARGS="-Xms512m -Xmx512m -XX:MaxPermSize=256m"


if [ ! -d $DOMAIN_HOME ]; then
   echo "Using ${CONFIG_SCRIPT} to create domain"
   $JAVA_HOME/bin/java weblogic.WLST $PROJDIR/${CONFIG_SCRIPT}
fi


# COPY DERBY JARs to DOMAIN_HOME/lib

if [ ! -f $DOMAIN_HOME/lib/derby.jar ]; then

	cp $JAVA_HOME/db/lib/derby.jar $DOMAIN_HOME/lib
	cp $JAVA_HOME/db/lib/derbyclient.jar $DOMAIN_HOME/lib
fi


# Create and Load Sample data

if [ ! -d $DOMAIN_HOME/demo ]; then
    mkdir $DOMAIN_HOME/demo
    $JAVA_HOME/bin/java -jar $JAVA_HOME/db/lib/derbyrun.jar ij sample.sql
    echo "$JAVA_HOME/bin/java -jar $JAVA_HOME/db/lib/derbyrun.jar server start" > $DOMAIN_HOME/demo/startDB.sh
    echo "MW_HOME=$MW_HOME ../bin/startNodeManager.sh" > $DOMAIN_HOME/demo/startNM.sh
   cd ${PROJDIR}
fi

echo "DOMAIN HOME=$DOMAIN_HOME"
echo "Starting Server `date`"
$DOMAIN_HOME/bin/startWebLogic.sh noderby 
