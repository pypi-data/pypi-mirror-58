#coding: utf-8
import os
import sys
sys.tracebacklimit=0
import platform
import subprocess
import getpass

def install():
    jpath = 'notSet'
    while (jpath == 'notSet'):
        jpath=javapath()
    server_type = ''
    while (server_type != 'tomcat' and server_type != 'jboss'):
        server_type=server_name()
    sigma_status = ''        
    while (sigma_status != 'Y' and sigma_status != 'N'):
        sigma_status=sigma_install()
    folder_value=''                
    while (folder_value != 'Y' and folder_value != 'N' and folder_value !='NEW'):
        folder_value=folder_check()
    if(folder_value == 'Y' or folder_value == 'NEW'):
        download_app(server_type,sigma_status)
    app_server_path = server_validation(server_type)
    app_install(app_server_path,sigma_status,server_type)
    db_type=''
    dbsir=''    
    while (db_type != 'Oracle' and db_type != 'MySQL'):
        db_type=dbselect()
    if(db_type=='MySQL'):
        connection_status=''           
        while (connection_status != 'success'):
            dbvalues=dbinput()            
            connection_status=connection_check(dbvalues[:])
        dos2unixValidate()
        runDBScript(dbvalues[:],sigma_status)
    else:                
        dbvalues=dbinput()
        dbsir=additionalInput()    
    update_dbentries(server_type,db_type,app_server_path,sigma_status,dbvalues[:],dbsir)
    pathReplacePDF()
    copyTransactionJars(server_type,app_server_path)
    finish(server_type,db_type)
    
def javapath():
    platform_check = platform.system()
    print platform_check
    if(platform_check == "Linux" or platform_check == "Darwin"):
        javapath=raw_input('Enter Java path(Minimum java version is 1.8+) : ')                  
        java_string = javapath + " -version 2>&1 | awk -F[\\\"\.] -v OFS=. \'NR==1{print $2,$3}\'"        
        java_version = subprocess.check_output(java_string, shell=True)        
        if(java_version.strip() == '.'):
            print "Please Enter the valid Java Path"
            return 'notSet'
        java_float = 0.0
        try:
            java_float = float(java_version)
        except ValueError:
            java_float = float(java_version.split("-")[0])                    
        if (float(java_float) >= 1.8):
            print 'Java Version Compertable with the bench mark. Lets Proceed Further!!! \n'
        else:
            print 'Java version not supported!!! \n'
            exit()        
        return javapath     

def server_name():
    server_value=raw_input('Enter Server Preference 1.Tomcat 2.Jboss (input 1 or 2): ')    
    val = 0
    try:
        val = int(server_value)
    except ValueError:
        print("input is not valid, Try again!!!")
        return ''
    if(val ==1 or val==2):
        if(val ==1):
            print 'You have choose Tomcat as your Application Server \n'
            return 'tomcat'
        if(val ==2):
            print 'Sorry for the inconvenience it is in progress...'
            exit()
            return 'jboss'            
    else:
        print 'Choose between 1 and 2'
        print 'Please try again!!!'
        return ''

def sigma_install():
    value = ''
    sigma_value=raw_input("Do you want to install Sigma Application also (input 'Y' or 'N'): ")    
    try:
        value = str(sigma_value)
    except ValueError:
        print("Please enter valid ones possible values are 'Y' or 'N'")
        return ''
    if(value =='Y'):
        print 'You have choose to install Sigma Application \n'
        return value            
    if(value =='N'):
        print 'No Need to install sigma proceed with the default installation \n'
        return value
    else:
        print "Please enter valid ones possible values are 'Y' or 'N'"
        print 'Please try again!!!'
        return ''

