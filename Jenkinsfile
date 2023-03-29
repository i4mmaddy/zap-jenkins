pipeline{
  agent any 
  stages{
    stage('mkdir'){
      steps{
          sh 'mkdir ${WORKSPACE}/arana'   
      }
    }
    stage('aranga'){
      steps{
         sh 'python3 ./arangra.py'      
      }
    }
  }
}
