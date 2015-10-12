#=======================================================================================
# This sample uses the demo Derby Server that is installed with your product.
# Before starting the Administration Server, you should start the demo Derby server
# by issuing one of the following commands:
#
# startdb
#
# Please note that some of the values used in this script are subject to change based on 
# your WebLogic installation and the template you are using.
#
# Usage: 
#      java weblogic.WLST <WLST_script> 
#
# Where: 
#      <WLST_script> specifies the full path to the WLST script.
#=======================================================================================

#=======================================================================================
# Open a domain template.
#=======================================================================================

DOMAIN_HOME=os.environ["DOMAIN_HOME"]
WL_HOME=os.environ["WL_HOME"]
readTemplate(WL_HOME+"/common/templates/wls/wls.jar")

#=======================================================================================
# Configure the Administration Server and SSL port.
#
# To enable access by both local and remote processes, you should not set the 
# listen address for the server instance (that is, it should be left blank or not set). 
# In this case, the server instance will determine the address of the machine and 
# listen on it. 
#=======================================================================================

cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', 7001)


#=======================================================================================
# Define the user password for weblogic.
#=======================================================================================

cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('welcome1')


#=======================================================================================
# Configure Coherence Cluster
#=======================================================================================
cd('/')

create('Coherence-0', 'CoherenceClusterSystemResource')



#=======================================================================================
# Create and configure a JDBC Data Source, and sets the JDBC user.
#=======================================================================================

cd('/')
create('sample', 'JDBCSystemResource')
cd('JDBCSystemResource/sample/JdbcResource/sample')
create('myDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName','org.apache.derby.jdbc.EmbeddedDriver')
set('URL','jdbc:derby:demo/sample;create=true')
set('PasswordEncrypted', 'app')
set('UseXADataSourceInterface', 'false')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
create('user', 'Property')
cd('Property/user')
cmo.setValue('app')

cd('/JDBCSystemResource/sample/JdbcResource/sample')
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String("jdbc/sample"))

#=======================================================================================
# Application Deployment
#=======================================================================================

cd('/')
create('my-demo-app-ear-1.0-SNAPSHOT','AppDeployment')
cd('/AppDeployment/my-demo-app-ear-1.0-SNAPSHOT')
set('SourcePath',DOMAIN_HOME+'/../my-demo-app-ear-1.0-SNAPSHOT.ear')
set('ModuleType','ear')
set('Target','AdminServer')

#=======================================================================================
# Target resources to the servers. 
#=======================================================================================

cd('/')
assign('JDBCSystemResource', 'sample', 'Target', 'AdminServer')
#assign('CoherenceClusterSystemResource', 'Coherence-0', 'Target', 'AdminServer')

#=======================================================================================


#=======================================================================================
# Define JNDI for  Proxy Config Override
#=======================================================================================

#cd('/CoherenceClusterSystemResources/Coherence-0')
#create('CacheConfig-0','CoherenceCacheConfig')

#cd('CoherenceCacheConfigs/CacheConfig-0')
#set('JNDIName', "MyGAR")
#set('CacheConfigurationFile','demo/proxy-cache-config.xml')
#set('Targets','AdminServer')

#=======================================================================================
# Write the domain and close the domain template.
#=======================================================================================

setOption('OverwriteDomain', 'true')

writeDomain(DOMAIN_HOME)
closeTemplate()

#=======================================================================================
# Exit WLST.
#=======================================================================================

exit()