def folder_check():    
    if os.path.exists(os.path.expanduser("~/.canvas")):
            uservalue=raw_input("canvas folder already exists.\n Do yo want to clear the folder(input 'Y' or 'N') Note: For the latest version of CT (Input as 'Y') : ")            
            try:
                uservalue = str(uservalue)            
            except ValueError:
                print("Please enter valid ones possible values are 'Y' or 'N'")
                return ''
            if(uservalue =='Y'):
                subprocess.check_output("rm -rf ~/.canvas && mkdir ~/.canvas", shell=True)        
                print "Updating the canvas home folder...\n"
                return uservalue            
            if(uservalue =='N'):
                print 'Canvas folder is same as the previous version...\n'        
                return uservalue
            else:
                print "Please enter valid ones possible values are 'Y' or 'N'"
                print 'Please try again!!!'
                return ''
    else:
        print "Creating the canvas folder in home directory"        
        subprocess.check_output("mkdir ~/.canvas", shell=True)       
        return 'NEW'

def download_app(server_type,sigma_status):
    if(server_type == 'tomcat'):        
        subprocess.check_output("curl -v -u admin:admin123 http://172.19.29.253:8081/repository/Release/19/tomcat/expertctstudio.war -O && curl  -v -u admin:admin123 http://172.19.29.253:8081/repository/Release/19/tomcat/ctmodelhouse.war -O && mv ./expertctstudio.war ~/.canvas/expertctstudio.war &&  mv ./ctmodelhouse.war ~/.canvas/ctmodelhouse.war && chmod +x ~/.canvas/*",shell=True)
    subprocess.check_output("curl -v -u admin:admin123 http://172.19.29.253:8081/repository/Release/19/tmpl.zip -O && unzip tmpl.zip -d ~/.canvas/tmpl/ && rm -rf tmpl.zip", shell=True)
    subprocess.check_output("mkdir ~/.canvas/template", shell=True)            
    subprocess.check_output("rm -rf ~/.canvas/ExpertModeCTStudio && rm -rf ~/.canvas/Modelhouse && rm -rf ~/.canvas/sigma && rm -rf ~/.canvas/transactionjars && rm -rf ~/.canvas/canvasSetup_MYSQL.zip && rm -rf ~/.canvas/canvasSetup_oracle.zip  && curl  -v -u admin:admin123 http://172.19.29.253:8081/repository/Release/19/dependencies.zip -O && unzip dependencies.zip -d ~/.canvas/ && rm -rf dependencies.zip", shell=True)
    subprocess.check_output("chmod -R 777 ~/.canvas", shell=True)
    if(sigma_status=="Y"):
        subprocess.check_output("curl  -v -u admin:admin123 http://172.19.29.253:8081/repository/Release/19/tomcat/sigma.war -O && mv sigma.war ~/.canvas/sigma.war && chmod +x ~/.canvas/*", shell=True)
    else:
        print "Skipping the download of Sigma as User Preference"

def server_validation(server_type):    
    if (server_type == 'tomcat'):
        tomcatpath=raw_input('Enter Tomcat base path(If you dont have tomcat Please install tomcat with portable version) : ')        
        if not os.path.exists(tomcatpath):
            print "Tomcat Server and related files does not exist && please recheck it once and try again \n"
            tomcatpath=raw_input('Enter Tomcat base path(If you dont have tomcat Please install tomcat) : ')            
            if not os.path.exists(tomcatpath):
                print "Tomcat Server and related files does not exist && you have exceed your limit please install tomcat and try again with portable version \n"
                exit()            
        elif not os.path.exists(tomcatpath+ "/webapps"):
            print 'unable to find the Webapps folder: '+tomcatpath+ '/webapps'
            print 'Note:Please install tomcat as a portable version. so that we can proceed \n'
            exit()
        elif not os.path.exists(tomcatpath+ "/conf/server.xml"):
            print 'unable to find server.xml: '+tomcatpath+ '/conf/server.xml Missing!!!'
            print 'Note:Please install tomcat as a portable version. so that we can proceed \n'
            exit()
        elif not os.path.exists(tomcatpath+ "/conf/context.xml"):
            print 'unable to find context.xml: '+tomcatpath+ '/conf/context.xml Missing!!!'
            print 'Note:Please install tomcat as a portable version. so that we can proceed \n'
            exit()
        else:
            return tomcatpath
                
