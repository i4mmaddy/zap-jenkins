pipeline{
  agent any 
  stages{
    stage('mkdir'){
      steps{
          sh 'mkdir -p ${WORKSPACE}/zap/wrk'   
      }
    }
    stage('aranga'){
      steps{
         sh 'python3 ./arangra.py'      
      }
    }
  }
}
