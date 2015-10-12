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
# Configure Dynamic Cluster
#=======================================================================================
cd('/')
create('machine-1','Machine')
cd('/Machines/machine-1')
create('machine-1','NodeManager')
cd('NodeManager/machine-1')
set('NMType','Plain')
cd('/NMProperties')
set('SecureListener','false')


#=======================================================================================
# Create Data Tier 
#=======================================================================================
cd('/')
create('DataTier','Cluster')

cd('/')
create('cache-server-tmp','ServerTemplate')
cd('/ServerTemplates/cache-server-tmp')
set('ListenPort',8100)
set('Machine','machine-1')
set('Cluster','DataTier')

cd('/Clusters/DataTier')
create('DataTier','DynamicServers')
create('DataTier','CoherenceTier')
cd('DynamicServers/DataTier')
set('ServerNamePrefix','CacheServer-')
set('ServerTemplate','cache-server-tmp')
set('MaximumDynamicServerCount',2)
cd('/Clusters/DataTier/CoherenceTier/DataTier')
set('LocalStorageEnabled',true)



#=======================================================================================
# Create App Tier 
#=======================================================================================
cd('/')
create('AppTier','Cluster')

cd('/')
create('app-server-tmp','ServerTemplate')
cd('/ServerTemplates/app-server-tmp')
set('ListenPort',7100)
set('Machine','machine-1')
set('Cluster','AppTier')
#set('LocalStorageEnabled',false)

cd('/Clusters/AppTier')
create('AppTier','DynamicServers')
create('AppTier','CoherenceTier')
cd('DynamicServers/AppTier')
set('ServerNamePrefix','AppServer-')
set('ServerTemplate','app-server-tmp')
set('MaximumDynamicServerCount',2)
cd('/Clusters/AppTier/CoherenceTier/AppTier')
set('LocalStorageEnabled',false)



#=======================================================================================
# Create Proxy Tier 
#=======================================================================================
cd('/')
create('ProxyTier','Cluster')

cd('/')
create('proxy-server-tmp','ServerTemplate')
cd('/ServerTemplates/proxy-server-tmp')
set('ListenPort',7100)
set('Machine','machine-1')
set('Cluster','ProxyTier')
#set('LocalStorageEnabled',false)

cd('/Clusters/ProxyTier')
create('ProxyTier','DynamicServers')
create('ProxyTier','CoherenceTier')
cd('DynamicServers/ProxyTier')
set('ServerNamePrefix','ProxyServer-')
set('ServerTemplate','proxy-server-tmp')
set('MaximumDynamicServerCount',2)
cd('/Clusters/ProxyTier/CoherenceTier/ProxyTier')
set('LocalStorageEnabled',false)



#=======================================================================================
# Define JNDI for  Proxy Config Override
#=======================================================================================

cd('/CoherenceClusterSystemResources/Coherence-0')
create('CacheConfig-0','CoherenceCacheConfig')

cd('CoherenceCacheConfigs/CacheConfig-0')
set('JNDIName', "MyGAR")
set('CacheConfigurationFile','demo/proxy-cache-config.xml')
set('Targets','ProxyTier')



#=======================================================================================
# Create and configure a JDBC Data Source, and sets the JDBC user.
#=======================================================================================

cd('/')
create('sample', 'JDBCSystemResource')
cd('JDBCSystemResource/sample/JdbcResource/sample')
create('myDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName','org.apache.derby.jdbc.ClientDriver')
set('URL','jdbc:derby://localhost:1527/sample;create=true')
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
set('JNDIName', 'jdbc/sample')


#######

cd('/')
create('my-demo-app-ear-1.0-SNAPSHOT','AppDeployment')
cd('/AppDeployment/my-demo-app-ear-1.0-SNAPSHOT')
set('SourcePath',DOMAIN_HOME+'/../my-demo-app-ear-1.0-SNAPSHOT.ear')
set('ModuleType','ear')
set('Target','AppTier')


cd('/')
create('my-demo-app-gar-1.0-SNAPSHOT','AppDeployment')
cd('/AppDeployment/my-demo-app-gar-1.0-SNAPSHOT')
set('SourcePath',DOMAIN_HOME+'/../my-demo-app-gar-1.0-SNAPSHOT.gar')
set('ModuleType','gar')
set('Target','DataTier,AppTier,ProxyTier')

####

#=======================================================================================
# Target resources to the servers. 
#=======================================================================================

cd('/')
assign('JDBCSystemResource', 'sample', 'Target', 'DataTier,AppTier,ProxyTier')
cd('/')
#unassign('Server','AdminServer','CoherenceClusterSystemResource','Coherence-0')
#cd('/Server/AdminServer')
#set('CoherenceClusterSystemResource',false)
#=======================================================================================

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