def app_install(app_server_path,sigma_status,server_type):
    if(server_type=='tomcat'):
        if os.path.exists(os.path.expanduser(app_server_path+ "/webapps/expertctstudio.war")):
            print "ExpertStudio Application already exists removing the old version of application \n"
            subprocess.check_output(" rm -rf " +app_server_path+"/webapps/expertctstudio.war && rm -rf " +app_server_path.strip()+"/webapps/expertctstudio", shell=True)
        if os.path.exists(os.path.expanduser(app_server_path+ "/webapps/ctmodelhouse.war")):
            print "CTModelhouse Application already exists removing the old version of application \n"
            subprocess.check_output(" rm -rf " +app_server_path+"/webapps/ctmodelhouse.war && rm -rf " +app_server_path.strip()+"/webapps/ctmodelhouse", shell=True)
        subprocess.check_output("cp ~/.canvas/expertctstudio.war "+app_server_path.strip()+"/webapps/", shell=True)
        subprocess.check_output("cp ~/.canvas/ctmodelhouse.war "+app_server_path.strip()+"/webapps/", shell=True)
        print 'Installed the ctmodelhouse,studio application in tomcat server \n'
        if(sigma_status=='Y'):
            if os.path.exists(os.path.expanduser(app_server_path+ "/webapps/sigma.war")):
                print "Sigma Application already exists removing the old version of application \n"
                subprocess.check_output(" rm -rf " +app_server_path+"/webapps/sigma.war && rm -rf " +app_server_path.strip()+"/webapps/sigma", shell=True)
                subprocess.check_output("cp ~/.canvas/sigma.war "+app_server_path.strip()+"/webapps/", shell=True)
                print 'Installed the Sigma application in tomcat server\n'
            else:                
                subprocess.check_output("cp ~/.canvas/sigma.war "+app_server_path.strip()+"/webapps/", shell=True)
                print 'Installed the Sigma application in tomcat server \n'
        else:
            print "Skipping the Installation of Sigma as User Preference \n"

def dbselect():
    db_value=raw_input('Enter DB Preference 1.Oracle 2.MySQL (input 1 or 2): ')    
    val = 0
    try:
        val = int(db_value)        
    except ValueError:
        print("input is not valid, Try again!!!")
        return ''
    if(val ==1 or val==2):
        if(val ==1):
            print 'You have choose Oracle as your Database \n'
            return 'Oracle'
        if(val ==2):
            print 'You have choose MySQL as your Database \n'
            return 'MySQL'
    else:
        print 'Choose between 1 and 2'
        print 'Please try again!!!'
        return ''

def dbinput():
    stream = os.popen('which mysql') 
    path = stream.read().strip()    
    if(len(path)==0):
        print 'MySQL is not installed in the default path...Please provide the mysql path to process \n'
        path=raw_input('Please provide the MySQL path:')
        print "\n"
    dbip=raw_input('Please provide the Database IP/FQDN:')
    print "\n"
    dbport=raw_input('Please provide the Database Port (Default port for MySQL is 3306 and Default port for Oracle is 1521):')
    print "\n"
    dbuser=raw_input('Please provide the Database username or Schema Name:')
    print "\n"
    dbpass= getpass.getpass('Please provide the Database password or Schema password(password will not be displayed):')              
    print "\n"
    return [path,dbip,dbuser,dbpass,dbport];

def connection_check(dbvalues):
    data=subprocess.check_output(['~/.canvas/tmpl/mysql_check.sh %s %s %s %s %s' % (dbvalues[0],dbvalues[1],dbvalues[2],dbvalues[3],dbvalues[4])],shell=True)    
    if(data.strip()!="success"):
        print "The given Host,username,password,port number is not able to connect to the Database server. Please check and try again \n"
    else:
        print "successfully connection established with the given inputs... Lets Proceed to further \n"
    return data.strip()        

def additionalInput():
    dbsir=raw_input("Please provide the service name or SID for oracle:")
    print "\n"
    return dbsir    

