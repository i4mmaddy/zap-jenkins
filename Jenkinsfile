pipeline{
  agent any 
  stages{
    stage('mkdir'){
      steps{
          sh 'mkdir ${WORKSPACE}/zap'   
      }
    }
    stage('aranga'){
      steps{
         sh 'python3 ./arangra.py'      
      }
    }
  }
}
