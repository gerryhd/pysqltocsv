pipeline {
    agent { docker { image 'python:3.8.10' } }
    stages {
        stage('build') {
            steps {
	    	dir("/home/gerardo/misc") {
	        	sh "cd /home/gerardo/misc"
              		sh "docker build -t pysqltocsv-${GIT_BRANCH}:${BUILD_NUMBER} ."
			sh 'docker run -e MEGA_USER=gerry_hd@live.com.mx -e MEGA_PASSWORD=LunSi3d4 pysqltocsv-${GIT_BRANCH}:${BUILD_NUMBER}'
		}
            }
        }
    }
}