def update_dbentries(server_type,db_type,app_server_path,sigma_status,dbvalues,dbsir):
    subprocess.check_output("cp ~/.canvas/tmpl/* ~/.canvas/template/",shell=True)    
    subprocess.check_output("perl -p -i -e 's/{ip}/'"+dbvalues[1]+"'/g' ~/.canvas/template/*", shell=True)
    subprocess.check_output("perl -p -i -e 's/{port}/'"+dbvalues[4]+"'/g' ~/.canvas/template/*", shell=True)
    subprocess.check_output("perl -p -i -e 's/{user}/'"+dbvalues[2]+"'/g' ~/.canvas/template/*", shell=True)
    subprocess.check_output("perl -p -i -e 's/{pass}/'"+dbvalues[3]+"'/g' ~/.canvas/template/*", shell=True)
    subprocess.check_output("perl -p -i -e 's/{sirid}/'"+dbsir+"'/g' ~/.canvas/template/*", shell=True)
    if (server_type == 'tomcat' and db_type=='MySQL'):
        with open(app_server_path + '/conf/server.xml', "r") as f1:
            rem = f1.readlines()            
            f1.close()
        with open(app_server_path + '/conf/server.xml', "w") as f:
            for line in rem:
                if 'ModelHouseCT' in line or 'ModelHouse' in line or 'ExpertStudio' in line or 'ExpertStudioTarget' in line or 'SigmaCanvasDataSource' in line or 'SigmaAppDataSource' in line:                        
                    exist=1
                else:                    
                    f.write(line)
        f.close()                    
        if(sigma_status=='N'):
            tmp = open("/tmp/temp_server.xml", 'w')                 
            with open(app_server_path + '/conf/server.xml', 'r+') as fh:
                for line in fh:                    
                    tmp.write(line)
                    if '<GlobalNamingResources>' in line:
                        with open(os.path.expanduser('~/.canvas/template/s.txt'), 'r') as server:
                            for fi in server:                  
                                if 'ExpertStudioTarget' in fi or 'ExpertStudio' in fi or 'ModelHouse' in fi:                                                                        
                                    tmp.write(fi)
            tmp.close()
            fh.close()                                                                                                                                                                                                          
            print "Updated the DB Entries in server.xml \n"
        else:
            tmp = open("/tmp/temp_server.xml", 'w')                 
            with open(app_server_path + '/conf/server.xml', 'r+') as fh:
                for line in fh:
                    tmp.write(line)
                    if '<GlobalNamingResources>' in line:
                        with open(os.path.expanduser('~/.canvas/template/s.txt'), 'r') as server:
                            for fi in server:                                
                                tmp.write(fi)                                                                                                                
            tmp.close()                                             
            fh.close()
            print "Updated the DB Entries in server.xml"
        with open(app_server_path + '/conf/context.xml', "r") as f1:
            rem = f1.readlines()
            f1.close()
        with open(app_server_path + '/conf/context.xml', "w") as f:
            for line in rem:
                if 'ModelHouseCT' in line or 'ModelHouse' in line or 'ExpertStudio' in line or 'ExpertStudioTarget' in line or 'SigmaCanvasDataSource' in line or 'SigmaAppDataSource' in line or 'Container' in line or 'UserTransactionFactory' in line:                         
                    exist=1
                else:
                    f.write(line)
            f.close()                                 
        tmp = open("/tmp/temp_context.xml", 'w')
        f = open(os.path.expanduser('~/.canvas/template/c.txt'), 'r')
        text = f.read().strip()        
        f.close()
        with open(app_server_path + '/conf/context.xml', 'r+') as fh:
            for line in fh:
                tmp.write(line)
                if '<Context>' in line:
                    tmp.write(text)
                    print "Updated the DB Entries in context.xml \n"
        tmp.close()
        fh.close()            
        subprocess.check_output("mv /tmp/temp_server.xml " +app_server_path + "/conf/server.xml", shell=True)
        subprocess.check_output("mv /tmp/temp_context.xml " +app_server_path + "/conf/context.xml", shell=True)
    if (server_type == 'tomcat' and db_type=='Oracle'):
        with open(app_server_path + '/conf/server.xml', "r") as f1:
            rem = f1.readlines()
            f1.close()
        with open(app_server_path + '/conf/server.xml', "w") as f:
            for line in rem:
                if 'ModelHouseCT' in line or 'ModelHouse' in line or 'ExpertStudio' in line or 'ExpertStudioTarget' in line or 'SigmaAppDataSource' in line or 'SigmaCanvasDataSource' in line:
                    exist=1
                else:
                    f.write(line)
        f.close()
        if(sigma_status=='N'):
            tmp = open("/tmp/temp_server.xml", 'w')                 
            with open(app_server_path + '/conf/server.xml', 'r+') as fh:
                for line in fh:
                    tmp.write(line)
                    if '<GlobalNamingResources>' in line:
                        with open(os.path.expanduser('~/.canvas/template/os.txt'), 'r') as server:
                            for fi in server:                  
                                if 'ExpertStudioTarget' in fi or 'ExpertStudio' in fi or 'ModelHouse' in fi:                                    
                                    tmp.write(fi)                                                                                                                                                                                                          
            tmp.close()                                    
            fh.close()
            print "Updated the DB Entries in server.xml \n"
        else:
            tmp = open("/tmp/temp_server.xml", 'w')                 
            with open(app_server_path + '/conf/server.xml', 'r+') as fh:
                for line in fh:
                    tmp.write(line)
                    if '<GlobalNamingResources>' in line:
                        with open(os.path.expanduser('~/.canvas/template/os.txt'), 'r') as server:
                            for fi in server:                                
                                tmp.write(fi)                                                                                                                                
            tmp.close()                                             
            fh.close()
            print "Updated the DB Entries in server.xml \n"                                                
        with open(app_server_path + '/conf/context.xml', "r") as f1:
            rem = f1.readlines()
            f1.close()
        with open(app_server_path + '/conf/context.xml', "w") as f:
            for line in rem:
                if 'ModelHouseCT' in line or 'ModelHouse' in line or 'ExpertStudio' in line or 'ExpertStudioTarget' in line or 'SigmaCanvasDataSource' in line or 'SigmaAppDataSource' in line or 'Container' in line or 'UserTransactionFactory' in line:                         
                    exist=1
                else:
                    f.write(line)
            f.close()                                 
        tmp = open("/tmp/temp_context.xml", 'w')
        f = open(os.path.expanduser('~/.canvas/template/c.txt'), 'r')
        text = f.read().strip()        
        f.close()
        with open(app_server_path + '/conf/context.xml', 'r+') as fh:
            for line in fh:
                tmp.write(line)
                if '<Context>' in line:
                    tmp.write(text)
                    print "Updated the DB Entries in context.xml \n"
        tmp.close()
        fh.close()            
        subprocess.check_output("mv /tmp/temp_server.xml " +app_server_path + "/conf/server.xml", shell=True)
        subprocess.check_output("mv /tmp/temp_context.xml " +app_server_path + "/conf/context.xml", shell=True)

