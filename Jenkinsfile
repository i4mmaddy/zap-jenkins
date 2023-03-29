pipeline{
  agent any 
  stages{
    stage('mkdir'){
      steps{
          sh 'mkdir ${WORKSPACE}/zap/wrk'   
      }
    }
    stage('aranga'){
      steps{
         sh 'python3 ./arangra.py'      
      }
    }
  }
}