def dos2unixValidate():
    stream = os.popen('which dos2unix') 
    dosunix = stream.read().strip()    
    if(len(dosunix)==0):
        print 'dos2unix is not installed or it is not available in environment variable.Please install the dos2unix or if it installed please set in environment to proceed... \n'
        exit()        
    else:
        print "dos2unix is available \n"

def runDBScript(dbvalues,sigma_status):
    subprocess.check_output("rm -rf ~/.canvas/mysql", shell=True)
    subprocess.check_output("unzip ~/.canvas/canvasSetup_MYSQL.zip -d ~/.canvas/mysql", shell=True)
    tmp=open('/tmp/tmp_config.txt','w')
    result = dbvalues[0].rpartition("/")    
    path=result[0]    
    with open(os.path.expanduser('~/.canvas/mysql/bin/config.txt'), 'r+') as f:
        for line in f:
            if 'MYSQL_PATH' in line:                    
                a="MYSQL_PATH="+path                                
                tmp.write(a)
                tmp.write('\n')
            elif 'ADMIN_USER=root' in line:
                b="ADMIN_USER="+dbvalues[2]            
                tmp.write(b)
                tmp.write('\n')
            elif 'ADMIN_PASSWORD=Welcome01' in line:
                c="ADMIN_PASSWORD="+dbvalues[3]         
                tmp.write(c)
                tmp.write('\n')
            elif 'HOST=localhost' in line:
                d="HOST="+dbvalues[1]          
                tmp.write(d)
                tmp.write('\n')                                                                                             
            elif 'PORT=3306' in line:
                e="PORT="+dbvalues[4]          
                tmp.write(e)
                tmp.write('\n')     
            elif 'APP_LIST=modelhouse,ctstudio' in line:                
                if sigma_status=='Y':
                    h="APP_LIST=modelhouse,ctstudio"+",sigma"
                    tmp.write(h)
                    tmp.write('\n')
                else:
                    tmp.write(line)
            elif 'MULTI_APP=NO' in line:
                i="MULTI_APP=YES"
                tmp.write(i)
                tmp.write('\n')         
            elif 'MULTI_APP_SCHEMA' in line:
                j="MULTI_APP_SCHEMA=multi_app"
                tmp.write(j)
                tmp.write('\n')                 
            else:
                tmp.write(line)
    tmp.close()
    print "Updated the config.txt for mysql scripts \n"                         
    subprocess.check_output("rm ~/.canvas/mysql/bin/config.txt", shell=True)                    
    subprocess.check_output("mv /tmp/tmp_config.txt " "~/.canvas/mysql/bin/config.txt", shell=True)    
    subprocess.call("chmod -R 777 ~/.canvas/mysql/",shell=True) 
    print "Database scripts start executing.... \n"
    subprocess.call("cd ~/.canvas/mysql/bin/ && dos2unix -n config.txt config.txt", shell=True)
    subprocess.call("cd ~/.canvas/mysql/bin/ && bash ./run.sh", shell=True)

def pathReplacePDF():
    adminpath=os.path.expanduser("~/.canvas")    
    with open(os.path.expanduser("~/.canvas/Modelhouse/forReports/TempXML/CanvasFopUserconfig.xml")) as f:
        newText=f.read().replace('D:\Canvas',adminpath).replace("\\","/")
    with open(os.path.expanduser("~/.canvas/Modelhouse/forReports/TempXML/CanvasFopUserconfig.xml"), "w") as f:
        f.write(newText)
        f.close()
    with open(os.path.expanduser("~/.canvas/ExpertModeCTStudio/forReports/TempXML/CanvasFopUserconfig.xml")) as f:
        newText=f.read().replace('D:\Canvas',adminpath).replace("\\","/")
    with open(os.path.expanduser("~/.canvas/ExpertModeCTStudio/forReports/TempXML/CanvasFopUserconfig.xml"), "w") as f:
        f.write(newText)
        f.close()        

def copyTransactionJars(server_type,app_server_path):
    if (server_type == 'tomcat'):
        subprocess.check_output("cp ~/.canvas/transactionjars/* " + app_server_path + "/lib/", shell=True)
        subprocess.check_output("cp ~/.canvas/mysql-connector-java-8.0.16.jar "+app_server_path+"/lib/ && cp ~/.canvas/ojdbc6.jar "+app_server_path+"/lib/", shell=True)
        
def finish(server_type,db_type):
    if (server_type == 'tomcat' and db_type=="Oracle"):
        print "RUN the Database Scripts that is available in canvas home folder(canvasSetup_oracle.zip) and start the tomcat server \n"        
        print 'You have successfully Installed Canvas!!! Ready to Rock and Roll'        
    if (server_type =='tomcat' and db_type=="MySQL"):
        print "Application and DB Setup Done. Now it is time to start the tomcat server...\n"
        print 'You have successfully Installed Canvas!!! Ready to Rock and Roll'                      

install()